from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "r12"
password = "1234"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == "POST":	
		if request.form['username'] == username and request.form['password'] == password:
			return render_template('home.html', facebook_friends=facebook_friends)
		else:
	 		return render_template('login.html', error = 'wrong password or/and username')

	else:
	 	return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])  # '/' for the default page
def home():
	 	return render_template('home.html', facebook_friends=facebook_friends)





@app.route('/friend_exists/<string:name>') # '/' for the default page
def friend(name):
	if name in facebook_friends:
		friend = True
	else:
		friend = False
	return render_template('friend_exists.html', name=name, friend=friend)
 


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True)