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


def gen_html(pages):
    base = "./templates/base.html"

    for p in pages:
        # Read in the entire template
        template = open(base).read()
        # Read in the content of the index HTML page
        #index_content = open("content/index.html").read()
        index_content = open(p["filename"]).read()
        # Use the string replace
        finished_index_page = template.replace("{{content}}", index_content)
        #open("docs/index.html", "w+").write(finished_index_page)
        open(p["filename"], "w+").write(finished_index_page)



#def main():
#      if gen_html(pages):
#          print('Done generating HTML files at docs/')
#      else:
#          print('oh snap, theres a problem here!!')
#
#if __name__ == "__main__":
#    main()
