from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        toml = tomli.loads(content)

        block = toml.get("tool", {}).get("poetry", {})
        name = block.get("name", "N/A")
        desc = block.get("description", "N/A")
        authors = block.get("authors", [])
        license = block.get("license", "N/A")
        dependencies = list(block.get("dependencies", {}).keys())
        dev_dependencies = list(block.get("group", {}).get("dev", {}).get("dependencies", {}).keys())

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, authors, license, dependencies, dev_dependencies)