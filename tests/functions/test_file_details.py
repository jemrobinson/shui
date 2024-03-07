from pathlib3x import Path

from shui.classes import Version
from shui.functions import get_file_details


class TestFileDetails:
    def test_get_file_details(self, tmp_path: Path) -> None:
        version = Version("spark-3.5.0-bin-hadoop3.tgz", "https://example.com/file.tgz")
        install_dir = Path(tmp_path) / "install"
        filewithhash = get_file_details(version, install_dir)
        assert filewithhash.file.url == "https://example.com/file.tgz"
        assert filewithhash.file.path == install_dir / "spark-3.5.0-bin-hadoop3.tgz"
        assert filewithhash.hashfile.url == "https://example.com/file.tgz.sha512"
        assert (
            filewithhash.hashfile.path
            == install_dir / "spark-3.5.0-bin-hadoop3.tgz.sha512"
        )
