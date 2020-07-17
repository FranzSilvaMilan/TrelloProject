from behave import *
from compare import expect

from core.pages.list_page import ListPage


@Step("I add to card in the list created with {card_name} name")
def step_impl(context, card_name):
    """
    :param card_name:
    :param context: Add list Board
    """
    list_page = ListPage()
    list_page.click_add_to_card_link()
    list_page.set_card_name(card_name)
    list_page.click_add_card_button()
    context.list_page = list_page


@Step("The card {card_name} should be created in the list")
def step_impl(context, card_name):
    """
    :param card_name:
    :param context: cards Created
    """
    list_page = ListPage()
    expect(list_page.get_text_card_name()).to_equal(card_name)
