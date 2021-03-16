"""Class to relate local and remote information about a Spark/Hadoop file"""


class FileInfo:
    """Class to relate local and remote information about a Spark/Hadoop file"""

    def __init__(self, remote_url, local_path):
        self.url = remote_url
        self.path = local_path

    @property
    def name(self):
        """Get the name of the local file"""
        return self.path.name

    @property
    def is_hashfile(self):
        """Boolean indicating whether this is a hashfile"""
        return self.path.suffix == ".sha512"

    def is_hash_for(self, other):
        """Boolean indicating whether this is the hashfile corresponding to another file"""
        return self.is_hashfile and self.path.stem == other.path.name
