"""Functions for downloading a particular version from the remote repository"""
from tqdm import tqdm
import requests
from shui.classes import FileInfo, FileWithHash


def download_version(fileinfo):
    """Download a particular Spark/Hadoop version from a remote URL to a local path"""
    response = requests.get(fileinfo.url, stream=True, allow_redirects=True)
    total_size = int(response.headers.get("content-length"))
    with open(fileinfo.path, "wb") as output_file:
        with tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    output_file.write(chunk)
                    progress_bar.update(len(chunk))


def get_file_details(version, install_dir):
    """Construct local paths for a particular Spark/Hadoop version"""
    tarball_path = install_dir / version.filename
    sha512_path = tarball_path.append_suffix(".sha512")
    return FileWithHash(
        FileInfo(version.url, tarball_path),
        FileInfo(f"{version.url}.sha512", sha512_path),
    )
