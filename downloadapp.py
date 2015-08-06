#!/usr/bin/env python

import requests

url = "http://thoufeeq.com/downloads/scan1.pdf"

print "Starting Download..."
r = requests.get(url)
with open("desired_filename.pdf", "wb") as code:
	code.write(r.content)
