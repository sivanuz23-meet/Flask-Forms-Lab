from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "123"
password = "123"
facebook_friends=["Loai","Sivan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		if username == request.form['username'] and password == request.form['password']:
			return redirect(url_for('home'))
		else:
			return render_template('login.html')

@app.route('/home.html', methods=['GET', 'POST'])  # '/' for the default page
def home():
	return render_template('home.html', facebook_friends = facebook_friends)
  
@app.route('/friend_exists.html/<string:name>', methods=['GET', 'POST'])  # '/' for the default page
def friends(name):
	if request.method == 'GET':
		if name in facebook_friends:
			return render_template('friend_exists.html', n = name, bool = "true")
		else:
			return render_template('friend_exists.html', n = name, bool = "false")


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)