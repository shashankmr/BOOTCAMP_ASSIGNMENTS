from flask import Flask,request
import requests

app = Flask(__name__)

@app.route('/')
def quering():
	request_str =request.args.get('request_str')
	return requests.get("https://en.wikipedia.org/wiki/"+request_str).content

if __name__ =="__main__":
	app.run()
