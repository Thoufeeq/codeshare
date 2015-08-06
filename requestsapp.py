#!/usr/bin/env python

def DownloadFile(url)
	filename = url.split('/')[-1]
	r = requests.get(url, stream=True)
	with open(filename, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024):
			if chunk: # filter out keep-alive new chunks
				f.write(chunk)
				f.flush()
	return filename
