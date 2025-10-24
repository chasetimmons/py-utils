#!/usr/bin/env python3

"""
Author: Chase Timmons
Date: 09/02/2025
Purpose: Salary calculator
"""

# ------------------------------------------------------------------
def hourly():
    """ convert hourly rate """

    hourly = float(input("Please enter an hourly rate: "))

    # convert hourly rate to annual salary
    annual = hourly * 40 * 52
    # convert hourly rate to semi-monthly rate
    semi = annual / 24
    
    display_results(hourly, semi, annual)

    return

# ------------------------------------------------------------------
def annual():
    """ convert annual salary """

    annual = float(input("Please enter an annual salary: "))

    # convert annual salary to hourly rate
    hourly = annual / 52 / 40
    # convert annual salary to semi-monthly rate
    semi = annual / 24
    
    display_results(hourly, semi, annual)

    return

# ------------------------------------------------------------------
def semimonthly():
    """ convert semi-monthly rate """

    semi = float(input("Please enter a semi-monthly rate: "))

    # convert annual salary to hourly rate
    annual = semi * 24
    # convert annual salary to semi-monthly rate
    hourly = annual / 52 / 40
    
    display_results(hourly, semi, annual)

    return

# ------------------------------------------------------------------
def display_results(hourly,semi,annual):
    """ Display calculated results """

    print("---------------------------------------")
    print(f"Hourly Rate : \t\t${hourly:.2f}")
    print(f"Semi-Monthly Rate: \t${semi:,.2f}")
    print(f"Annual Salary: \t\t${annual:,.2f}")
    print("---------------------------------------")

    return

# ------------------------------------------------------------------
def percentage_change():
    """ calculate percentage change """
    
    old_rate = float(input("Enter Old Rate: "))
    new_rate = float(input("Enter New Rate: "))

    try:
        percentage = ((new_rate - old_rate) / old_rate) * 100

        print("-----------------------------------")
        print(f"Old Rate : \t\t${old_rate:.2f}")
        print(f"New Rate: \t\t${new_rate:,.2f}")
        print(f"Percentage Change: \t{percentage:,.2f}%")
        print("-----------------------------------")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except Exception as e:
        print(f"Error: {e}")

    return

# ------------------------------------------------------------------
def one_payment():
    """ calculate one-time payment """
    pass

# ------------------------------------------------------------------
def display_menu():
    """ display menu options """

    print()
    print("1 > Convert Hourly Rate")
    print("2 > Convert Annual Salary")
    print("3 > Convert Semi-Monthly Rate")
    print("4 > Calculate Percentage Change")
    print("5 > Calculate One-Time Payment")
    print("9 > Quit")
    print()

    option = input("Enter your selection: ")

    return option

# ------------------------------------------------------------------
def main():
    """ main """

    print("\nS A L A R Y   C A L C U L A T O R")

    while True:
        choice = display_menu()

        match choice:
            case "1":
                print("Option 1 Chosen\n")
                hourly()
            case "2":
                print("Option 2 Chosen\n")
                annual()
            case "3":
                print("Option 3 Chosen\n")
                semimonthly()
            case "4":
                print("Option 4 Chosen\n")
                percentage_change()
            case "5":
                print("Option 5 Chosen\n")
                one_payment()
            case "9":
                break
            case _:
                print("Please make a selection")

# ------------------------------------------------------------------
if __name__ == '__main__':
    main()
