from shifl.commands import InstallCommand, VersionsCommand
from cleo import Application

application = Application()
application.add(InstallCommand())
application.add(VersionsCommand())

if __name__ == "__main__":
    application.run()