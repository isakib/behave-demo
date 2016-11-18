import time
# from PyQt4.uic import driver
from behave import given
from selenium.webdriver.common.by import By

@given("access facebook")
def step_impl(context):
    context.browser.get(context.base_url)
    time.sleep(10)

@given("visit singup of facebook")
def step_impl(context):
    context.browser.get(context.base_url + '/r.php')
    time.sleep(10)