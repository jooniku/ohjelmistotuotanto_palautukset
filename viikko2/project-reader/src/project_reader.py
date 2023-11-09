from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_dict = tomli.loads(content)

        info = toml_dict["tool"]["poetry"]

        name = info["name"]
        description = info["description"]
        license = info["license"]
        authors = info["authors"]
        dependencies = info["dependencies"]
        dev_dependencies = info["group"]["dev"]["dependencies"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dependencies)
