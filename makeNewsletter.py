import pullBlog
import pdfkit
import pullLinks
import re

styles_str = "<style>p{font-size: 150%}body{font-size:150%}h4{font-size: 150%}div.blog-item-author-profile-wrapper{opacity: 0.0;height: 0px}div.blog-meta-item{opacity: 0.0;height: 0px;}h1{margin-block-start: 0.1em; margin-block-end: 0.1em}h4{margin-block-start: 0.1em; margin-block-end: 0.1em}p{margin-block-start: 0.2em; margin-block-end: 0.2em}</style>"

#chapters = open("intro.html", "r").read()
with open("out.html", "ab") as f:
    f.write(styles_str.encode(encoding="utf-8"))
    f.write("<head><meta charset='utf-8'></head>".encode(encoding="utf-8"))
    f.write("<img src='Banner.png' >".encode(encoding="utf-8"))
    f.write("<h1>August 2020</h1>".encode(encoding="utf-8"))
    


links = pullLinks.pullLinks()
blog = pullBlog.pullBlog()
intro ='<p>'+ links[0]+ '</p>' 
with open("out.html", "ab") as f:
    f.write("<h1>A note from editor </h1>".encode(encoding="utf-8"))
    f.write(intro.encode(encoding="utf-8"))
    for i in range(len(blog)):
        f.write(('<p>'+ str(i+1)+' '+blog[i][0]+ '</p>').encode())

        f.write(('<p style="margin-left: 1em">' + blog[i][1]+ '</p>').encode())
        
    f.write(('<p>'+ str(len(blog)+1)+' For further reading'+ '</p>').encode())
    
    f.write('<hr style="height:2px;border:none;color:#333;background-color:#333;">'.encode())
    for b in blog:
        f.write(b[2].encode(encoding="utf-8"))
        


space = '<hr style="height:30pt; visibility:hidden;" />'

with open("out.html", "ab") as f:
    fr = "<h1>FOR FURTHER READING </h1>"
    f.write(fr.encode(encoding="utf-8"))
    for link in links[1]:
        link = '<p>'+ link + '</p>'
        
        f.write(link.encode(encoding="utf-8"))

options = {
    'page-size': 'Letter',
    'margin-top': '0.3in',
    'margin-right': '0.75in',
    'margin-bottom': '0.3in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
}
pdfkit.from_file('out.html', 'out.pdf', options = options)

