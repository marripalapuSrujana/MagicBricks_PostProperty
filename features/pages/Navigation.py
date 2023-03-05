from selenium.webdriver.common.by import By


class NavigationPage:

    def __init__(self, driver):
        self.driver = driver
    # first scenario
    def click_post_property_button(self):

        button = self.driver.find_element(By.XPATH, "(//a[@href = 'https://post.magicbricks.com'])[2]")
        self.driver.execute_script("arguments[0].click();", button)
        print("Parent window title: " + self.driver.title)
        # get current window handle
        p = self.driver.current_window_handle
        # get first child window
        chwd = self.driver.window_handles
        for w in chwd:
            # switch focus to child window
            if (w != p):
                self.driver.switch_to.window(w)