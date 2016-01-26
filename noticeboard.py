import gmail
import exceptions
import subprocess
import time

g = gmail.login("trilaciousexps@gmail.com", "experiments@tlabs")


def startscreen():
	outfile = open("message.html", "wb")
	# Starting to write the Startscreen content to file as HTML
	print >>outfile, """<html>
	<head>
	<title>Smart NoticeBoard</title>
	<meta http-equiv="refresh" content="10">
	<link rel="stylesheet" type="text/css" href="style.css">
	</head>
	<body>
	<br />
	<h1>Smart NoticeBoard</h1>
	<h4>Final Year B.Tech Project, ECE Dept., NCERC</h4>
	<h3>Group Members</h3>
	<li>Group Member 1</li>
	<li>Group Member 2</li>
	<li>Group Member 3</li>
	<li>Group Member 4</li>
	<li>Group Member 5</li>
	<h3>Project Guide: First Name Last Name</h3>\n"""
	# print >>outfile, "<h4>%s</h4>" %(time.ctime())
	print >>outfile, """</body>
	</html>"""
	# writing to startscreen content ends here
	outfile.close()
	return

startscreen()

subprocess.Popen(['/usr/bin/chromium', '--kiosk', '--noerrdialogs', 'message.html'])

while True:
	try:
		#g = gmail.login("trilaciousexps@gmail.com", "experiments@tlabs")
		g.inbox().mail()
		print "Scanning INBOX"
		unread = g.inbox().mail(unread=True, sender="thoufeeq.mohd@gmail.com")
		print "Scanning for UNREAD mail"
		unread[-1].fetch()
		email_body = unread[-1].body
		#print unread[-1].body
		outfile = open("message.html", "wb")
		# writing html to the document starts here
		print >>outfile, """<html>
	    	<head>
	            <title>Notification!</title>
	            <meta http-equiv="refresh" content="10">
		    <link rel="stylesheet" type="text/css" href="style.css">
	    	</head>
	    	<body>
		<br />
		<h1>ATTENTION!</h1>"""
	    	print >>outfile, "<h2>%s</h2>" %(email_body)
	    	print >>outfile, "<p>--</p>\n"
	    	print >>outfile, "H.O.D, ECE Dept.\n"
	    	print >>outfile, "NCERC\n"
	    	print >>outfile, "<h4>%s</h4>" %(time.ctime())
	    	print >>outfile, """<body>
	    	</html>"""
	    	# HTML writing ends here
		outfile.close()
		for i in unread:
			i.read()
		print "Fetched the recent UNREAD mail"
		
	except (IndexError, gmail.exceptions.AuthenticationError):
		g.logout()
		g = gmail.login("trilaciousexps@gmail.com", "experiments@tlabs")
		print "No new notifications. Scanning continues..."
	


