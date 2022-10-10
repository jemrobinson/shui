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
            
            import os
            
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(f_tarball, install_dir)
    except tarfile.ReadError as exc:
        raise IOError(f"<info>{tarball.path}</info> is not a valid tarball!") from exc
    return install_dir / extraction_dir
