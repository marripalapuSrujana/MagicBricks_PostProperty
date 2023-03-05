from selenium.webdriver.common.by import By


class PostPropertyPage:

    def __init__(self, driver):
        self.driver = driver

    # Second scenario

    def click_owner_button(self):
        owner = self.driver.find_element(By.XPATH, "(//*[@class='pp-form__elem-radio__label'])[1]")
        owner.click()

    def sell_button(self):
        sell = self.driver.find_element(By.XPATH, "(//*[@class='pp-form__elem-radio__label'])[4]")
        sell.click()

    def enter_num(self, ):
        phoneNumber = self.driver.find_element(By.XPATH, "//input[@placeholder = 'WhatsApp Number']")
        phoneNumber.send_keys(8317501584)

    def click_start_now_button(self):
        startButton = self.driver.find_element(By.XPATH, "//button[@onclick='submitPropertyForm();']")
        startButton.click()

    # Third scenario

    def click_builder_button(self):
        builder = self.driver.find_element(By.XPATH, "(//label[@class='pp-form__elem-radio__label'])[3]")
        builder.click()

    def click_PG_button(self):
        listAsPg = self.driver.find_element(By.XPATH, "(//label[@class='pp-form__elem-radio__label'])[6]")
        listAsPg.click()

    # Fourth scenario

    def enter_number(self, num):
        number = self.driver.find_element(By.XPATH, "//input[@placeholder = 'WhatsApp Number']")
        number.send_keys(num)

    def error_msg(self):
        error = self.driver.find_element(By.XPATH, "//div[@id='mobile__error']").text
        return error

    # DDF

    def click_agent_button(self):
        agent = self.driver.find_element(By.XPATH, "(//label[@class='pp-form__elem-radio__label'])[2]")
        agent.click()

    def click_rent_or_lease_button(self):
        rent = self.driver.find_element(By.XPATH, "(//label[@class='pp-form__elem-radio__label'])[5]")
        rent.click()
