from behave import given

from core.trello.login_page import *


@given("I login with user {user} and password {password} in the Trello page")
def step_impl(context, user, password):
    """
    :param context: login
    :param user: user
    :param password: password
    """
    login_page = LoginPage()
    login_page.set_user(user)
    login_page.set_password(password)
    login_page.click_login()
