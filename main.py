from flask import Flask, request, session, g, redirect, \
    url_for, abort, render_template, flash
import os
import requests
from datetime import date, timedelta
import json

DEBUG = True
app = Flask(__name__)
##MAPBOX_ACCESS_KEY = app.config['MAPBOX_ACCESS_KEY']

@app.route('/')
def index():
        rainData = getJson()
        return render_template('index.html', rainData= rainData)

def getJson():
        accumulated_rainfall = "precip_3hr"
	yesterday = date.today() - timedelta(1)
	startTime = yesterday.strftime('%Y-%m-%d')
	endTime = str(date.today())
	url = 'https://pmmpublisher.pps.eosdis.nasa.gov/opensearch?q='+accumulated_rainfall+'&lat=60&lon=180&limit=10&startTime='+startTime+'&endTime='+endTime+''
	data = requests.get(url).json()
	format_data = data['items'][0]['action'][5]
	#Extract geojson url from request
	rainData = format_data['using'][0]['url']
	return rainData
if __name__ == '__main__':
    app.run()
