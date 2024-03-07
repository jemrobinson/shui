from shui.classes import Version


class TestVersion:
    version_350 = Version("spark-3.5.0-bin-hadoop3.tgz", "https://example.com")
    version_351 = Version("spark-3.5.1-bin-hadoop3.tgz", "https://example.com")
    version_352 = Version("spark-3.5.2-bin-hadoop3.tgz", "https://example.com")

    def test_hadoop(self) -> None:
        assert self.version_351.hadoop == "3"

    def test_spark(self) -> None:
        assert self.version_351.spark == "3.5.1"

    def test_str(self) -> None:
        assert (
            str(self.version_351)
            == "<comment>Spark</comment> (<info>3.5.1</info>) <comment>Hadoop</comment> (<info>3</info>)"
        )

    def test_repr(self) -> None:
        assert (
            repr(self.version_351)
            == "<Version spark-3.5.1-bin-hadoop3.tgz https://example.com>"
        )

    def test_ordering(self) -> None:
        ordered = sorted([self.version_351, self.version_352, self.version_350])
        assert ordered == [self.version_350, self.version_351, self.version_352]
