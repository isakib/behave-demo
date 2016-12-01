from behave import *
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.common.exceptions import WebDriverException
import unittest
import time

import traceback

use_step_matcher("re")

@when("I open seleniumframework website")
def step_impl(context):
    context.browser.get("http://www.seleniumframework.com/PracticeForm")

@step("I set implicit timeout")
def step_impl(context):
    context.browser.implicitly_wait(10) # seconds

@then("I print the text for periodic element")
def step_impl(context):
    target_element = context.browser.find_element_by_id("periodicElement")
    print("Periodic Element text:"+target_element.text)
    # print("Periodic Element text:"+target_element.get_attribute("innerHTML"))

@step("I set script timeout")
def step_impl(context):
    context.browser.set_script_timeout(30) # seconds
    #http://selenium.googlecode.com/git/docs/api/py/webdriver_remote/selenium.webdriver.remote.webdriver.html?
    #highlight=timeout#selenium.webdriver.remote.webdriver.WebDriver.set_script_timeout

@then("I wait for presence of element using id")
def step_impl(context):

    try:
        periodic_element = WebDriverWait(context.browser, 5).until(
            EC.presence_of_element_located((By.ID, "periodicElement"))
        )
    except(TimeoutException,StaleElementReferenceException):
        traceback.print_exc()
        #This line will print the latest exception stack trace in python

@then("I wait for text to be present in element")
def step_impl(context):
    # Increase and decrease the timeout around 3 seconds and observe the behavior.
    # https://code.google.com/p/selenium/source/browse/py/test/selenium/webdriver/common/webdriverwait_tests.py?r=5cc5085692c6784aefd3f63da85f0c0cb629714a
    try:
        WebDriverWait(context.browser, 5).until(EC.text_to_be_present_in_element((By.ID, 'periodicElement'), 'Element0'))
    except(Exception):
        traceback.print_exc()

@then("I wait for value attribute in element")
def step_impl(context):
    try:
        WebDriverWait(context.browser, 5).until(EC.text_to_be_present_in_element_value((By.ID, 'tea1'), 'Black Tea'))
    except(Exception):
        traceback.print_exc()

@then("I wait for alert")
def step_impl(context):
    context.browser.find_element_by_id("timingAlert").click()
    try:
        WebDriverWait(context.browser, 7).until(EC.alert_is_present())
    except(TimeoutException):
        traceback.print_exc()
    alert = context.browser.switch_to_alert()
    print(alert.text)
    assert 'Please share this website with your friends and in your organization.' in alert.text

@then("I check for staleness of element")
def step_impl(context):
    new_browser_window = context.browser.find_element_by_id("button1")
    print("Before refresh"+new_browser_window.text)
    context.browser.refresh()
    try:
        WebDriverWait(context.browser, 3).until(EC.staleness_of(new_browser_window))
        print("After refresh if we reached here means new browser window WebElement is stale now")
    except(TimeoutException):
        print("After refresh if we reached here means timeout exception occured, thet means element is NOT stale")
        # traceback.print_exc()
    finally:
        print("Continue execution in the finally block")

@then("I use lambda for selenium race conditions")
def step_impl(context):
    # http://chimera.labs.oreilly.com/books/1234000000754/ch20.html#_a_common_selenium_problem_race_conditions

    # THE BELOW CODE IS NOT YET TESTED WELL
    def wait_for(self, function_with_assertion, timeout=30):
        start_time = time.time()
        while time.time() - start_time &lt; timeout:
            try:
                return function_with_assertion()
            except (AssertionError, WebDriverException):
                time.sleep(1)
        # one more try, which will raise any errors if they are outstanding
        return function_with_assertion()

    def my_function(expected,actual):
        if(expected == actual):
            return True
        else:
            raise AssertionError

    span_clock = context.browser.find_element_by_id('clock')
    wait = ui.WebDriverWait(context.browser,50) #timeout after 10 seconds
    wait_for(lambda: my_function(span_clock.text, "Buzz  Buzz"))