from selenium import webdriver
from features.utility.config import ConfigClass

class UtilityClass:

    def __init__(self, driver):
        self.driver = driver

    def launch_browser(self):
        self.driver = webdriver.Chrome(ConfigClass.filePath)

    def maximize_window(self):
        self.driver.maximize_window()


    def launch_app(self):
        self.driver.get(ConfigClass.website_URL)

    def close_browser(self):
        self.driver.quit()