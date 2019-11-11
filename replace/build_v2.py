#! /usr/bin/python

import os



pages = [
        {
        "filename": "./content/about.html",
        "output": "./docs/bout.html",
        "title": "About Me",
        },
        {
        "filename": "./content/projects.html",
        "output": "./docs/Projects.html",
        "title": "Projects",
        },
        {
        "filename": "./content/blog.html",
        "output": "./docs/blog.html",
        "title": "Blog",
        }



# Generate HTML content 

#print("Were going to gen your new html content")


def gen_html():

    top = "./templates/top.html"
    bottom = "./templates/bottom.html"


# Loop through LIbrary and open file
for p pages:
with open('pages.filename', 'w') as outfile:

# Read in files
     with open(fname) as infile:
            outfile.write(infile.read())



def main():


if __name__=="__main__":
    main()
