#read contents of file 
with open('data.txt', 'r') as f:
    data = f.read()

print(data)


# Write stuff file
with open ('data.txt', 'w') as f:
    data = 'Your mom is a cool guy'
    f.write(data)


print(data)

# Get directory listing
entries = os.listdir('./docs/')
for file in entries:
    print(file)


textList = ["I", "Like", "To", "Eat", "Tacos"]

# Write out file
outF = open("myOutFile.txt", "w")
for line in textList:
    # Write line to output file
    outF.write(line)
    outF.write("\n")
outF.close()


outF = open("MyOUtFile.txt", "w")
for line in textList:
    print >>outF, line
outF.close()
