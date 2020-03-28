import horoscope
from datetime import datetime as dt

def generate_body (header,paragraphs):
    body="<h1>" + header + "</h1>"
    for p in paragraphs:
        body+="<p>"+ p + "</p>"
    return "<body><center><font size='4em'>"+  body + "</center></body>"

def generate_page(head,body):
    page="<html>"+ head+body+"</html>"
    return page

def generate_head(title):
    title="<title>"+ title+"</title>"
    return "<head>"+title+"</head>"

def save_page(title, header, paragraps, output="index.html"):
    fp=open(output,'w')
    today=dt.now().date()
    page=generate_page(
        head=generate_head(title),
        body=generate_body(header, paragraps)
    )
    print(page, file=fp)

    fp.close()

body_page=generate_body(header="Гороскоп на 2018-11-12", paragraphs=horoscope.generate_prophecies())
save_page("pidar","zalupa",horoscope.generate_prophecies())

#fp=open("1.html","w")
#print(body_page,file=fp)
#fp.close()

