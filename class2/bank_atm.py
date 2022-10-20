import sys
# assumed user balance
user_balance = float(1234.55)

# assumed user password
user_password = "!2A34"

#Checking if the user password is correct before implementing the withdraw logic
pin = str(input("Enter Pin: "))

if pin != user_password:
    print("Invalid Pin")
    sys.exit()


print("Welcome to Trusted Bank ATM")
print("1. Withdraw")
print("2. Exit")
print("3. Deposit")



choice = int(input("Enter 1, 2 or 3: "))

if choice == 1:
    amount = float(input("Enter the amount: "))
    # Checking if the amount is greater than the user balance
    if amount <= 0:
        print("Invalid amount")
    elif amount <= user_balance:
        # If so, print "Take your money" and deduct the amount from the user's balance
        print("Take your money")
        newBalance = user_balance - amount
        print(f"Your new balance is {newBalance}")
    else:
        print("Insufficient funds")


# Checking if the choice is 2
elif choice == 2:
    print("Thank you for using our ATM")
    
elif choice == 3:
    deposit = float(input("How much do you want to deposit: "))
    newUserBalance = float(deposit + user_balance)
    print(f"Your new balance is {newUserBalance}")

else:
    print("Invalid choice")


