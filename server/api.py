from flask import Flask,request,render_template
import sqlite3
import time

app = Flask(__name__)



@app.route('/')
def home():
	return render_template('index.html')


@app.route('/setlocation', methods=['POST'])
def sendlocation2():
	data = request.get_json()
	conn = sqlite3.connect('database.db')
	conn.execute("INSERT INTO locations VALUES (?,?,?,?,?)",( data['longitude'], data['latitude'], data['speed'], data['course'], data['timesend']))
	conn.commit()
	return {"answer" : "location data received" , "data" : data}



@app.route('/getlocation')
def getlocation():
	result = "no location"
	conn = sqlite3.connect('database.db')
	cursor = conn.execute("SELECT * from locations")
	rows = cursor.fetchall()
	for row in rows:
		result = {"longitude" : row[0] , "latitude" : row[1], "speed" : row[2], "course" : row[3], "timesend" : row[4]}
	conn.close()
	return result


@app.route('/reset')
def reset():
	conn = sqlite3.connect('database.db')
	conn.execute('DROP TABLE locations')
	conn.execute('CREATE TABLE locations (longitude REAL, latitude REAL, speed REAL, course REAL, timesend REAL)')
	conn.commit()
	conn.close()
	return('table reset')


@app.route('/mapdata')
def getalldata():
	result = "<pre>longitude,latitude,speed,course,timesend \n"
	conn = sqlite3.connect('database.db')
	cursor = conn.execute("SELECT * from locations")
	rows = cursor.fetchall()
	
	for row in rows:
		result = result + str(row[0]) + "," + str(row[1]) + "," + str(row[2]) + "," + str(row[3]) + "," + str(row[4]) + "\n"
	conn.close()
	result = result + "</pre>"
	return result



