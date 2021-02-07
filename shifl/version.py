import re


class Version:
    regex = re.compile("spark-([0-9.]*)-bin-hadoop([0-9.]*).tgz$")

    def __init__(self, filename, url):
        self.filename = filename
        self.url = url

    @property
    def spark(self):
        return self.regex.match(self.filename).group(1)

    @property
    def hadoop(self):
        return self.regex.match(self.filename).group(1)

    def __str__(self):
        return f"<comment>Spark</comment> (<info>{self.spark}</info>) <comment>Hadoop</comment> (<info>{self.hadoop}</info>)"

    def __repr__(self):
        return f"<Version {self.filename} {self.url}>"
