from behave import *
from core.pages.welcome_page import WelcomePage
from core.pages.board_page import BoardPage
from core.pages.list_page import ListPage
from compare import expect


@Step("I create a board with name {board_name}")
def step_impl(context, board_name):
    """
    :param board_name:
    :param context: Add list Board
    """
    welcome_page = WelcomePage()
    welcome_page.click_create_board()
    welcome_page.set_board_name(board_name)
    welcome_page.click_create_board_button()


@Step("I add list with {list_name} name")
def step_impl(context, list_name):
    """
    :param list_name:
    :param context: Add list Board
    """
    board_page = BoardPage()
    board_page.set_list_name(list_name)
    board_page.click_add_list_button()
    context.board_page = board_page


@Step("I update the list created to {new_list_name}")
def step_impl(context, new_list_name):
    """
    :param new_list_name:
    :param context: update list name
    """
    list_page = ListPage()
    # list_page.update_list_name(new_list_name)


@Step("The Board {board_name} should be created")
def step_impl(context, board_name):
    """
    :param board_name: Validate Board
    :param context: Add list Board
    """
    board_page = BoardPage()
    expect(board_page.get_board_name()).to_equal(board_name)


@Step("The {list_name} list should be created in the board")
def step_impl(context, list_name):
    """
    :param list_name: Validate Board
    :param context: Add list Board
    """
    list_page = ListPage()
    expect("TestList").to_equal(list_name)


@Step("I get info of Team member")
def step_impl(context):
    """
    :param context: get info Team member
    """
    board_page = BoardPage()
    board_page.click_member_info()
    context.board_page = board_page


@Step("The name should be {member_name} with rol {rol}")
def step_impl(context, member_name, rol):
    """
    :param rol:
    :param member_name:
    :param context: Validate memeber info
    """
    board_page = context.board_page
    expect(board_page.get_member_name()).to_equal(member_name)
    expect(board_page.get_member_rol()).to_equal(rol)


@Step("I update the board created to {board_name}")
def step_impl(context, board_name):
    """
    :param board_name:
    :param context: UIpdate board name
    """
    board_page = BoardPage()
    # board_page.update_board_name(board_page)
