import tomli

from urllib import request
from project import Project

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        toml_dict = tomli.loads(content)
        project = Project("", "", [], [])
        project.name = toml_dict["tool"]["poetry"]["name"]
        project.description = toml_dict["tool"]["poetry"]["description"]
        for i in toml_dict["tool"]["poetry"]["dependencies"]:
            project.dependencies.append(i)
        for j in toml_dict["tool"]["poetry"]["dev-dependencies"]:
            project.dev_dependencies.append(j)
        return project
