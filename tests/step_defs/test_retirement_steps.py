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
def looping_test():
    # validated by the loops in validate year/month
    pass


@when(parsers.parse('"<year>" is entered for year'))
@when('"<year>" is entered for year')
def year_test(year):
    with raises(OSError):
        retirement.validate_year(year)


@when(parsers.parse('"<month>" is entered for month'))
@when('"<month>" is entered for month')
def month_test(month):
    with raises(OSError):
        retirement.validate_month(month)


@then(parsers.parse('"<output>" is calculated from "<year>" and "<month>"'))
@then('"<output>" is calculated from "<month>" and "<year>"')
def valid_calc(output, month, year):
    assert str(retirement.calculate_nra(year, month)) == str(output)


@when('"1899" is entered for year')
def year_test():
    with raises(OSError):
        retirement.validate_year(1899)


@when('"2022" is entered for year')
def year_test():
    with raises(OSError):
        retirement.validate_year(2022)
