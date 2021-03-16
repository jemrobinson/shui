"""Functions for installing a particular version from a local tarball"""
import tarfile


def extract_tarball(tarball, install_dir):
    """Extract tarball to a local path"""
    if not tarball.path.is_file():
        raise ValueError(
            f"Could not find a valid tarball at <info>{tarball.path}</info>!"
        )
    with tarfile.open(tarball.path, "r:gz") as f_tarball:
        extraction_dir = [
            obj.name
            for obj in f_tarball.getmembers()
            if obj.isdir() and "/" not in obj.name
        ][0]
        f_tarball.extractall(install_dir)
    return install_dir / extraction_dir
