# MAC OS initialization
# Open terminal

# Install Python Package Index
	$ sudo easy_install pip

# Clone the openai gym github repository
	$ git clone https://github.com/openai/gym

# Change the directory
	$ cd gym

# install all gym python dependencies
	$ pip install gym[all]				

# Create a python script containing code 

# Create a virtual environment. 
# virtualenv is a tool to create isolated Python environments.
# virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

# Firstly, Install virtualenv via pip:
	$ pip install virtualenv

# Create and proceed further by following commands
	$ virtualenv venv
	$ source venv/bin/activate
	$ pip install requests

# Do once again 
	$ pip install gym[all]
	
# run the .py script
 	$ python testrun.py

