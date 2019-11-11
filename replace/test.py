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

    for p in pages:
        base = "./templates/base.html"
        # Read in the entire template
        template = open(base).read()
        # Read in the content of the index HTML page
        index_content = open("content/index.html").read()
        # Use the string replace
        finished_index_page = template.replace("{{content}}", index_content)
        #open("docs/index.html", "w+").write(finished_index_page)
        open(p["filename"], "w+").write(finished_index_page)


gen_html()
