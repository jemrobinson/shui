"""Functions for installing a particular version from a local tarball"""
import tarfile
import pathlib3x as pathlib
from shui.classes import FileInfo


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


def safe_extract(
    tarfile: tarfile.TarFile,
    extract_path: pathlib.Path,
    members=None,
    numeric_owner=False,
):
    """Extract tarfile to extract_path while validating that no files are extracted outside the base path"""
    for member in tarfile.getmembers():
        member_path = extract_path / member.name
        if member_path not in extract_path.resolve().parents:
            raise IOError(
                f"Tar file attempted to extract to {member_path} which is outside the base path {extract_path}."
            )
    tarfile.extractall(extract_path, members, numeric_owner=numeric_owner)
