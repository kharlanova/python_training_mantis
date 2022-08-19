from selenium.webdriver.common.by import By

from model.project import Project

class ProjectHelper:
    def __init__(self, app):
        self.app = app



    def open_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            sidebar = wd.find_element(By.ID, "sidebar")
            last = sidebar.find_elements(By.TAG_NAME, "li")[-1]
            last.find_element(By.XPATH, "./a[@href]").click()
            top_bar = wd.find_element(By.CLASS_NAME, "page-content")
            manage_projects_tab = top_bar.find_elements(By.TAG_NAME, "li")[2]
            manage_projects_tab.find_element(By.XPATH, "./a[@href]").click()

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.project_cache = []
            table = wd.find_element(By.CLASS_NAME, "table-responsive")
            body = table.find_element(By.TAG_NAME, "tbody")
            rows = body.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                tds = row.find_elements(By.XPATH, ".//child::td")
                name = tds[0].text
                self.project_cache.append(Project(name=name))
        return list(self.project_cache)

    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element(By.ID, "project-name").click()
        wd.find_element(By.ID, "project-name").send_keys(project.name)
        wd.find_element(By.CSS_SELECTOR, ".btn-white").click()
        wd.find_element(By.LINK_TEXT, "Proceed").click()

    def create_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element(By.XPATH,"//button[@type='submit']").click()
        wd.find_element(By.ID,"project-name").click()
        wd.find_element(By.ID,"project-name").clear()
        wd.find_element(By.ID,"project-name").send_keys(project.name)
        wd.find_element(By.XPATH,"//input[@value='Add Project']").click()
        self.open_projects_page()
        self.project_cache = None

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element(By.LINK_TEXT, name).click()
        wd.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()
        wd.find_element(By.CSS_SELECTOR, ".btn-white").click()
        self.open_projects_page()
        self.project_cache = None




