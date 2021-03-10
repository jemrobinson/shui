from cleo import Command
from shifl.api import get_versions, install_version


class InstallCommand(Command):
    """
    Install a particular Spark and Hadoop version

    install
        {--latest : Use the latest available version}
        {--spark=any : Spark version}
        {--hadoop=any : Hadoop version}
    """

    def handle(self):
        if self.option("latest"):
            selected_version = sorted(get_versions())[-1]
        else:
            matching_versions = get_versions()
            if self.option("spark") != "any":
                matching_versions = [v for v in matching_versions if v.spark == self.option("spark")]
            if self.option("hadoop") != "any":
                matching_versions = [v for v in matching_versions if v.hadoop == self.option("hadoop")]
            if not len(matching_versions) == 1:
                self.line(f"Found {len(matching_versions)} versions matching <comment>Spark</comment> <info>{self.option('spark')}</info>; <comment>Hadoop</comment> <info>{self.option('hadoop')}</info>")
                for version in matching_versions:
                    self.line(f"  - Found {version}")
                raise ValueError("Could not identify version to install!")
            selected_version = matching_versions[0]
        install_version(self.line, selected_version)
