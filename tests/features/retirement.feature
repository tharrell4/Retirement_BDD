# Created by Tiffany at 11/15/2021
Feature: Retirement Age Calculation
  As a US Citizen,
  I want to know when I can retire,
  So that I maximize my benefits from Social Security

  Scenario Outline: Calculation with correct inputs and boundaries
    Given the program is running
    When "<year>" is entered for year
    When "<month>" is entered for month
    Then "<output>" is calculated from "<month>" and "<year>"

    Examples:
      | year | month | output |
      | 2000 | 10    | ('67 and 0 months', 'October of 2067') |
      | 1938 | 1     | ('65 and 2 months', 'March of 2003') |
      | 1938 | 11    | ('65 and 2 months', 'January of 2004') |
      | 1955 | 1     | ('66 and 2 months', 'March of 2021') |
      | 1955 | 11    | ('66 and 2 months', 'January of 2022') |
      | 1939 | 1     | ('65 and 4 months', 'May of 2004') |
      | 1939 | 11    | ('65 and 4 months', 'March of 2005') |
      | 1956 | 1     | ('66 and 4 months', 'May of 2022') |
      | 1956 | 11    | ('66 and 4 months', 'March of 2023') |
      | 1940 | 1     | ('65 and 6 months', 'July of 2005') |
      | 1940 | 11    | ('65 and 6 months', 'May of 2006') |
      | 1957 | 1     | ('66 and 6 months', 'July of 2023') |
      | 1957 | 11    | ('66 and 6 months', 'May of 2024')|
      | 1941 | 1     | ('65 and 8 months', 'September of 2006') |
      | 1941 | 11    | ('65 and 8 months', 'July of 2007') |
      | 1958 | 1     | ('66 and 8 months', 'September of 2024') |
      | 1958 | 11    | ('66 and 8 months', 'July of 2025') |
      | 1942 | 1     | ('66 and 10 months', 'November of 2007') |
      | 1942 | 11    | ('66 and 10 months', 'September of 2008') |
      | 1959 | 1     | ('66 and 10 months', 'November of 2025') |
      | 1959 | 11    | ('66 and 10 months', 'September of 2026') |
      | 1960 | 1     | ('67 and 0 months', 'January of 2027') |

  Scenario: Incorrect date before 1900 entered
    Given the program is running
    When "1899" is entered for year
    Then program will loop until error resolved

  Scenario: Incorrect date of 2022 entered
    Given the program is running
    When "2022" is entered for year
    Then program will loop until error resolved

  Scenario: Incorrect date of Month "13" entered
    Given the program is running
    When "2000" is entered for year
    When "13" is entered for month
    Then program will loop until error resolved
