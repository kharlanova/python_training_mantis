from model.project import Project
import random


def test_delete_some_project(app):
    if len(app.project.get_project_list()) == 0:
        p = Project(name="Test")
        app.project.create_project(p)
    app.project.get_project_list()
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=lambda x: x.name) == sorted(new_projects, key=lambda x: x.name)

