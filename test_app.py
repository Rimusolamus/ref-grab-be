import requests
from flask import Flask
import json


app = Flask(__name__)

url = "https://data.unhcr.org/population/?widget_id=351610&sv_id=54&population_group=5478"

@app.route('/')
def home():
	r = json.loads(requests.get(url).content)["data"][0]
	return r

