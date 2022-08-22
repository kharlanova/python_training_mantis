from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        soap_config = self.app.config["soap"]
        client = Client(soap_config["host"])
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list_user(self, username, password):
        soap_config = self.app.config["soap"]
        client = Client(soap_config["host"])
        projects_list = []

        for project in client.service.mc_projects_get_user_accessible(username,password):
            projects_list.append(Project(name=project.name))
        return projects_list

    def get_projects_list_administrator(self):
        soap_config = self.app.config["soap"]
        return self.get_projects_list_user(soap_config["username"], soap_config["password"])