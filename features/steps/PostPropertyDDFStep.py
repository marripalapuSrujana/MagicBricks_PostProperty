import time
from behave import *
from features.utility.config import ConfigClass
from DataFiles import ExcelUtils

from features.pages.PostPropertyPage import PostPropertyPage


# Clicks the Agent button
@step("User clicks Agent button")
def step_impl(context):
    # Create an instance of the PostPropertyPage class
    agentButton = PostPropertyPage(context.driver)
    # Call the click_agent_button() method to click the button
    agentButton.click_agent_button()


# Clicks the Rent/Lease button
@step("User clicks Rent/Lease button")
def step_impl(context):
    # Create an instance of the PostPropertyPage class
    rentButton = PostPropertyPage(context.driver)
    # Call the click_rent_or_lease_button() method to click the button
    rentButton.click_rent_or_lease_button()


# Enters first valid mobile number from Excel sheet
@step("User enter {mobilenumber} with first valid data")
def step_impl(context, mobilenumber):
    # Read the data from the Excel sheet
    ExcelUtils.get_row_count(ConfigClass.excel_path, "Sheet1")
    mobileNumber = ExcelUtils.read_data(ConfigClass.excel_path, "Sheet1", 2, 1)
    time.sleep(2)
    # Enter the mobile number on the Post Property page
    number = PostPropertyPage(context.driver)
    number.enter_number(mobileNumber)
    print("***************************************************")


# Enters second valid mobile number from Excel sheet
@step("User enter {mobilenumber} with second valid data")
def step_impl(context, mobilenumber):
    # Read the data from the Excel sheet
    ExcelUtils.get_row_count(ConfigClass.excel_path, "Sheet1")
    mobileNum = ExcelUtils.read_data(ConfigClass.excel_path, "Sheet1", 3, 1)
    time.sleep(2)
    # Enter the mobile number on the Post Property page
    number = PostPropertyPage(context.driver)
    number.enter_number(mobileNum)