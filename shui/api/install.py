"""Functions for installing a particular version from a local tarball"""
import hashlib
import tarfile


def cleanup(path_details):
    """Remove tarball and SHA512 hash"""
    for path in [details["path"] for details in path_details.values()]:
        if path.is_file():
            path.unlink()


def extract_tarball(tarball_path, install_dir):
    """Extract tarball to a local path"""
    if not tarball_path.is_file():
        raise ValueError(
            f"Could not find a valid tarball at <info>{tarball_path}</info>!"
        )
    with tarfile.open(tarball_path, "r:gz") as f_tarball:
        extraction_dir = [
            obj.name
            for obj in f_tarball.getmembers()
            if obj.isdir() and "/" not in obj.name
        ][0]
        f_tarball.extractall(install_dir)
    return install_dir / extraction_dir


def verify_tarball(path_details):
    """Verify that a file matches its SHA512 hash"""
    file_path = path_details["file"]["path"]
    sha512_path = path_details["sha512"]["path"]
    # Get the file hash
    file_hash = hashlib.sha512()
    buffer_size = 524288  # read in chunks of 512kb
    with open(file_path, "rb") as input_file:
        while input_bytes := input_file.read(buffer_size):
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
