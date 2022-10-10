"""Functions for installing a particular version from a local tarball"""
import os
import tarfile
import pathlib3x as pathlib
from shui.classes import FileInfo


def is_within_directory(directory, target):
    abs_directory = os.path.abspath(directory)
    abs_target = os.path.abspath(target)
    prefix = os.path.commonprefix([abs_directory, abs_target])
    return prefix == abs_directory


def extract_tarball(tarball: FileInfo, install_dir: pathlib.Path) -> pathlib.Path:
    """Extract tarball to a local path"""
    if not tarball.path.is_file():
        raise IOError(f"<info>{tarball.path}</info> is not a file!")
    try:
        with tarfile.open(tarball.path, "r:gz") as f_tarball:
            extraction_dir = [
                obj.name
                for obj in f_tarball.getmembers()
                if obj.isdir() and "/" not in obj.name
            ][0]
            safe_extract(f_tarball, install_dir)
    except tarfile.ReadError as exc:
        raise IOError(f"<info>{tarball.path}</info> is not a valid tarball!") from exc
    return install_dir / extraction_dir


def safe_extract(tar: tarfile.TarFile, path: str, members=None, *, numeric_owner=False):
    for member in tar.getmembers():
        member_path = os.path.join(path, member.name)
        if not is_within_directory(path, member_path):
            raise IOError(
                f"Tar file attempted to extract to {member_path} which is outside its base path."
            )
    tar.extractall(path, members, numeric_owner=numeric_owner)
