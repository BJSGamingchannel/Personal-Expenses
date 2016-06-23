#########################
#|---------------------|#
#|   In/Outcome Calc   |#
#|=====================|#
#|Author: Beau Saunders|#
#|Version:          1.0|#
#|---------------------|#
#########################

def numOfIncome():

    numIncome = int(input("\nPlease enter the number of income you would like to enter (Up to 10 incomes)"))

    if numIncome == 1:

        _1I()

    elif numIncome == 2:

        _2I()

    elif numIncome == 3:

        _3I()

    elif numIncome == 4:

        _4I()

    elif numIncome == 5:

        _5I()

    elif numIncome == 6:

        _6I()

    elif numIncome == 7:

        _7I()

    elif numIncome == 8:

        _8I()

    elif numIncome == 9:

        _9I()

    elif numIncome == 10:

        _10I()

    else:

        print("Something went wrong, please try again.")

        numOfIncome()

def _1I():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")

    Income1 = float(input("\nIncome 1 = "))

    rounded = round(Income1, 2)

    totalIncome = str(rounded)

    print("\nYour total income is: £" + totalIncome)

def _2I():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")

    Income1 = float(input("\nIncome 1 = "))
    Income2 = float(input("\nIncome 2 = "))

    rounded = round(Income1 + Income2, 2)

    totalIncome = str(rounded)

    print("\nYour total income is: £" + totalIncome)


def _3I():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")

    Income1 = float(input("\nIncome 1 = "))
    Income2 = float(input("\nIncome 2 = "))
    Income3 = float(input("\nIncome 3 = "))

    rounded = round(Income1 + Income2 + Income3, 2)

    totalIncome = str(rounded)

    print("\nYour total income is: £" + totalIncome)


def _4I():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")

    Income1 = float(input("\nIncome 1 = "))
    Income2 = float(input("\nIncome 2 = "))
    Income3 = float(input("\nIncome 3 = "))
    Income4 = float(input("\nIncome 4 = "))

    rounded = round(Income1 + Income2 + Income3 + Income4, 2)

    totalIncome = str(rounded)

    print("\nYour total income is: £" + totalIncome)


def _5I():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")

    Income1 = float(input("\nIncome 1 = "))
    Income2 = float(input("\nIncome 2 = "))
    Income3 = float(input("\nIncome 3 = "))
    Income4 = float(input("\nIncome 4 = "))
    Income5 = float(input("\nIncome 5 = "))

    rounded = round(Income1 + Income2 + Income3 + Income4 + Income5, 2)

    totalIncome = str(rounded)

    print("\nYour total income is: £" + totalIncome)


def _6I():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")

    Income1 = float(input("\nIncome 1 = "))
    Income2 = float(input("\nIncome 2 = "))
    Income3 = float(input("\nIncome 3 = "))
    Income4 = float(input("\nIncome 4 = "))
    Income5 = float(input("\nIncome 5 = "))
    Income6 = float(input("\nIncome 6 = "))

    rounded = round(Income1 + Income2 + Income3 + Income4 + Income5 + Income6, 2)

    totalIncome = str(rounded)

    print("\nYour total income is: £" + totalIncome)


def _7I():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")

    Income1 = float(input("\nIncome 1 = "))
    Income2 = float(input("\nIncome 2 = "))
    Income3 = float(input("\nIncome 3 = "))
    Income4 = float(input("\nIncome 4 = "))
    Income5 = float(input("\nIncome 5 = "))
    Income6 = float(input("\nIncome 6 = "))
    Income7 = float(input("\nIncome 7 = "))

    rounded = round(Income1 + Income2 + Income3 + Income4 + Income5 + Income6 + Income7, 2)

    totalIncome = str(rounded)

    print("\nYour total income is: £" + totalIncome)


def _8I():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")

    Income1 = float(input("\nIncome 1 = "))
    Income2 = float(input("\nIncome 2 = "))
    Income3 = float(input("\nIncome 3 = "))
    Income4 = float(input("\nIncome 4 = "))
    Income5 = float(input("\nIncome 5 = "))
    Income6 = float(input("\nIncome 6 = "))
    Income7 = float(input("\nIncome 7 = "))
    Income8 = float(input("\nIncome 8 = "))

    rounded = round(Income1 + Income2 + Income3 + Income4 + Income5 + Income6 + Income7 + Income8, 2)

    totalIncome = str(rounded)

    print("\nYour total income is: £" + totalIncome)


def _9I():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")

    Income1 = float(input("\nIncome 1 = "))
    Income2 = float(input("\nIncome 2 = "))
    Income3 = float(input("\nIncome 3 = "))
    Income4 = float(input("\nIncome 4 = "))
    Income5 = float(input("\nIncome 5 = "))
    Income6 = float(input("\nIncome 6 = "))
    Income7 = float(input("\nIncome 7 = "))
    Income8 = float(input("\nIncome 8 = "))
    Income9 = float(input("\nIncome 9 = "))

    rounded = round(Income1 + Income2 + Income3 + Income4 + Income5 + Income6 + Income7 + Income8 + Income9, 2)

    totalIncome = str(rounded)

    print("\nYour total income is: £" + totalIncome)


def _10I():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")

    Income1 = float(input("\nIncome 1 = "))
    Income2 = float(input("\nIncome 2 = "))
    Income3 = float(input("\nIncome 3 = "))
    Income4 = float(input("\nIncome 4 = "))
    Income5 = float(input("\nIncome 5 = "))
    Income6 = float(input("\nIncome 6 = "))
    Income7 = float(input("\nIncome 7 = "))
    Income8 = float(input("\nIncome 8 = "))
    Income9 = float(input("\nIncome 9 = "))
    Income10 = float(input("\nIncome 10 = "))

    rounded = round(Income1 + Income2 + Income3 + Income4 + Income5 + Income6 + Income7 + Income8 + Income9 + Income10, 2)

    totalIncome = str(rounded)

    print("\nYour total income is: £" + totalIncome)

def numOfOutcome():

    numOutcome = int(input("\nPlease enter the number of outcome you would like to enter (Up to 10 outcomes) "))

    if numOutcome == 1:

        _1O()

    elif numOutcome == 2:

        _2O()

    elif numOutcome == 3:

        _3O()

    elif numOutcome == 4:

        _4O()

    elif numOutcome == 5:

        _5O()

    elif numOutcome == 6:

        _6O()

    elif numOutcome == 7:

        _7O()

    elif numOutcome == 8:

        _8O()

    elif numOutcome == 9:

        _9O()

    elif numOutcome == 10:

        _10O()

    else:

        print("Something went wrong, please try again.\n")

        numOfOutcome()

def _1O():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")
    
    Outcome1 = float(input("\nOutcome 1 = "))

    rounded = round(Outcome1, 2)

    totalOutcome = str(rounded)

    print("\nYour total income is: £" + totalOutcome)

def _2O():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")

    Outcome1 = float(input("\nOutcome 1 = "))
    Outcome2 = float(input("\nOutcome 2 = "))

    rounded = round(Outcome1 + Outcome2, 2)

    totalOutcome = str(rounded)

    print("\nYour total income is: £" + totalOutcome)

def _3O():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")

    Outcome1 = float(input("\nOutcome 1 = "))
    Outcome2 = float(input("\nOutcome 2 = "))
    Outcome3 = float(input("\nOutcome 3 = "))

    rounded = round(Outcome1 + Outcome2 + Outcome3, 2)

    totalOutcome = str(rounded)

    print("\nYour total income is: £" + totalOutcome)

def _4O():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")

    Outcome1 = float(input("\nOutcome 1 = "))
    Outcome2 = float(input("\nOutcome 2 = "))
    Outcome3 = float(input("\nOutcome 3 = "))
    Outcome4 = float(input("\nOutcome 4 = "))

    rounded = round(Outcome1 + Outcome2 + Outcome3 + Outcome4, 2)

    totalOutcome = str(rounded)

    print("\nYour total income is: £" + totalOutcome)

def _5O():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")

    Outcome1 = float(input("\nOutcome 1 = "))
    Outcome2 = float(input("\nOutcome 2 = "))
    Outcome3 = float(input("\nOutcome 3 = "))
    Outcome4 = float(input("\nOutcome 4 = "))
    Outcome5 = float(input("\nOutcome 5 = "))

    rounded = round(Outcome1 + Outcome2 + Outcome3 + Outcome4 + Outcome5, 2)

    totalOutcome = str(rounded)

    print("\nYour total income is: £" + totalOutcome)

def _6O():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")

    Outcome1 = float(input("\nOutcome 1 = "))
    Outcome2 = float(input("\nOutcome 2 = "))
    Outcome3 = float(input("\nOutcome 3 = "))
    Outcome4 = float(input("\nOutcome 4 = "))
    Outcome5 = float(input("\nOutcome 5 = "))
    Outcome6 = float(input("\nOutcome 6 = "))

    rounded = round(Outcome1 + Outcome2 + Outcome3 + Outcome4 + Outcome5 + Outcome6, 2)

    totalOutcome = str(rounded)

    print("\nYour total income is: £" + totalOutcome)

def _7O():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")

    Outcome1 = float(input("\nOutcome 1 = "))
    Outcome2 = float(input("\nOutcome 2 = "))
    Outcome3 = float(input("\nOutcome 3 = "))
    Outcome4 = float(input("\nOutcome 4 = "))
    Outcome5 = float(input("\nOutcome 5 = "))
    Outcome6 = float(input("\nOutcome 6 = "))
    Outcome7 = float(input("\nOutcome 7 = "))

    rounded = round(Outcome1 + Outcome2 + Outcome3 + Outcome4 + Outcome5 + Outcome6 + Outcome7, 2)

    totalOutcome = str(rounded)

    print("\nYour total income is: £" + totalOutcome)

def _8O():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")

    Outcome1 = float(input("\nOutcome 1 = "))
    Outcome2 = float(input("\nOutcome 2 = "))
    Outcome3 = float(input("\nOutcome 3 = "))
    Outcome4 = float(input("\nOutcome 4 = "))
    Outcome5 = float(input("\nOutcome 5 = "))
    Outcome6 = float(input("\nOutcome 6 = "))
    Outcome7 = float(input("\nOutcome 7 = "))
    Outcome8 = float(input("\nOutcome 8 = "))

    rounded = round(Outcome1 + Outcome2 + Outcome3 + Outcome4 + Outcome5 + Outcome6 + Outcome7 + Outcome8, 2)

    totalOutcome = str(rounded)

    print("\nYour total income is: £" + totalOutcome)

def _9O():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")

    Outcome1 = float(input("\nOutcome 1 = "))
    Outcome2 = float(input("\nOutcome 2 = "))
    Outcome3 = float(input("\nOutcome 3 = "))
    Outcome4 = float(input("\nOutcome 4 = "))
    Outcome5 = float(input("\nOutcome 5 = "))
    Outcome6 = float(input("\nOutcome 6 = "))
    Outcome7 = float(input("\nOutcome 7 = "))
    Outcome8 = float(input("\nOutcome 8 = "))
    Outcome9 = float(input("\nOutcome 9 = "))

    rounded = round(Outcome1 + Outcome2 + Outcome3 + Outcome4 + Outcome5 + Outcome6 + Outcome7 + Outcome8 + Outcome9, 2)

    totalOutcome = str(rounded)

    print("\nYour total income is: £" + totalOutcome)

def _10O():

    print("\nPlease do not type any symbols (e.g. £,$ etc)")

    Outcome1 = float(input("\nOutcome 1 = "))
    Outcome2 = float(input("\nOutcome 2 = "))
    Outcome3 = float(input("\nOutcome 3 = "))
    Outcome4 = float(input("\nOutcome 4 = "))
    Outcome5 = float(input("\nOutcome 5 = "))
    Outcome6 = float(input("\nOutcome 6 = "))
    Outcome7 = float(input("\nOutcome 7 = "))
    Outcome8 = float(input("\nOutcome 8 = "))
    Outcome9 = float(input("\nOutcome 9 = "))
    Outcome10 = float(input("\nOutcome 10 = "))

    rounded = round(Outcome1 + Outcome2 + Outcome3 + Outcome4 + Outcome5 + Outcome6 + Outcome7 + Outcome8 + Outcome9 + Outcome10, 2)

    totalOutcome = str(rounded)

    print("\nYour total income is: £" + totalOutcome)

def menu():

    print("\nWelcome to the Personal Expenses Calculator\n")

    in_outcome = input("Type I to use the income calculator or O to use the outcome calculator ").upper()

    if in_outcome == "I":

        numOfIncome()

    elif in_outcome == "O":

        numOfOutcome()

    else:

        print("Something went wrong, please try again\n")

        menu()
    
menu()
