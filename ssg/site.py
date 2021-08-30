from os import mkdir
from pathlin import Path 

class Site():

    def __init__(self, source, dest) -> None:
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        #directory = f"{self._dest}/{self._source.relative_to(path)}"
        directory = self.dest / self.source.relative_to(path)

        mkdir(directory, parents=True, exist_ok=True)

    def build(self):

        mkdir(self.dest, parents=True, exist_ok=True)

        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
                


