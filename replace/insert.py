#"index" and "value" are the line and value of your choice, lines starting from 0.

f = open("input.txt", "r")
contents = f.readlines()
f.close()

contents.insert(4, value)

f = open("output.txt", "w")
contents = "".join(contents)
f.write(contents)
f.close()
