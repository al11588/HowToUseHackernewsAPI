import requests

# Item and profile changes in hackernews

# Requests a resource at the requested URL.
def hackernewsgetapirequest():
	req = requests.get('')
	print (req.text)
	print ("Status Code", req.status_code)

# Indicates which techniques are supported.
def hackernewsoptionsapirequest():
	req = requests.options('')
	print (req.text)
	print ("Status Code", req.status_code)

# Returns meta information in that given URL. 
def hackernewsheadapirequest():
	req = requests.head('')
	print (req.text)
	print ("Status Code", req.status_code)

# Requests a resource at the requested URL.
hackernewsgetapirequest()

# Indicates which techniques are supported.
#hackernewsoptionsapirequest()

# Returns meta information in that given URL. 
#hackernewsheadapirequest()