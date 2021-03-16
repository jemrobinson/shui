"""Functions for downloading a particular version from the remote repository"""
from tqdm import tqdm
import requests


def download_version(remote_url, local_path):
    """Download a particular Spark/Hadoop version from a remote URL to a local path"""
    response = requests.get(remote_url, stream=True, allow_redirects=True)
    total_size = int(response.headers.get("content-length"))
    with open(local_path, "wb") as output_file:
        with tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    output_file.write(chunk)
                    progress_bar.update(len(chunk))


def get_paths(version, install_dir):
    """Construct local paths for a particular Spark/Hadoop version"""
    tarball_path = install_dir / version.filename
    sha512_path = tarball_path.append_suffix(".sha512")
    return {
        "file": {"url": version.url, "path": tarball_path},
        "sha512": {"url": f"{version.url}.sha512", "path": sha512_path},
    }
