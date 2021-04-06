from behave import given, when, then
from behave import __main__ as runner_with_options

#if __name__ =='__main__':



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

