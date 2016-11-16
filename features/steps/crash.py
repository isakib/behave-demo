from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Firefox()

def after_all(context):
    context.browser.quit()

@when('we visit https://crash-stats.mozilla.com/')
def step(context):
   context.browser.get("https://crash-stats.mozilla.com/")

@then('it should have a title "Crash Data for Firefox"')
def step(context):
    assert context.browser.title == "Crash Data for Firefox"