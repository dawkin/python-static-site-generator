from pathlib import Path

from typing import List

import shutil


class Parser:
    def __init__(self):
        self.extensions = List[str]

    def valid_extension(self, extension):
        is_valid_extension = False
        if extension in self.extensions:
            is_valid_extension = True
        return is_valid_extension

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    @staticmethod
    def read(path):
        with open(path) as file:
            return file.read()

    @staticmethod
    def write(path, dest, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path) as file:
            file.write(content)

    @staticmethod
    def copy(path, source, dest):
        copy_path = dest / path.relative_to(source)
        shutil.copy2(path, copy_path)


class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        super.copy(path, source, dest)
