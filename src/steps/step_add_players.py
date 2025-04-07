from behave import given, when, then
from src.pages.start_page import StartPage


@given(u'I am on the chess game start page')
def step_given_start_page(context):
    context.start_page = StartPage
    context.start_page.navigate_to(context.base_url)



@when(u'I enter "Alice" as a new player\'s name')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter "Alice" as a new player\'s name')


@when(u'I click the "Lägg till spelare" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the "Lägg till spelare" button')


@then(u'I should see "Alice" in the list of players')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see "Alice" in the list of players')


@then(u'the timer for "Alice" should be visible')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the timer for "Alice" should be visible')


@when(u'I enter "Bob" as a new player\'s name')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter "Bob" as a new player\'s name')


@then(u'I should see "Bob" in the list of players')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see "Bob" in the list of players')


@then(u'the timer for "Bob" should be visible')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the timer for "Bob" should be visible')


@given(u'I have added "Alice" and "Bob" as players')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have added "Alice" and "Bob" as players')


@when(u'the game starts')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the game starts')


@then(u'I should see timers running for both "Alice" and "Bob"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see timers running for both "Alice" and "Bob"')


@then(u'I should see a pause button')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see a pause button')
