import pytest
import requests_mock

from shui.classes import FileInfo


@pytest.fixture
def testfile(tmp_path) -> FileInfo:
    file_path = tmp_path / "testfile"
    return FileInfo("https://example.com", file_path)


@pytest.fixture
def testhashfile(tmp_path) -> FileInfo:
    file_path = tmp_path / "testfile.sha512"
    return FileInfo("https://example.com", file_path)


class TestFileInfo:
    def test_download(self, testfile: FileInfo) -> None:
        with requests_mock.Mocker() as request:
            request.get("https://example.com", text="content")
            testfile.download()
            with open(testfile.path, "rb") as f_test:
                content = f_test.readlines()
        assert content == [b"content"]

    def test_is_hashfile(self, testfile: FileInfo, testhashfile: FileInfo) -> None:
        assert testfile.is_hashfile == False
        assert testhashfile.is_hashfile == True

    def test_is_hash_for(self, testfile: FileInfo, testhashfile: FileInfo) -> None:
        assert testhashfile.is_hash_for(testfile) == True

    def test_name(self, testfile: FileInfo) -> None:
        assert testfile.name == "testfile"

    def test_remove(self, testfile: FileInfo) -> None:
        testfile.remove()
        assert testfile.path.is_file() == False
