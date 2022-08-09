import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()

content= ''

def extract_news(url):
    print("Extracting latest cyber security news for you......")
    cnt=''
    cnt+= ('<b> Top Stories From Cyber World </b>\n ')
    response=requests.get('url')
    content=response.content
    soup= BeautifulSoup(content, 'html.parser')
    for i,tag in enumerate(soup.findAll('td',attrs={'class':'title','valign':''})):
        cnt +=((str(i+1)+'::'+tag.text + "\n" + '<br>') if tag.text!='more' else '')
    return cnt

cnt = extract_news('https://news.ycombinator.com/')
content +=cnt
content += ('<br>-----------------------<br>')
content +=('<br><br> THE END ')

print("composing email........")
SERVER = 'smtp.gmail.com'
PORT= 587
FROM='senderemail@gmail.com'
TO ='reciveremail@gmail.com'
PASS= 'sender@password'

msg= MIMEMultipart()

msg['Subject']='Top News Stories HN [ Automated Email ]' + '' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)

msg['FROM']=FROM
msg[TO]=TO

msg.attach(MIMEText(content,'html'))

print ('Initiating server...')
server=smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(0)
server.ehlo()
server.starttls()
server.login(FROM,PASS)
server.sendmail(FROM,TO,msg.as_string())
print('Email sent successfully ....')
server.quit()