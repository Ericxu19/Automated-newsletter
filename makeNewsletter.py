import pullBlog
import pdfkit
import pullLinks
import re

styles_str = "<style>p{font-size: 150%}body{font-size:150%}h4{font-size: 150%}div.blog-item-author-profile-wrapper{opacity: 0.0;height: 0px}div.blog-meta-item{opacity: 0.0;height: 0px;}</style>"

chapters = open("intro.html", "r").read()
with open("out.html", "ab") as f:
    f.write(styles_str.encode(encoding="utf-8"))
    f.write("<head><meta charset='utf-8'></head>".encode(encoding="utf-8"))
    f.write("<img src='Banner.png' >".encode(encoding="utf-8"))
    f.write("<p>August<p><br>".encode(encoding="utf-8"))
    


links = pullLinks.pullLinks()
intro ='<p>'+ links[0]+ '<p>' 
with open("out.html", "ab") as f:
    f.write("Introduction: <br>".encode(encoding="utf-8"))
    f.write(intro.encode(encoding="utf-8"))
    f.write(chapters.encode(encoding="utf-8"))

pullBlog.pullBlog()

space = "<br>"

with open("out.html", "ab") as f:
    fr = "<P>For further reading: </p>"
    f.write(fr.encode(encoding="utf-8"))
    for link in links[1]:
        link = '<p>'+ link + '</p>'
        f.write(space.encode(encoding="utf-8"))
        
        f.write(link.encode(encoding="utf-8"))

options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
}
pdfkit.from_file('out.html', 'out.pdf', options = options)

