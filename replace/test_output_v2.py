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


def get_template(template):
    with open(template) as template_contents:
        return template_contents.read()

def gen_html():

    top = "./templates/top.html"
    bottom = "./templates/bottom.html"
#    top_html = get_template(top)
#    top_html = top_html.replace("{{title}}", p["title"])


# loop through Library
    for p in pages:
        with open(p["output"], 'w') as outfile:
            top_html = get_template(top)
            top_html = top_html.replace("{{title}}", p["title"])
            outfile.write(top_html)

            # Get and dump page.filename conents into page.output
            with open(p["filename"]) as infile:
                outfile.write(infile.read())

            # Get and dump 'bottom' template into 'output' file
            outfile.write(get_template(bottom))

                              #with open(bottom) as infile:
                              #    outfile.write(infile.read())
                              #    outfile.write(get_template(bottom))

                #with open(top) as infile:
                #    outfile.write(infile.read())
                #        with open(p["filename"]) as infile:
                #            outfile.write(infile.read())
                #            with open(bottom) as infile:
                #                outfile.write(infile.read())
                #                outfile.write(get_template(bottom))


def main():

    gen_html()


if __name__ == "__main__":
    main()
