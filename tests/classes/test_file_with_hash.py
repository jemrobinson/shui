import pytest
from pathlib3x import Path

from shui.classes import FileInfo, FileWithHash


@pytest.fixture
def testfile(tmp_path: Path) -> FileInfo:
    file_path = tmp_path / "testfile"
    file_info = FileInfo("https://example.com", file_path)
    with open(file_info.path, "w") as f_out:
        f_out.write("content\n")
    return file_info


@pytest.fixture
def testhashfile(tmp_path: Path) -> FileInfo:
    file_path = tmp_path / "testfile.sha512"
    file_info = FileInfo("https://example.com", file_path)
    return file_info


@pytest.fixture
def filewithhash(testfile: FileInfo, testhashfile: FileInfo) -> FileWithHash:
    return FileWithHash(testfile, testhashfile)


class TestFileWithHash:
    def test_init(self, testfile: FileInfo) -> None:
        with pytest.raises(ValueError):
            FileWithHash(testfile, testfile)

    def test_iter(
        self, filewithhash: FileWithHash, testfile: FileInfo, testhashfile: FileInfo
    ) -> None:
        objects = list(filewithhash)
        assert len(objects) == 2
        assert objects[0] == testfile
        assert objects[1] == testhashfile

    def test_remove(self, filewithhash: FileWithHash) -> None:
        filewithhash.remove()
        assert filewithhash.file.path.is_file() == False
        assert filewithhash.hashfile.path.is_file() == False

    def test_verify(self, filewithhash: FileWithHash) -> None:
        with open(filewithhash.hashfile.path, "w") as f_out:
            f_out.write(
                "90eecf7b3db9ea38dda020755b28405c5267c8865e76bd9847f4f2f8c95a7ebfbe1e2c81ab9766573535389264178eda6ca951287471840115bd403668a4ec37\n"
            )
        assert filewithhash.verify() == True
        with open(filewithhash.hashfile.path, "w") as f_out:
            f_out.write("incorrect_hash")
        assert filewithhash.verify() == False
