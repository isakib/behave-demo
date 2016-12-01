import time
from behave import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@given('I open Gmail registration page')
def step_impl(context):
   context.browser.get("https://accounts.google.com/SignUp?")


@then('I found the title of Create your Google Account')
def step_impl(context):
   title = context.browser.title
   assert "Create your Google Account" in title


@step("I fill the Gamil Registration form")
def step_impl(context):
    context.browser.find_element_by_name("FirstName").send_keys("Sakib Al")
    context.browser.find_element_by_name("LastName").send_keys("Mahmud")
    context.browser.find_element_by_name("GmailAddress").send_keys("sakibalmahmud007@gmailcom")
    context.browser.find_element_by_name("Passwd").send_keys("eyrwurewiuwri#$&$%&%$*@")
    context.browser.find_element_by_name("PasswdAgain").send_keys("eyrwurewiuwri#$&$%&%$*@")
    context.browser.find_element_by_name("BirthDay").send_keys("12")
    context.browser.find_element_by_name("BirthYear").send_keys("2016")
    context.browser.find_element_by_name("RecoveryEmailAddress").send_keys("aluddudu@gmail.com")
    # context.browser.find_element_by_id('sex-1').click()
    # context.browser.find_element_by_id('BirthMonth').send_keys("May")
    # continents_select = Select(context.browser.find_element_by_id('BirthMonth'))
    # continents_select.options[0].click()
    # context.browser.find_element_by_id('sex-1').click()
    # context.browser.find_element_by_id('BirthMonth').send_keys("May")
    # context.browser.find_element_by_id('tea2').click()
    # context.browser.find_element_by_id('tool-1').click()
    #     continents_select = Select(context.browser.find_element_by_id('BirthMonth'))
    #     continents_select.options[0].click()
    # another_select_list = Select(context.browser.find_element_by_id('selenium_commands'))
    # another_select_list.options[0].click()

@then("I select dropdown items from the-internet.herokuapp.com/dropdown")
def step_impl(context):
    context.browser.get("http://the-internet.herokuapp.com/dropdown")
    month_select = Select(context.browser.find_element_by_id('dropdown'))
    month_select.options[2].click()
    time.sleep(5)
    # find_element_by_css_selector("select#numReturnSelect > option[value='15000']").click()


@then("I select checkbox items from the-internet.herokuapp.com/checkboxes")
def step_impl(context):
    context.browser.get("http://the-internet.herokuapp.com/checkboxes")
    time.sleep(15)
    select_items_checkbox = context.browser.find_elements_by_xpath(".//*[@id='checkboxes']/input[1]")
    select_items_checkbox[0].click()
    time.sleep(15)

@step("I select checkbox items from seleniumframework.com/Practiceform")
def step_impl(context):
    context.browser.get("http://www.seleniumframework.com/Practiceform")
    select_radio_button = context.browser.find_element_by_id('vfb-7-2')
    select_radio_button.click()
    time.sleep(15)

@step("I select Date from calender at seleniumframework.com/Practiceform")
def step_impl(context):
    context.browser.get("http://www.seleniumframework.com/Practiceform")
    datepicker_from = context.browser.find_element_by_xpath(".//*[@id='vfb-8']")
    datepicker_from.click()
    wait = WebDriverWait(context.browser, 10)
    date_from = wait.until(EC.presence_of_element_located((By.XPATH, "//tbody/tr/td/a[text()='17']")))
    date_from.click()
    time.sleep(15)

@Then("I clicked on Submit button to continue")
def step_impl(context):
    context.browser.find_element_by_name("submitbutton").click()