from os import mkdir
from pathlib import Path 

class Site():

    def __init__(self, source, dest) -> None:
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        #directory = f"{self._dest}/{self._source.relative_to(path)}"
        directory = self.dest / path.relative_to(self.source)

        directory.mkdir(parents=True, exist_ok=True)

    def build(self):

        self.dest.mkdir(parents=True, exist_ok=True)

        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
                


