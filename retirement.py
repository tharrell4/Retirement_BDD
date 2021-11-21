months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
          9: 'September', 10: 'October', 11: 'November', 12: 'December'}


def main():
    cycle = True
    print("Social Security Full Retirement Age Calculator")
    while cycle:  # cycle controls repetition so that the program will run for as long as the user wants
        year = input("\nType the year of birth and press enter, or leave blank to exit: ")
        if year == "":
            cycle = False
            continue  # resets the loop to end program ASAP
        year = validate_year(year)
        month = input("\nType the month of birth and press enter: ")
        month = validate_month(month)
        print("\nCalculating...")
        age, date = calculate_nra(int(year), int(month))
        print(f'\nThe Full Retirement Age is {age}.\nThis will be in {date}.\n\n')


def validate_year(year):
    valid = False
    while not valid:  # loop control. repetition is prediction is power
        if not year.isnumeric():
            year = input("\nPlease enter only digits for year: ")
        elif int(year) < 1900 or int(year) > 2021:
            year = input("\nPlease enter only years between 1900 and 2021: ")
        else:
            valid = True
    return year  # will only return validated year


def validate_month(month):
    valid = False  # loop control
    while not valid:
        if not month.isnumeric() or month not in months.values():
            month = input("\nPlease enter only digits for month: ")
        elif int(month) < 1 or int(month) > 12 or month not in months.values():
            month = input("\nPlease enter only numbers 1-12: ")
        else:
            valid = True
    return month


def calculate_nra(year, month):
    if year <= 1942:  # cuts down on total if/elif/else statements, since 10 dates share five months and ALL dates share 3 years
        age = 65
    elif year <= 1959:
        age = 66
    else:
        age = 67
    if year in (1938, 1955):
        eMonth = 2
    elif year in (1939, 1956):
        eMonth = 4
    elif year in (1940, 1957):
        eMonth = 6
    elif year in (1941, 1958):
        eMonth = 8
    elif year in (1942, 1959):
        eMonth = 10
    else:
        eMonth = 0
    endAge = f'{age} and {eMonth} months'  # formatted for final printout
    if month + eMonth > 12:  # correction for months past December
        year += 1
        month = (month + eMonth) - 12
    else:
        month += eMonth
    year += age
    date = f'{months[month]} of {year}'  # formatted for final printout
    return endAge, date
