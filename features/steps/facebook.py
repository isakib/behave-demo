import time

@given('we visit mahara')
def step_impl(context):
    context.browser.get('http://demo.mahara.org/')

@when(u'a user visits the site')
def impl(context):
    context.browser.visit('/')

@when(u'Logging into the system as student')
def step_impl(context):
    username_field =('login_login_username')
    password_field = context.browser.find_element_by_id('login_login_password')
    username_field.send_keys('student')
    password_field.send_keys('MaharaDemo')
    submit_button = context.browser.find_element_by_id('login_submit')
    submit_button.click()
    time.sleep(10)

@when(u'I log in as "sakibqa@gmail.com"')
def step_impl(context):
    username_field = context.browser.find_by_id('email')
    password_field = context.browser.find_by_id('pass')
    username_field.send_keys('sakibqa@gmail.com')
    password_field.send_keys('759759@')
    submit_button = context.browser.find_by_id('id="u_0_l"')
    submit_button.click()

@when(u'I log in as "unregisteredUser"')
def step_impl(context):
    username_field = context.browser.find_by_id('username')
    password_field = context.browser.find_by_id('password')
    username_field.send_keys('unregisteredUser')
    password_field.send_keys('1234')
    submit_button = context.browser.find_by_id('submit')
    submit_button.click()

@then(u'I should see the message {auth_message}')
def imple(context, auth_message):
    message = context.browser.find_by_id('auth-message')
    assert message.text == auth_message

@then(u'I should see a message {messages}')
def imple(context, messages):
    message = context.browser.find_by_id('messages')
    assert message.text == messages