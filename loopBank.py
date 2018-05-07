'''
Description: This program displays a menu for banking services with options to withdraw money, deposit money, check balance, change username, and exit the application.
'''
Customers = ["Mike","Jane","Steve"]
Balances = [300,300,300]
Answers = ["d","w","b","c","e"]
program = "true"

def depositFunction():
    amount = float(input("Please enter amount to be deposited: $"))
    Balances[index] = Balances[index] + amount
    return(Balances[index])

def withdrawFunction():
    amount = float(input("Please enter withdrawal amount: $"))
    if amount > Balances[index]:
        print("The amount entered is more than the allowable withdrawal amount.")
    else:
        Balances[index] = Balances[index] - amount
        return(Balances[index])

def balanceFunction():
    print("Your current balance is $","%.2f" %round(Balances[index],2))


print("Welcome to the banking application!")

name = input("Please enter username: ")
if name in Customers:
    index = Customers.index(name)
    while program == "true":
        answer = input("   Type D to deposit money"+"\n"+
            "   Type W to withdraw money"+"\n"+
            "   Type B to display Balance"+"\n"+
            "   Type C to change user and display user name"+"\n"+
            "   Type E to exit"+"\n"+">>>>")        
        answer = answer.lower()
        if answer in ["d","w","b","e"]:
            if answer == "d":
                depositFunction()
                print("Your current balance is $","%.2f" %round(Balances[index],2))
                print()
            elif answer == "w":
                balanceFunction()
                withdrawFunction()
                print("Your current balance is $","%.2f" %round(Balances[index],2))
                print()
            elif answer == "b":
                balanceFunction()
                print()
            elif answer == "e":
                print()
                print("Thank you for banking with us.")
                program="false"
        elif answer == "c":
            print()
            name=input("Please enter name: ")
            if name in Customers:
                index = Customers.index(name)
        else:
            print("Invalid response.")
            print()
else: 
    print("Name entered not in file. Please restart program.")

    






    