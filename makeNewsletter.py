import pullBlog
import pdfkit
import pullLinks
import re

styles_str = "<style>p{font-size: 120%}body{font-size:120%}h4{font-size: 12S0%}div.blog-item-author-profile-wrapper{opacity: 0.0;height: 0px}div.blog-meta-item{opacity: 0.0;height: 0px;}h1{margin-block-start: 0.1em; margin-block-end: 0.1em}h4{margin-block-start: 0.1em; margin-block-end: 0.1em}p{margin-block-start: 0.2em; margin-block-end: 0.2em}</style>"

#chapters = open("intro.html", "r").read()
with open("out.html", "ab") as f:
    f.write(styles_str.encode(encoding="utf-8"))
    f.write("<head><meta charset='utf-8'></head>".encode(encoding="utf-8"))
    f.write('<img src="https://images.squarespace-cdn.com/content/v1/5ecd504cf4aac80c66bc8fa0/1599774235089-I7NT3ZE9GIXAMG3MZQD6/ke17ZwdGBToddI8pDm48kDLZMA5A_0QTt70JA05UypMUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8N_N4V1vUb5AoIIIbLZhVYy7Mythp_T-mtop-vrsUOmeInPi9iDjx9w8K4ZfjXt2dsn8kDoUsqm_RvvYkNOfzP_cCjuFVRfEFw1RcssrXSLJCjLISwBs8eEdxAxTptZAUg/The+covid+guide+newsletter%284%29.png">'.encode(encoding="utf-8"))
    f.write("<h1>September 2020</h1>".encode(encoding="utf-8"))
    


links = pullLinks.pullLinks()
blog = pullBlog.pullBlog()
intro ='<p>'+ links[0]+ '</p>' 
with open("out.html", "ab") as f:
    f.write("<h1>Table of contents</h1>".encode(encoding="utf-8"))
    
    for i in range(len(blog)):
        f.write(('<p>'+ str(i+1)+' '+blog[i][0]+ '</p>').encode())

        f.write(('<p style="margin-left: 1em">' + blog[i][1]+ '</p>').encode())
        #f.write((str(i)+' '+blog[i][0]+'/n').encode(encoding="utf-8"))
    f.write(('<p>'+ str(len(blog)+1)+' For further reading'+ '</p>').encode())
    #f.write(chapters.encode(encoding="utf-8"))
    f.write('<hr style="height:2px;border:none;color:#333;background-color:#333;">'.encode())
    for b in blog:
        b[2] = str(b[2])
        b[2] = re.sub(r'Uma Kalkar','', b[2])
        b[2] = re.sub(r'Uma Kalkar','', b[2])
        f.write(b[2].encode(encoding="utf-8"))
        f.write('<hr style="height:2px;border:none;color:#333;background-color:#333;">'.encode())
        


space = '<hr style="height:30pt; visibility:hidden;" />'

with open("out.html", "ab") as f:
    fr = "<h1>FOR FURTHER READING </h1>"
    f.write(fr.encode(encoding="utf-8"))
    for link in links[1]:
        date = ''
        d = re.findall(r'\[(.*?)\]', link)

        if d:
            date = d[-1]
        link = re.sub(r'\[(.*?)\]','', link)
        actualLink = re.findall(r'http.*$', link)
        if actualLink:
            actualLink = actualLink[0]
        else:
            actualLink = ''
        link = re.sub(r'http.*$','', link)
        link = link.strip()
        f.write('<p><a href='.encode() )
        f.write(actualLink.encode(encoding="utf-8"))
        f.write('><span style="text-decoration:underline">'.encode())
        f.write(link.encode(encoding="utf-8"))
        f.write('</span></a>'.encode())
        f.write(date.encode(encoding="utf-8"))
        f.write('</p>'.encode())

options = {
    'page-size': 'Letter',
    'margin-top': '0.3in',
    'margin-right': '0.75in',
    'margin-bottom': '0.3in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
}
pdfkit.from_file('out.html', 'out.pdf', options = options)

