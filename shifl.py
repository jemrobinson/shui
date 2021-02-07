from shifl.commands import VersionsCommand
from cleo import Application

application = Application()
application.add(VersionsCommand())

if __name__ == "__main__":
    application.run()