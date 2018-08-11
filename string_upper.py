#! /usr/local/bin/python3

 
def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters // 2)
    print(result)

yell("You are doing great")
yell("Dont forget to ask for help")
yell("Dont Repeat Yourself. keep things DRY")

