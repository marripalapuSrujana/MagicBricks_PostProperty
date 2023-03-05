import time
from hamcrest import *
from behave import *
# Importing the NavigationPage class from the pages folder
from features.pages.Navigation import NavigationPage
# Importing the PostPropertyPage class from the pages folder
from features.pages.PostPropertyPage import PostPropertyPage


#  first scenario

# Given step
@given('MagicBricks website should open')
def step_impl(context):
    # Expected title of the page
    expectedTitle = "Real Estate | Property in India | Buy/Sale/Rent Properties | MagicBricks"
    # Get the actual title of the page
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    # Check if the expected title matches the actual title
    assert_that(expectedTitle, equal_to(actualTitle))


# Step to click on POST PROPERTY button
@step('User clicks POST PROPERTY Button')
def step_impl(context):
    # Create an instance of the PostPropertyPage class
    propertyPage = NavigationPage(context.driver)
    # Call the click_post_property_button() method to click the button
    propertyPage.click_post_property_button()


# Step to check if user is redirected to Post Property page
@then('User is redirected to the Post Property page')
def step_impl(context):
    # Expected title of the page
    expectedTitle = "Post Free Property Ads | Rent & Sell Property Online"
    # Get the actual title of the page
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    # Check if the expected title matches the actual title
    assert_that(expectedTitle, equal_to(actualTitle))
    print("***************************************************")


#  second scenario

# When step to check if user is redirected to Post Property page
@when('User is redirected to the Post Property page')
def step_impl(context):
    # Expected title of the page
    expectedTitle = "Post Free Property Ads | Rent & Sell Property Online"
    # Get the actual title of the page
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    # Check if the expected title matches the actual title
    assert_that(expectedTitle, equal_to(actualTitle))


# Step to click on Owner button
@step("User clicks Owner button")
def step_impl(context):
    # Create an instance of the PostPropertyPage class
    ownerButton = PostPropertyPage(context.driver)
    # Call the click_owner_button() method to click the button
    ownerButton.click_owner_button()


# Step to click on Sell button
@step("User clicks Sell button")
def step_impl(context):
    # Create an instance of the PostPropertyPage class
    sellButton = PostPropertyPage(context.driver)
    # Call the sell_button() method to click the button
    sellButton.sell_button()


# Step to enter valid mobile number
@step('User enters valid mobile number')
def step_impl(context):
    # Create an instance of the PostPropertyPage class
    number = PostPropertyPage(context.driver)
    # Call the enter_num() method to enter the number
    number.enter_num()


# Step to click on Start now button
@then("User clicks Start now button")
def step_impl(context):
    # Create an instance of the PostPropertyPage class
    start = PostPropertyPage(context.driver)
    # Call the click_start_now_button() method to click the button
    start.click_start_now_button()


# Step definition to verify if user is redirected to the Sell and Rent your property page
@step("User is redirected to Sell and Rent your property")
def step_impl(context):
    # Expected title of the page
    expectedTitle = "Sell and Rent Your Property For Free on Magicbricks"
    # Get the actual title of the page
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    # Check if the expected title matches the actual title
    assert_that(expectedTitle, equal_to(actualTitle))
    time.sleep(2)
    print("***************************************************")


# Third Scenario
# Step to click on Builder button
@step("User clicks Builder button")
def step_impl(context):
    # Create an instance of the PostPropertyPage class
    builderButton = PostPropertyPage(context.driver)
    # Call the click_builder_button() method to click the button
    builderButton.click_builder_button()

# Step to click on List as PG button
@step("User clicks List as PG button")
def step_impl(context):
    # Create an instance of the PostPropertyPage class
    pg = PostPropertyPage(context.driver)
    # Call the click_PG_button() method to click the button
    pg.click_PG_button()

# Step definition to verify if user is redirected to Paying Guest page
@step("User is redirected to Paying Guest page")
def step_impl(context):
    time.sleep(5)
    expectedTitle = "Paying Guest in Bangalore | Real Estate in Bangalore | MagicBricks"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
    time.sleep(3)
    print("***************************************************")




# Fourth scenario
# Step definition to verify if User enters invalid {number}
@step('User enters invalid {number}')
def step_impl(context, number):
    # Create an instance of the PostPropertyPage class
    numbers = PostPropertyPage(context.driver)
    # Call the enter_number() method to click the button
    numbers.enter_number(number)

# Step definition to verify Website Displays error
@step("Website Displays error")
def step_impl(context):
    # Create an instance of the PostPropertyPage class
    context.Visibility = PostPropertyPage(context.driver)
    # Expected error
    expectedError = "Mobile number should be of 10 digits. Please re-enter."
    # Actual error
    actualError = context.Visibility.error_msg()
    # Prints actual error
    print("Error is " + actualError)
    # Check if the expected error matches the actual error
    assert_that(expectedError, equal_to(actualError))
    time.sleep(3)
