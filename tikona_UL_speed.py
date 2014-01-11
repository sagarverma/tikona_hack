# Add you username and password in data dictionary
# Run using CMD by entering python file_name.py
import mechanize
import urllib
import time
br = mechanize.Browser()
i = 1
while(i):
	time.sleep(30)
	br.open("https://login.tikona.in/userportal/logout.do?svccat=1")
	br.open("https://login.tikona.in/userportal/logout.do?svccat=1")
	br.open("https://login.tikona.in/userportal/logout.do?svccat=1")
	i+=1
	print "logout",i
	time.sleep(1)
	data = {'type':2,'username':'1109309249','password':'INVERSE#index$LAB','rememberme':'on','act':'null'}
	req = br.open('https://login.tikona.in/userportal/newlogin.do?phone=0',data=urllib.urlencode(data))
	print "login"
