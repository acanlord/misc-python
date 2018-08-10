#! /usr/local/bin/python3 

continents = ['Asia', 'South America', 'North America', 'Africa', 'Europe', 'Antarctica', 'Australia']
# Your code here


# Print first char of each element

#print ("Contients:")
for i in continents:
   if i[0] == "A":
      print("* " + i)

# Print if starts with A
print("Continents:")
for i in continents:
    if i.startswith('A'):
        print ("* " + i)
