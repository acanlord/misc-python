#! /usr/local/bin/python3

 

 first_name = input("What is your first name?")

print("Hello,",first_name)
if first_name == "rich":
    print(first_name, "is learning Pyhton")
elif first_name == "george":
    print(first_name, "is learning with fellow students community")
else:
    age = int(input("How old are you? "))
    if age <= 6:
        print ("Wow you're {}! If your confident with reading your already.." .format(age))
    print("You should totally learn python, {}!".format(first_name))
print("Have a great day {}!".format(first_name))
      
