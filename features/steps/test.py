from behave import given, when, then, Step


@given(u'I am logged In')
def step_impl(context):
    print("Given Condition")


@when(u'Logged In')
def step_impl(context):
    print("When Condition")


@then(u'Success')
def step_impl(context):
    print("Then Condition")

@then(u'Failureexample')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Failure Example')

