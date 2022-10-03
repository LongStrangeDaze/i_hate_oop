# #  Build a Shopping Cart
# # You can use either lists or dictionaries. The program should have the following capabilities:

# # 1) Takes in input
# # 2) Stores user input into a dictionary or list
# # 3) The User can add or delete items
# # 4) The User can see current shopping list
# # 5) The program Loops until user 'quits'
# # 6) Upon quiting the program, print out all items in the user's list


# shopping_cart = {}

# print("""
#     "Welcome to S-Mart"
#     1:add item
#     2:remove item
#     3:view basket
#     0:quit
# """)

# choice = int(input("Make your selection: "))

# while choice != 0:
#     if choice == 1:
#         item = input("Chose an item: ")
#         amount = input("How many would you like?: ")
#         shopping_cart[item] = amount

#     elif choice == 2:
#         item = input("chose a item to remove: ")
#         del (shopping_cart[item])

#     elif choice == 3:
#         for item in shopping_cart:
#             print(item, ":", shopping_cart[item])

#     elif choice != 0:
#         print("Make your selection again.")

#     choice = int(input("\n\nSelect a choice: "))
# else:
#     print(item, ":", shopping_cart[item])
#     print("Thank you for shopping S-Mart.")


class Shopping_cart():
    def __int__(self, choice_1, choice_2, choice_3, choice_0):
        choice_1 = item
        choice_2 = del_item
        choice_3 = view
        choice_0 = end

    def item:
    item = input("Chose an item: ")
    amount = input("How many would you like?: ")
    shopping_cart[item] = amount

    def del_item:
    del_item = input("chose a item to remove: ")
    del (shopping_cart[item])

    def view:
    for item in shopping_cart:
        print(item, ":", shopping_cart[item])

    def end:
    print(item, ":", shopping_cart[item])
    print("Thank you for shopping S-Mart.")
