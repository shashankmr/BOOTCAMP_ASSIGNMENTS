import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def ext_url_conn():
	return requests.get('https://www.wikipedia.org/').content


if __name__ =='__main__':
	app.run()

