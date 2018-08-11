#! /usr/local/bin/python3


shopping_list = []


def show_help():
    print("What should we pickup at the store?")
    print("""
Enter 'done' to stop adding items.
Enter 'help' for this help.
Enter 'show' to show the items in the list.
""")
    
    
def add_to_list(item):
    shopping_list.append(item)
    print("Added! list has {} items".format(len(shopping_list)))
    
    # Define a function named show_list that prints all the items in the list
    
def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print (item) 
    
show_help()
while True:
    new_item = input("> ")
    
    if new_item == 'done':
        break
    elif new_item == "help":
        show_help()
        continue
    # Enable the SHOW command to show the list. Dont forget to update the help Documentation.
    # HINT: makek sure to run it.
    
    elif new_item == 'show':
        show_list()
        continue
    
        
    
    add_to_list(new_item)
    
show_list()
