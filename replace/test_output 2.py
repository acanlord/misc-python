#! /usr/bin/python



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


def gen_html():

    top = "./templates/top.html"
    bottom = "./templates/bottom.html"


# loop through Library
    for p in pages:
        with open(p["output"], 'w') as outfile:

            # Get and dump 'top' template into 'output'

            with open(top) as infile:
                outfile.write(infile.read())
                with open(p["filename"]) as infile:
                    outfile.write(infile.read())
                with open(bottom) as infile:
                    outfile.write(infile.read())
                    outfile.write(bottom)
    #return True


def main():
    #if gen_html(pages):
     #   print("Done generating HTML files in docs/")
    #else:
     #   print("Oh snap, something went wrong")


if __name__ == "__main__":
    main()
