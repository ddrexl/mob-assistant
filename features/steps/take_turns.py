from behave import given, when, then


@given('driver starts turn')
def step_impl(context):
    pass


@when('turn ends')
def step_impl(context):
    pass


@then('a notification shows "{message}"')
def step_impl(context, message):
    if message not in context.response:
        fail('notification does not show %r' % (message,))
