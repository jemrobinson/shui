"""Module for interacting with remote Apache server"""
from .download import download_version, get_file_details
from .install import extract_tarball
from .versions import get_versions

__all__ = [
    "download_version",
    "extract_tarball",
    "get_file_details",
    "get_versions",
]
