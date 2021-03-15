"""Functions for downloading a particular version from the remote repository"""
import hashlib
import tarfile
import requests


def install_version(logger, version, install_dir):
    """Download and install a particular Spark/Hadoop version"""
    # Construct local paths
    logger(f"Installing {version} to <info>{install_dir}</info>")
    tarball_path = install_dir / version.filename
    sha512_path = tarball_path.append_suffix(".sha512")
    # Download tarball and SHA512 sum
    download(logger, version.url, tarball_path, as_bytes=True)
    download(logger, f"{version.url}.sha512", sha512_path, as_bytes=False)
    # Verify tarball
    if verify_tarball(tarball_path, sha512_path):
        logger(f"Verified SHA512 hash for <info>{version.filename}</info>")
    else:
        raise IOError(f"Could not verify {version} using SHA512!")
    # Extract tarball
    if not tarball_path.is_file():
        raise ValueError(f"Could not download {version} to <info>{install_dir}</info>!")
    with tarfile.open(tarball_path, "r:gz") as f_tarball:
        f_tarball.extractall(install_dir)
    # Remove tarball
    tarball_path.unlink()


def download(logger, remote_url, local_path, as_bytes):
    """Download from a remote URL to a local path"""
    logger(f"Downloading from <info>{remote_url}</info>...")
    response = requests.get(remote_url, stream=True)
    if response.status_code == 200:
        with open(local_path, "wb") as f_local:
            if as_bytes:
                f_local.write(response.raw.read())
            else:
                f_local.write(response.content)


def verify_tarball(file_path, sha512_path):
    """Verify that a file matches its SHA512 hash"""
    # Get the file hash
    file_hash = hashlib.sha512()
    buffer_size = 524288  # read in chunks of 512kb
    with open(file_path, "rb") as input_file:
        while (input_bytes := input_file.read(buffer_size)) :
            file_hash.update(input_bytes)
    calculated_hash = file_hash.hexdigest().lower()
    # Read the reference hash
    with open(sha512_path, "r") as input_hash:
        reference_hash = (
            "".join(input_hash.readlines())
            .replace("\n", " ")
            .replace(" ", "")
            .split(":")[1]
            .strip()
            .lower()
        )
    return calculated_hash == reference_hash
