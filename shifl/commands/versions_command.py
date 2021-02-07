import re
import requests
from bs4 import BeautifulSoup
from cleo import Command
from url_normalize import url_normalize
from shifl.version import Version


class VersionsCommand(Command):
    """
    Get available Spark and Hadoop versions

    versions
    """

    @staticmethod
    def match_links(url, compiled_regex):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        matches = {
            elem.string: url_normalize(f"{url}/{elem['href']}")
            for elem in soup.find_all("a")
            if compiled_regex.match(elem["href"])
        }
        return matches

    def handle(self):
        versions = []

        spark_version_dict = VersionsCommand.match_links(
            "https://archive.apache.org/dist/spark/", re.compile("spark-*")
        )
        for version in spark_version_dict:
            full_version_dict = VersionsCommand.match_links(
                spark_version_dict[version], Version.regex
            )
            versions += [
                Version(filename, url) for filename, url in full_version_dict.items()
            ]

        for version in versions:
            self.line(f"  - Found <info>{version}</info>")
