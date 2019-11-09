#! /usr/bin/python


import os




pages = [ 
    { 
        "filename": "./content/index.html",
        "output": "docs/index.html",
        "title": "About Me",
    },
    {
        "filename": "./content/projects.html",
        "output": "docs/projects.html",
        "title": "Projects",
    },
    {

        "filename": "./content/blog.html",
        "output": "docs/blog.html",
        "title": "blog",
    }
    ]


# Read contents of file 
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



#Eaiser , does not need to close file, with file.close()
for p in pages:
    with open(p["output"], 'w') as out_file:


    # Get and dum ppalge.filename contents into page.output

        with open(p["filename"]) as infile:
            outfile.write(infile.read())

    # Get and dump 'Bottom' template into 'output' filename

        outfile.write(bottom)


