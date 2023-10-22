# NB: This file is not used in our project
# We plan to, but it turns out frontend can accomplish every function
# so we save the trouble to request from backend
# We leave the file here for further reference

from flask import Flask
import datetime

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)


# Route for seeing a data
@app.route('/data')
def get_time():

	# Returning an api for showing in reactjs
	return {
		'Name':"geek", 
		"Age":"22",
		"Date":x, 
		"programming":"python"
		}

	
# Running app
if __name__ == '__main__':
	app.run(debug=True)
