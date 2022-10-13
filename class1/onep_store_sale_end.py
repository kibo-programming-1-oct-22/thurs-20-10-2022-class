# The below are differnt ways to solve this coding exercise.

# Wednesday in-class code sample
# https://replit.com/@MohammedSaudi/class1#main.py


# Thursday in-class code sample
# https://replit.com/@MohammedSaudi/class-1-thursday#main.py


# Original Class Solution

BOOK_PRICE = 19.99

OLD_CAT_DISCOUNT = 0.5
FANCY_CAT_DISCOUNT = 0.3
YUMMY_CAT_DISCOUNT = 0.2

# print a message on screen
print("How many Old books?")

# get input from user
old_books = int(input())

fancy_books = input("How many Fancy books?\n")

# get convert string input to int
fancy_books = int(fancy_books)

# all in one step
yummy_books = int(input("How many Yummy books?\n"))

# test your inputs are stored correctly
# print(old_books+fancy_books+yummy_books)

# calculate the total
total = old_books * BOOK_PRICE * OLD_CAT_DISCOUNT + \
    fancy_books * BOOK_PRICE * FANCY_CAT_DISCOUNT + \
    yummy_books * BOOK_PRICE * YUMMY_CAT_DISCOUNT

# print the total
print("Total: ${:.2f}".format(total))
