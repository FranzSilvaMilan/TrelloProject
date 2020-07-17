from behave import *
from compare import expect

from core.pages.team_page import TeamPage
from core.pages.welcome_page import WelcomePage


@Step("I create a team with {team_name} name")
def step_impl(context, team_name):
    """
    :param team_name:
    :param context: Create Team
    """
    welcome_page = WelcomePage()
    welcome_page.click_create_team()
    team_page = TeamPage()
    team_page.set_team_name(team_name)
    team_page.select_type_team()
    team_page.click_continue_button()
    context.team_page = team_page
