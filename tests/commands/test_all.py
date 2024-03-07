import pytest
import requests_mock
from cleo.application import Application
from cleo.testers.application_tester import ApplicationTester
from pathlib3x import Path

from shui.commands import InstallCommand, VersionsCommand


@pytest.fixture()
def app() -> Application:
    app = Application()
    app.add(InstallCommand())
    app.add(VersionsCommand())
    return app


@pytest.fixture()
def tester(app: Application) -> ApplicationTester:
    return ApplicationTester(app)


@pytest.fixture
def fixtures_directory() -> Path:
    return Path(__file__).parent.parent.resolve() / "fixtures"


@pytest.fixture
def spark_350_html(fixtures_directory: Path) -> str:
    with open(fixtures_directory / "spark_350.html", "r") as f_in:
        content = f_in.readlines()
    return "\n".join(content)


@pytest.fixture
def spark_351_html(fixtures_directory: Path) -> str:
    with open(fixtures_directory / "spark_351.html", "r") as f_in:
        content = f_in.readlines()
    return "\n".join(content)


@pytest.fixture
def spark_main_html(fixtures_directory: Path) -> str:
    with open(fixtures_directory / "spark_main.html", "r") as f_in:
        content = f_in.readlines()
    return "\n".join(content)


@pytest.fixture
def spark_example_tgz(fixtures_directory: Path) -> bytes:
    with open(fixtures_directory / "example.tgz", "rb") as f_in:
        content = f_in.read()
    return content


@pytest.fixture
def spark_example_tgz_hash() -> str:
    return "4c63792055a083e8c770370f22240853dc64da96e3200c7aa2710607b841bb0972c29eece43b068dd11c4f77719427b6c48df27e6e389efd664fb3e9b9743f9f\n"


def test_install_fail(
    tester: ApplicationTester,
    spark_main_html: str,
    spark_350_html: str,
    spark_351_html: str,
) -> None:
    with requests_mock.Mocker() as request:
        request.get("https://archive.apache.org/dist/spark/", text=spark_main_html)
        request.get(
            "https://archive.apache.org/dist/spark/spark-3.5.0/", text=spark_350_html
        )
        request.get(
            "https://archive.apache.org/dist/spark/spark-3.5.1/", text=spark_351_html
        )
        assert tester.execute("install --spark 3.5.0 --hadoop 4") == 1


def test_install_succeed(
    tester: ApplicationTester,
    spark_main_html: str,
    spark_350_html: str,
    spark_351_html: str,
    spark_example_tgz: bytes,
    spark_example_tgz_hash: str,
    tmp_path: Path,
) -> None:
    with requests_mock.Mocker() as request:
        request.get("https://archive.apache.org/dist/spark/", text=spark_main_html)
        request.get(
            "https://archive.apache.org/dist/spark/spark-3.5.0/", text=spark_350_html
        )
        request.get(
            "https://archive.apache.org/dist/spark/spark-3.5.1/", text=spark_351_html
        )
        request.get(
            "https://archive.apache.org/dist/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz",
            content=spark_example_tgz,
        )
        request.get(
            "https://archive.apache.org/dist/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz.sha512",
            text=spark_example_tgz_hash,
        )
        assert (
            tester.execute(f"install --spark 3.5.0 --hadoop 3 --target {tmp_path}") == 0
        )


def test_versions_latest(
    tester: ApplicationTester,
    spark_main_html: str,
    spark_350_html: str,
    spark_351_html: str,
) -> None:
    with requests_mock.Mocker() as request:
        request.get("https://archive.apache.org/dist/spark/", text=spark_main_html)
        request.get(
            "https://archive.apache.org/dist/spark/spark-3.5.0/", text=spark_350_html
        )
        request.get(
            "https://archive.apache.org/dist/spark/spark-3.5.1/", text=spark_351_html
        )
        assert tester.execute("versions --latest") == 0
        assert tester.status_code == 0
        assert (
            tester.io.fetch_output().strip()
            == "Available version: Spark (3.5.1) Hadoop (3)"
        )
