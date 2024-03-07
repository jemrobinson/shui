import pytest
from pathlib3x import Path

from shui.classes import FileInfo, FileWithHash
from shui.functions import extract_tarball


@pytest.fixture
def fixtures_directory() -> Path:
    return Path(__file__).parent.parent.resolve() / "fixtures"


@pytest.fixture
def filewithhash(testfile: FileInfo, testhashfile: FileInfo) -> FileWithHash:
    return FileWithHash(testfile, testhashfile)


@pytest.fixture
def spark_example_tgz(fixtures_directory: Path) -> bytes:
    return FileInfo(
        "https://example.com/example.tgz", fixtures_directory / "example.tgz"
    )


@pytest.fixture
def spark_example_tgz_hash(fixtures_directory: Path) -> FileInfo:
    return FileInfo(
        "https://example.com/example.tgz.sha512",
        fixtures_directory / "example.tgz.sha512",
    )


def test_extract_tarball(
    spark_example_tgz: FileInfo, spark_example_tgz_hash: FileInfo, tmp_path: Path
) -> None:
    file_with_hash = FileWithHash(spark_example_tgz, spark_example_tgz_hash)
    install_dir = Path(tmp_path) / "install"
    assert extract_tarball(file_with_hash.file, install_dir) == install_dir / "spark"
