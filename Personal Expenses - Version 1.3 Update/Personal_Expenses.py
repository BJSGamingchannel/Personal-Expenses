#########################
#|---------------------|#
#|  Personal Expenses  |#
#|=====================|#
#|Author: Beau Saunders|#
#|Version:          1.3|#
#|---------------------|#
#########################

_2016months = """
===== 2016 =====

1 = January 2016
2 = February 2016
3 = March 2016
4 = April 2016
5 = May 2016
6 = June 2016
7 = July 2016
8 = August 2016
9 = September 2016
10 = October 2016
11 = November 2016
12 = December 2016

===== 2017 =====

13 = January 2017
14 = February 2017
"""

def january2016():

    openFile = open("January2016.txt", "r")

    file = openFile.read()

    print(file)

def february2016():

    openFile = open("February2016.txt", "r")
    
    file = openFile.read()

    print(file)

def march2016():

    openFile = open("March2016.txt", "r")
    
    file = openFile.read()

    print(file)

def april2016():

    openFile = open("April2016.txt", "r")
    
    file = openFile.read()

    print(file)

def may2016():

    openFile = open("May2016.txt", "r")
    
    file = openFile.read()

    print(file)

def june2016():

    openFile = open("June2016.txt", "r")
    
    file = openFile.read()

    print(file)

def july2016():

    openFile = open("July2016.txt", "r")
    
    file = openFile.read()

    print(file)

def august2016():

    openFile = open("August2016.txt", "r")
    
    file = openFile.read()

    print(file)

def september2016():

    openFile = open("Spetember2016.txt", "r")
    
    file = openFile.read()

    print(file)

def october2016():

    openFile = open("October2016.txt", "r")
    
    file = openFile.read()

    print(file)

def november2016():

    openFile = open("Novmeber2016.txt", "r")
    
    file = openFile.read()

    print(file)

def december2016():

    openFile = open("December2016.txt", "r")
    
    file = openFile.read()

    print(file)

def january2017():

    openFile = open("January2017.txt", "r")
    
    file = openFile.read()

    print(file)

def february2017():

    openFile = open("February2017.txt", "r")
    
    file = openFile.read()

    print(file)

#==================================================================================================================================================#

def january2016e():

    print("\nPlease only type numbers (e.g. No £,$ etc).\n")
    print("Please only enter a maximum of 2 decimal places (e.g 2.57).\n")

    income1 = float(input("\nIncome 1 = "))

    totalIncome = (income1)

    totalIncome1 = str(totalIncome)

    outcome1 = float(input("\nOutcome 1 = "))

    totalOutcome = (outcome1)

    totalOutcome1 = str(totalOutcome)

    totalProfit = str(totalIncome - totalOutcome)

    print("\nYour Total Profit this month is: £" + totalProfit)

    file = open("January2016.txt", "w")

    TextFile = (file.write("\nTotal Profit for this month was £" + totalProfit + "\nYou spent £" + totalOutcome1 + "\nAnd made £" + totalIncome1))
    
def february2016e():

    print("\nPlease only type numbers (e.g. No £,$ etc).\n")
    print("Please only enter a maximum of 2 decimal places (e.g 2.57).\n")

    income1 = float(input("\nIncome 1 = "))
    totalIncome = (income1)

    totalIncome1 = str(totalIncome)

    outcome1 = float(input("\nOutcome 1 = "))

    totalOutcome = (outcome1)

    totalOutcome1 = str(totalOutcome)

    totalProfit = str(totalIncome - totalOutcome)

    print("\nYour Total Profit this month is: £" + totalProfit)

    file = open("February2016.txt", "w")

    TextFile = (file.write("\nTotal Profit for this month was £" + totalProfit + "\nYou spent £" + totalOutcome1 + "\nAnd made £" + totalIncome1))

def march2016e():

    print("\nPlease only type numbers (e.g. No £,$ etc).\n")
    print("Please only enter a maximum of 2 decimal places (e.g 2.57).\n")

    income1 = float(input("\nIncome 1 = "))
    
    totalIncome = (income1)

    totalIncome1 = str(totalIncome)

    outcome1 = float(input("\nOutcome 1 = "))

    totalOutcome = (outcome1)

    totalOutcome1 = str(totalOutcome)
    
    totalProfit = str(totalIncome - totalOutcome)

    print("\nYour Total Profit this month is: £" + totalProfit)

    file = open("March2016.txt", "w")

    TextFile = (file.write("\nTotal Profit for this month was £" + totalProfit + "\nYou spent £" + totalOutcome1 + "\nAnd made £" + totalIncome1))

def april2016e():

    print("\nPlease only type numbers (e.g. No £,$ etc).\n")
    print("Please only enter a maximum of 2 decimal places (e.g 2.57).\n")

    income1 = float(input("\nIncome 1 = "))
    totalIncome = (income1)

    totalIncome1 = str(totalIncome)

    outcome1 = float(input("\nOutcome 1 = "))

    totalOutcome = (outcome1)

    totalOutcome1 = str(totalOutcome)

    totalProfit = str(totalIncome - totalOutcome)

    print("\nYour Total Profit this month is: £" + totalProfit)

    file = open("April2016.txt", "w")

    TextFile = (file.write("\nTotal Profit for this month was £" + totalProfit + "\nYou spent £" + totalOutcome1 + "\nAnd made £" + totalIncome1))

def may2016e():

    print("\nPlease only type numbers (e.g. No £,$ etc).\n")
    print("Please only enter a maximum of 2 decimal places (e.g 2.57).\n")

    income1 = float(input("\nIncome 1 = "))
    totalIncome = (income1)

    totalIncome1 = str(totalIncome)

    outcome1 = float(input("\nOutcome 1 = "))

    totalOutcome = (outcome1)

    totalOutcome1 = str(totalOutcome)

    totalProfit = str(totalIncome - totalOutcome)

    print("\nYour Total Profit this month is: £" + totalProfit)

    file = open("May2016.txt", "w")

    TextFile = (file.write("\nTotal Profit for this month was £" + totalProfit + "\nYou spent £" + totalOutcome1 + "\nAnd made £" + totalIncome1))

def june2016e():

    print("\nPlease only type numbers (e.g. No £,$ etc).\n")
    print("Please only enter a maximum of 2 decimal places (e.g 2.57).\n")

    income1 = float(input("\nIncome 1 = "))

    totalIncome = (income1)

    totalIncome1 = str(totalIncome)

    outcome1 = float(input("\nOutcome 1 = "))

    totalOutcome = (outcome1)

    totalOutcome1 = str(totalOutcome)

    totalProfit = str(totalIncome - totalOutcome)

    print("\nYour Total Profit this month is: £" + totalProfit)

    file = open("June2016.txt", "w")

    TextFile = (file.write("\nTotal Profit for this month was £" + totalProfit + "\nYou spent £" + totalOutcome1 + "\nAnd made £" + totalIncome1))

def july2016e():

    print("\nPlease only type numbers (e.g. No £,$ etc).\n")
    print("Please only enter a maximum of 2 decimal places (e.g 2.57).\n")

    income1 = float(input("\nIncome 1 = "))

    totalIncome = (income1)

    totalIncome1 = str(totalIncome)

    outcome1 = float(input("\nOutcome 1 = "))

    totalOutcome = (outcome1)

    totalOutcome1 = str(totalOutcome)

    totalProfit = str(totalIncome - totalOutcome)

    print("\nYour Total Profit this month is: £" + totalProfit)

    file = open("July2016.txt", "w")

    TextFile = (file.write("\nTotal Profit for this month was £" + totalProfit + "\nYou spent £" + totalOutcome1 + "\nAnd made £" + totalIncome1))

def august2016e():

    print("\nPlease only type numbers (e.g. No £,$ etc).\n")
    print("Please only enter a maximum of 2 decimal places (e.g 2.57).\n")

    income1 = float(input("\nIncome 1 = "))
 
    totalIncome = (income1)

    totalIncome1 = str(totalIncome)

    outcome1 = float(input("\nOutcome 1 = "))
    
    totalOutcome = (outcome1)

    totalOutcome1 = str(totalOutcome)

    totalProfit = str(totalIncome - totalOutcome)

    print("\nYour Total Profit this month is: £" + totalProfit)

    file = open("August2016.txt", "w")

    TextFile = (file.write("\nTotal Profit for this month was £" + totalProfit + "\nYou spent £" + totalOutcome1 + "\nAnd made £" + totalIncome1))

def september2016e():

    print("\nPlease only type numbers (e.g. No £,$ etc).\n")
    print("Please only enter a maximum of 2 decimal places (e.g 2.57).\n")

    income1 = float(input("\nIncome 1 = "))
    
    totalIncome = (income1)

    totalIncome1 = str(totalIncome)

    outcome1 = float(input("\nOutcome 1 = "))

    totalOutcome = (outcome1)

    totalOutcome1 = str(totalOutcome)

    totalProfit = str(totalIncome - totalOutcome)

    print("\nYour Total Profit this month is: £" + totalProfit)

    file = open("September2016.txt", "w")

    TextFile = (file.write("\nTotal Profit for this month was £" + totalProfit + "\nYou spent £" + totalOutcome1 + "\nAnd made £" + totalIncome1))

def october2016e():

    print("\nPlease only type numbers (e.g. No £,$ etc).\n")
    print("Please only enter a maximum of 2 decimal places (e.g 2.57).\n")

    income1 = float(input("\nIncome 1 = "))
 
    totalIncome = (income1)

    totalIncome1 = str(totalIncome)

    outcome1 = float(input("\nOutcome 1 = "))
  
    totalOutcome = (outcome1)

    totalOutcome1 = str(totalOutcome)

    totalProfit = str(totalIncome - totalOutcome)

    print("\nYour Total Profit this month is: £" + totalProfit)

    file = open("October2016.txt", "w")

    TextFile = (file.write("\nTotal Profit for this month was £" + totalProfit + "\nYou spent £" + totalOutcome1 + "\nAnd made £" + totalIncome1))

def november2016e():

    print("\nPlease only type numbers (e.g. No £,$ etc).\n")
    print("Please only enter a maximum of 2 decimal places (e.g 2.57).\n")

    income1 = float(input("\nIncome 1 = "))

    totalIncome = (income1)

    totalIncome1 = str(totalIncome)

    outcome1 = float(input("\nOutcome 1 = "))

    totalOutcome = (outcome1)

    totalOutcome1 = str(totalOutcome)

    totalProfit = str(totalIncome - totalOutcome)

    print("\nYour Total Profit this month is: £" + totalProfit)

    file = open("November2016.txt", "w")

    TextFile = (file.write("\nTotal Profit for this month was £" + totalProfit + "\nYou spent £" + totalOutcome1 + "\nAnd made £" + totalIncome1))

def december2016e():

    print("\nPlease only type numbers (e.g. No £,$ etc).\n")
    print("Please only enter a maximum of 2 decimal places (e.g 2.57).\n")

    income1 = float(input("\nIncome 1 = "))
    
    totalIncome = (income1)

    totalIncome1 = str(totalIncome)

    outcome1 = float(input("\nOutcome 1 = "))
 
    totalOutcome = (outcome1)

    totalOutcome1 = str(totalOutcome)

    totalProfit = str(totalIncome - totalOutcome)

    print("\nYour Total Profit this month is: £" + totalProfit)

    file = open("December2016.txt", "w")

    TextFile = (file.write("\nTotal Profit for this month was £" + totalProfit + "\nYou spent £" + totalOutcome1 + "\nAnd made £" + totalIncome1))

def january2017e():

    print("\nPlease only type numbers (e.g. No £,$ etc).\n")
    print("Please only enter a maximum of 2 decimal places (e.g 2.57).\n")

    income1 = float(input("\nIncome 1 = "))

    totalIncome = (income1)

    totalIncome1 = str(totalIncome)

    outcome1 = float(input("\nOutcome 1 = "))

    totalOutcome = (outcome1)

    totalOutcome1 = str(totalOutcome)

    totalProfit = str(totalIncome - totalOutcome)

    print("\nYour Total Profit this month is: £" + totalProfit)

    file = open("January2017.txt", "w")

    TextFile = (file.write("\nTotal Profit for this month was £" + totalProfit + "\nYou spent £" + totalOutcome1 + "\nAnd made £" + totalIncome1))

def february2017e():

    print("\nPlease only type numbers (e.g. No £,$ etc).\n")
    print("Please only enter a maximum of 2 decimal places (e.g 2.57).\n")

    income1 = float(input("\nIncome 1 = "))
    totalIncome = (income1)

    totalIncome1 = str(totalIncome)

    outcome1 = float(input("\nOutcome 1 = "))

    totalOutcome = (outcome1)

    totalOutcome1 = str(totalOutcome)

    totalProfit = str(totalIncome - totalOutcome)

    print("\nYour Total Profit this month is: £" + totalProfit)

    file = open("February2017.txt", "w")

    TextFile = (file.write("\nTotal Profit for this month was £" + totalProfit + "\nYou spent £" + totalOutcome1 + "\nAnd made £" + totalIncome1))


    
def menu():

    monthChoice = input("\nPlease input V to view month's or N to enter data for a month ").upper()

    if monthChoice == "V":

        print (_2016months)

        inputMonth = input("Please input the number of the month you want to view ")

        if inputMonth == "1":

            january2016()

        elif inputMonth == "2":

            february2016()

        elif inputMonth == "3":

            march2016()

        elif inputMonth == "4":

            april2016()
            
        elif inputMonth == "5":

            may2016()
            
        elif inputMonth == "6":

            june2016()
        
        elif inputMonth == "7":

            july2016()

        elif inputMonth == "8":

            august2016()

        elif inputMonth == "9":

            september2016()

        elif inputMonth == "10":

            october2016()

        elif inputMonth == "11":

            november2016()

        elif inputMonth == "12":

            december2016()

        elif inputMonth == "13":

            january2017()

        elif inputMonth == "14":

            february2017()

        else:

            print("\nSomething went wrong, please try again")

            menu()
    
    elif monthChoice == "N":

        print(_2016months)
    
        inputMonth = input("Please input the number of the month you want to enter data for ")

        if inputMonth == "1":

            january2016e()

        elif inputMonth == "2":

            february2016e()

        elif inputMonth == "3":

            march2016e()

        elif inputMonth == "4":

            april2016e()
            
        elif inputMonth == "5":

            may2016e()
            
        elif inputMonth == "6":

            june2016e()
        
        elif inputMonth == "7":

            july2016e()

        elif inputMonth == "8":

            august2016e()

        elif inputMonth == "9":

            september2016e()

        elif inputMonth == "10":

            october2016e()

        elif inputMonth == "11":

            november2016e()

        elif inputMonth == "12":

            december2016e()

        elif inputMonth == "13":

            january2017e()

        elif inputMonth == "14":

            february2017e()

        else:

            print("\nSomething went wrong, please try again")

            menu()

    else:
        print("Incorrect input, please try again")

        menu()

menu()
