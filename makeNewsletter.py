import pullBlog
import pdfkit
import pullLinks
import re

styles_str = "<style>p{font-size: 150%}body{font-size:150%}</style>"

with open("out.html", "ab") as f:
    f.write(styles_str.encode(encoding="utf-8"))
    f.write("<head><meta charset='utf-8'></head>".encode(encoding="utf-8"))
    f.write("<img src='Banner.png' >".encode(encoding="utf-8"))


pullBlog.pullBlog()

space = "<br>"

links = pullLinks.pullLinks()
with open("out.html", "ab") as f:
    fr = "<P> for further reading: </p><br>"
    for link in links:
        f.write(space.encode(encoding="utf-8"))
        f.write(link.encode(encoding="utf-8"))

    
pdfkit.from_file('out.html', 'out.pdf')

