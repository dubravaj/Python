# Context manager demo

# create simple context manager resource
# with statement create a runtime context

import contextlib


# class based context manager
class ActivityManager:
    """Simple class-based context manager"""

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()

        
# function based context manager
