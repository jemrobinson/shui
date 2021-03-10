from cleo import Command
from shifl.api import get_versions


class VersionsCommand(Command):
    """
    Get available Spark and Hadoop versions

    versions
        {--latest : Show only the latest available version}
    """

    def handle(self):
        versions = get_versions()
        if self.option("latest"):
            versions = [sorted(versions)[-1]]
        for version in versions:
            self.line(f"  - Found {version}")
