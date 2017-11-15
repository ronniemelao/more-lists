"""
Goal: Create code to allow a user to create a shopping list
Minimum requirements:
  * User can enter items which will be stored in the shopping list
  * User can exit item entry mode, which will cause the program to print the contents of the list
Stretch goals:
  * User can delete an item from the list
  * A command user can enter at any time to display the contents of the list

Advice:
  * You want to continue doing this for an unknown number of repetitions - what sort of loop would you use?
  * Remember that break will take you out of a loop, so you could say that if some string were entered - for instance 'exit' - you would do something and exit the loop
  * You're probably going to want to use input() and shopping_list.append()
  * Remember to do this one step at a time.
    * Make sure you can add a single item before you try to loop it.
    * Make sure the loop is working before you worry about how to do more advanced things

There is no automated checking on this one
"""

shopping_list = []

#prints directions for the user, as well as how to exit the loop
print("Type out your shopping list when prompted. When you are finished, type 'done'.")

#for loop in which the user can add an item to the shopping list, and this item is added to the shopping_list list
while True:
    x=input("What do you need to buy?  ")
    shopping_list.append(x)
    if x == "done":
        del shopping_list[-1]
        break

#prints shopping list with bullets and a title
print("Your Shopping List:")
for item in shopping_list:
    print(f" - {item}")
