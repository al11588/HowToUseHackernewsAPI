import requests

# Item and profile changes in hackernews

# Requests a resource at the requested URL.
def hackernewsgetapirequest():
	req = requests.get('https://hacker-news.firebaseio.com/v0/updates.json?print=pretty')
	print (req.text)
	print ("Status Code", req.status_code)
	
# Indicates which techniques are supported
def hackernewsoptionsapirequest():
	req = requests.options('https://hacker-news.firebaseio.com/v0/updates.json?print=pretty')
	print (req.text)
	print ("Status Code", req.status_code)

# It returns meta information. 
def hackernewsheadapirequest():
	req = requests.head('https://hacker-news.firebaseio.com/v0/updates.json?print=pretty')
	print (req.text)
	print ("Status Code", req.status_code)


hackernewsgetapirequest()

#hackernewsoptionsapirequest()

#hackernewsheadapirequest()