# assumed user balance
user_balance = float(1234.55)

# assumed user password
user_password = "!2A34"


print("Welcome to Trusted Bank ATM")
print("1. Withdraw")
print("2. Exit")

choice = int(input("Enter 1 or 2: "))

if choice == 1:
    amount = float(input("Enter the amount: "))
    print(amount)
    # TODO 1: Check if the amount is greater than the user balance
    if amount < user_balance:
        print("Take your money")
        newBalance = user_balance - amount
        print(f"Your new balance is {newBalance}")
    else:
        print("Insufficient funds")
    # If so, print "Take your money" and deduct the amount from the user's balance
    # Also print the new balance.
    # Otherwise, print "Insufficient funds"

# TODO 2: Check if the choice is 2
elif choice == 2:
    print("Thank you for using our ATM")
# If so, print "Thank you for using our ATM"
else:
    print("Invalid choice")
# Otherwise, print "Invalid choice"


# TODO 3 (Bonus): Check if the user password is correct before implementing the withdraw logic
# TODO 4 (Bonus): Add a deposit option to the ATM
# a deposit should ask for the amount, add money to the user's balance and print the new balance
