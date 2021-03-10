from shifl.commands import InstallCommand, VersionsCommand
from cleo import Application

application = Application("shifl", "0.1.0", complete=True)
application.add(InstallCommand())
application.add(VersionsCommand())

#if __name__ == "__main__":
def main():
    application.run()