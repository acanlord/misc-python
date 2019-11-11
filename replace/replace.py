# Read in the entire template
template = open("templates/base.html").read()
# Read in the content of the index HTML page
index_content = open("content/index.html").read()
# Use the string replace
finished_index_page = template.replace("{{content}}", index_content)
# Write out File
open("docs/index.html", "w+").write(finished_index_page)
