import re
import requests
from bs4 import BeautifulSoup
from url_normalize import url_normalize
from shifl.version import Version


def match_links(url, compiled_regex):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    matches = {
        elem.string: url_normalize(f"{url}/{elem['href']}")
        for elem in soup.find_all("a")
        if compiled_regex.match(elem["href"])
    }
    return matches


def get_versions():
    versions = []

    spark_version_dict = match_links(
        "https://archive.apache.org/dist/spark/", re.compile("spark-*")
    )
    for version in spark_version_dict:
        full_version_dict = match_links(spark_version_dict[version], Version.regex)
        versions += [
            Version(filename, url) for filename, url in full_version_dict.items()
        ]

    return versions
