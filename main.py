print("Welcome to simple ATM simulator!")

balance = 1000
user_pin = "9891"

entered_pin = input("please enter your pin : ")


if entered_pin != user_pin:
    print("Invalid pin ")
    atm_on = False
else:
    atm_on = True

while atm_on:
    print("Main Menu :")
    print("1. Check Balance" )
    print ("2.Deposit Money")
    print ("3.Withdraw Money")
    print ("4.Exit")

    choice = input("Enter your choice :")

    if choice == '1':
        print ("YOur current balance is "+str(balance))
    elif choice == '2':
        amount = float(input("enter the amount to deposit :"))
        balance += amount
        print(str(amount)+" "+"deposited successful;y")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw :"))
        if amount > balance :
            print("insufficient balance !")
        else:
            balance -= amount
            print (str(amount)+"withdrawl successfully!")
    elif choice =='4':
        print("Thanku for using the ATM . GoodBye!")
        atm_on = False
    else :
        print ("invalid choice")


     

  