#!/usr/bin/env python

import urllib, urllib2, cookielib, sys, getpass
import encryptt, time

def generateHeaders():
	"""generate headers for the login"""
	Host = "net.zju.edu.cn"
	User_Agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0"
	Accept = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
	Accept_Language = "en-US,en;q=0.5"
	Accept_Encoding = "gzip, deflate"
	Content_Type = "application/x-www-form-urlencoded; charset=UTF-8"
	Referer = "https://net.zju.edu.cn/srun_port1.php?url=about:startpage"

	headers = {
		'Host' : Host,
		'User-Agent' : User_Agent,
		'Accept': Accept,
		'Accept-Language': Accept_Language,
		'Accept-Encoding': Accept_Encoding,
		'Content-Type': Content_Type,
		'Referer': Referer,
		}
		
	return headers


def generateLogData(req_type):
	"""generate login data"""
	
	try:
		username, password = encryptt.decrypt()
		
	except IOError:	
		username = raw_input("enter username:")
		password = getpass.getpass("enter password:")
		sampletime = input("enter a number whatever you like:")
		encryptt.encrypt(username, password, sampletime)
	
	if req_type == 0:
		raw_data = {
			'action' : "login",
			'username' : username,
			'password' : password,
			'ac_id' : "3",
			'type' : "1",
			'wbaredirect' : "http://about:startpage",
			'mac' : "undefined",
			'user_ip' : "",
			'is_ldap' : "1",
			'local_auth' : "1"
		}
	elif req_type == 1:
		raw_data = {
			'action' : "auto_dm",
			'username' : username,
			'password' : password
		}
	else:
		raise SyntaxError, 'Request type should be either 0 or 1'
	
	return urllib.urlencode(raw_data)
	

def testLog():
	"""test if already logged in"""
	tryURL = "http://www.baidu.com"
	logpageURL = "https://net.zju.edu.cn/srun_port1.php"
	
	response = urllib2.urlopen(tryURL)
	page = response.read()

	if not logpageURL in page:
		print "Already logged in. at " + getcurrtime()  
		sys.exit(0)


def generateOpener():
	""""install opener with a cookie processor"""

	cookiejar = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
	urllib2.install_opener(opener)
	
	return opener

def getcurrtime():
	
	timeformat = "%Y-%m-%d %H:%M:%S"
	
	return time.strftime(timeformat, time.localtime())


def login():
	
	logURL = "https://net.zju.edu.cn/cgi-bin/srun_portal"
	popURL = "https://net.zju.edu.cn/rad_online.php"
	logReq = urllib2.Request(logURL, generateLogData(0), generateHeaders())
	
	opener = generateOpener()
	response = opener.open(logReq)
	
	# if you already logged in Wifi on your mobile phone, 
	# the response will be in Chinese saying you've logged elsewhere.
	# note that if there is chinese in the script, the CRON will not
	# execute the script.
	# else if the login is successful, the page returned 
	# contains an javascript tag "<script> some code </script>"
	# thus keyword "script" can be used to check 
	# if we already logged in somewhere and whether to pop it out.
	
	if not "script" in response.read():
		popReq = urllib2.Request(popURL, generateLogData(1), generateHeaders())
		opener.open(popReq)
		res = opener.open(logReq)
		
	
	print "Welcome~~(^-^) at " + getcurrtime()
	sys.exit(0)

if __name__ == "__main__":
	
	attempt = 3
	
	while attempt:
		try:
			testLog()	
			login()
		except urllib2.URLError:
			print "Error: Check your network connection"
			attempt -= 1
			time.sleep(2)
	
	print ">_< I tried 3 times with no success! Bye Bye!" + getcurrtime()
	sys.exit(1)
			
			
