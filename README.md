# MajorLeagueHackingAssignment

# Introduction: 

The Hacker News API allows individuals to retrieve news information on their website: 

*	The ability to find the newest news.
*	Find the latest comments on the website.
*	Search for profile changes that a user has made. 

# Prerequisites: 

Before you begin this guide, you need the following: 

*	You need to set up a local development environment for Python 3. How to install Ubuntu? 
*	A text editor that you will be comfortable using: Sublime Text, Atom, Visual Studio Code. 
*	You need a Hacker News account. 

# What To Install:

*	You need to install Requests using PIP in Terminal. 
*	Press CTRL + ALT + T on your keyboard and type:
*	PIP install requests.

# API Calls:

*	**GET** - Requests a resource at the requested URL.
*	**OPTIONS** - Indicates which techniques are supported.
*	**HEAD** - Returns meta data from the requested URL.

# Use:

1.	Copy this code: 
 
2.	Copy the code below, indent and paste it on line 7 to make a GET API call: 
“req = requests.get('https://hacker-news.firebaseio.com/v0/updates.json?print=pretty')”
3.	Run the Python script and it will GET the information in JSON. 
 





4.	Copy the code below, indent and paste it on line 13 to make an OPTIONS API call: 
“req = requests.options('https://hacker-news.firebaseio.com/v0/updates.json?print=pretty')”
5.	Delete the # on line 27:
 
6.	Run the Python script to see which OPTIONS are supported:
 


7.	Copy the code below, indent and paste it on line 19 to make a HEAD API call: 
“req = requests.head('https://hacker-news.firebaseio.com/v0/updates.json?print=pretty')”
8.	Delete the # on line 30:
 
9.	Run the Python script to see what meta information is available the HEAD of the URL:
 
# How To Run Example:

*	**Install**: Python 3.
*	**Install**: Firefox or Chrome. 
*	**Run**: "pip install virtualenv".
*	**Run**: "source venv/bin/activate".
*	**Run**: "pip install -r requirements.txt".
*	**Run**: "python3 hackernewstep2.py".
