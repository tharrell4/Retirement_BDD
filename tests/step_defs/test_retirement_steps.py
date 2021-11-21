from pytest_bdd import scenarios, scenario, given, when, then, parsers, parser
from pytest import raises
import retirement

scenarios('../features/retirement.feature')


CONVERTERS = {
    'year': int,
    'month': int,
    'output': str,
}


@given("the program is running")
def program_running():
    # pytest will run the program automatically - manual step for a user/story
    pass


@then("program will loop until error resolved")
def invalid_inputs():
    # how do you test program exiting?
    # maybe look at console output???
    pass


@when(parsers.parse('"<year>" is entered for year'))
def year_set(year):
    pass


@when(parsers.parse('"<month>" is entered for month'))
def month_validate(month):
    pass


@then(parsers.parse('"<output>" is calculated from "<year>" and "<month>"'))
def valid_calc(output, month, year):
    assert str(retirement.calculate_nra(year, month)) == str(output)
