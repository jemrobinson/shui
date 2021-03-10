from shui.commands import InstallCommand, VersionsCommand
from cleo import Application

application = Application("shui", "0.1.0", complete=True)
application.add(InstallCommand())
application.add(VersionsCommand())


def main():
    application.run()