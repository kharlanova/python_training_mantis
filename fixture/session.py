from selenium.webdriver.common.by import By


class SessionHelper:


    def __init__(self, app):
        self.app = app


    def login(self, username, password):
        # login
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME,"username").click()
        wd.find_element(By.NAME,"username").clear()
        wd.find_element(By.NAME,"username").send_keys(username)
        wd.find_element(By.XPATH,"//input[@value='Вход']").click()
        wd.find_element(By.NAME,"password").click()
        wd.find_element(By.NAME,"password").clear()
        wd.find_element(By.NAME,"password").send_keys(password)
        wd.find_element(By.XPATH,"//input[@value='Вход']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, ".fa:nth-child(3)").click()
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.ID,"navbar")) > 0

    def is_logged_in_as(self,username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH,'.//span[@class = "user-info"]').text

    def ensure_login(self, username,password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username,password)




