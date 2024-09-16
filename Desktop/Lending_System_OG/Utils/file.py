import os


def ensure_directory_exists(directory_path):
    """Ensure that a directory exists; create it if it does not."""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
