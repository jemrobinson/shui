"""Base include for shui (Spark-Hadoop Unix Installer)"""
try:
    from importlib import metadata
except ImportError:
    # This is needed to support Python 3.7
    import importlib_metadata as metadata

__version__ = metadata.version("shui")
