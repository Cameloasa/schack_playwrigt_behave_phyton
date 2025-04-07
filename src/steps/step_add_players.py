from behave import when, then

@when(u'spelaren klickar på knappen "Lägg till spelare"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When spelaren klickar på knappen "Lägg till spelare"')


@when(u'spelaren skriver "David" i textfältet')
def step_impl(context):
    raise NotImplementedError(u'STEP: When spelaren skriver "David" i textfältet')


@then(u'"David" dyker upp på sidan med texten "0:00.0"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then "David" dyker upp på sidan med texten "0:00.0"')


@when(u'spelaren skriver "Gerson" i textfältet')
def step_impl(context):
    raise NotImplementedError(u'STEP: When spelaren skriver "Gerson" i textfältet')


@then(u'"Gerson" dyker upp på sidan med texten "0:00.0"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then "Gerson" dyker upp på sidan med texten "0:00.0"')