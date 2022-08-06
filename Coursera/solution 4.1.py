import os.path
import tempfile
import uuid


class File:

    def __init__(self, path):
        self.path = self.create_file(path)

    def __str__(self):
        return self.path

    def __iter__(self):
        with open(self.path, "r") as file:
            self.lines = iter(file.readlines())
        return self

    def __next__(self):
        return next(self.lines)

    def __add__(self, other):
        text = File(os.path.join(tempfile.gettempdir(), str(uuid.uuid4())))
        with open(text.path, 'w') as new_file, open(self.path, 'r') as file1, open(other.path, 'r') as file2:
            new_file.write(file1.read() + file2.read())
        return text

    def read(self):
        with open(self.path, 'r') as file:
            return file.read()

    def write(self, text):
        with open(self.path, 'w') as file:
            return file.write(text)

    @staticmethod
    def create_file(path):
        if not os.path.exists(path):
            with open(path, "w"):
                pass
        return path



