from flask import Flask,request
import pdb

app = Flask(__name__)

@app.route('/')
def password_auth():
	username_str = request.args.get('username')
	password_str = request.args.get('password')
	if username_str =='valleybootcamp' and password_str =='thevalley':
		return 'Login Successful'
	else:
		return 'Login unsuccessful'

if __name__ =='__main__':
	app.run()
