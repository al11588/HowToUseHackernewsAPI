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

![Image1](https://github.com/al11588/MajorLeagueHackingAssignment/blob/master/images/1.png =50*50) 
 
2.	Copy the code below, indent and paste it on line 7 to make a GET API call: 

“req = requests.get('https://hacker-news.firebaseio.com/v0/updates.json?print=pretty')”

3.	Run the Python script and it will GET the information in JSON. 

![Image2](https://github.com/al11588/MajorLeagueHackingAssignment/blob/master/images/2.png)

4.	Copy the code below, indent and paste it on line 13 to make an OPTIONS API call: 

“req = requests.options('https://hacker-news.firebaseio.com/v0/updates.json?print=pretty')”

5.	Delete the # on line 27:

![Image3](https://github.com/al11588/MajorLeagueHackingAssignment/blob/master/images/3.png) 

6.	Run the Python script to see which OPTIONS are supported:
 
![Image4](https://github.com/al11588/MajorLeagueHackingAssignment/blob/master/images/4.png) 

7.	Copy the code below, indent and paste it on line 19 to make a HEAD API call:

“req = requests.head('https://hacker-news.firebaseio.com/v0/updates.json?print=pretty')”

8.	Delete the # on line 30:

![Image5](https://github.com/al11588/MajorLeagueHackingAssignment/blob/master/images/5.png) 
 
9.	Run the Python script to see what meta information is available the HEAD of the URL:

![Image6](https://github.com/al11588/MajorLeagueHackingAssignment/blob/master/images/6.png) 
 
# How To Run Example:

*	**Install**: Python 3.

*	**Install**: Firefox or Chrome.

*	**Run**: "pip install virtualenv".

*	**Run**: "source venv/bin/activate".

*	**Run**: "pip install -r requirements.txt".

*	**Run**: "python3 hackernewstep2.py".