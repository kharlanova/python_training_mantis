from selenium import webdriver

from fixture.project import ProjectHelper
from fixture.session import SessionHelper
from fixture.soap import SoapHelper


class Application:
    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError ("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.soap = SoapHelper(self)
        self.project = ProjectHelper(self)
        self.base_url = config["web"]["baseUrl"]
        self.config = config

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()