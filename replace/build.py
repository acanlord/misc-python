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


top = "./templates/top.html"
bottom = "./templates/bottom.html"


# loop through Library
for p in pages:
    with open(p["output"], 'w') as outfile:
# Get and dump 'top' template into output file
        outfile.write(top)

# Get and dump file Content into page.output

        with open(p["filename"]) as infile:
            outfile.write(infile.read())


# Get and dump 'bottom' tempalte into 'output' file

            #outfile.write(bottom)
