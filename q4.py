from flask import Flask,request,render_template
import pdb
app =Flask(__name__)

@app.route('/')
def authenticate():
	user_name_str = request.args.get('user_name')
	password_str = request.args.get('password')
	#pdb.set_trace()
	if user_name_str =='thevalleybootcamp'and password_str =='thevalley':
		return render_template('home.html')
	else:
		return render_template('login_failed.html')


if __name__ == "__main__":
	app.run()

