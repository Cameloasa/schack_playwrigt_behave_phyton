from behave import given, when, then
from pages.start_page import StartPage

@given('I am on the chess game start page')
def step_given_start_page(context):
    print("În step_given_start_page")
    context.page.goto(context.base_url)
    context.start_page = StartPage(context.page)

@when('I click the "Lägg till spelare" button')
def step_when_click_add_player(context):
    context.start_page.click_add_player_button()

@when('I enter "{player_name}" as a new player\'s name')
def step_when_enter_player_name(context, player_name):
    context.start_page.fill_player_name(player_name)
    context.start_page.click_add_player_button()

@then('the timer for "{player_name}" should be visible')
def step_then_timer_visible(context, player_name):
    assert context.start_page.player_timer_visible(player_name), f"Timer for '{player_name}' is not visible"

@given('I have added "Alice" and "Bob" as players')
def step_given_two_players(context):
    context.page.goto(context.base_url)
    context.start_page = StartPage(context.page)
    context.start_page.click_add_player_button()
    context.start_page.fill_player_name("Alice")
    context.start_page.click_add_player_button()
    context.start_page.click_add_player_button()
    context.start_page.fill_player_name("Bob")
    context.start_page.click_add_player_button()

@when('the game starts')
def step_when_game_starts(context):
    pass

@then('I should see timers running for both "Alice" and "Bob"')
def step_then_timers_running(context):
    alice_timer = context.start_page.player_timer_visible("Alice")
    bob_timer = context.start_page.player_timer_visible("Bob")
    assert alice_timer, "Timer for Alice should be visible"
    assert bob_timer, "Timer for Bob should be visible"

