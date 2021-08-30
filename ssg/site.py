from os import mkdir
import pathlib 

class Site():

    def __init__(self, source, dest) -> None:
        self._source = pathlib.Path(source)
        self._dest = pathlib.Path(dest)

    def create_dir(self, path):
        #directory = f"{self._dest}/{self._source.relative_to(path)}"
        directory = self._dest / self._source.relative_to(path)

        mkdir(directory, parents=True, exist_ok=True)

    def build(self):

        mkdir(self._dest, parents=True, exist_ok=True)

        for path in self._source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
                


