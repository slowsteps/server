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
	print("in setlocation")
	print(data)
	conn = sqlite3.connect('database.db')
	conn.execute("INSERT INTO locations VALUES (?,?,?,?)",( data['longitude'], data['latitude'], data['speed'], data['course'] ))
	conn.commit()
	return {"answer" : "location data received" , "data" : data}



@app.route('/getlocation')
def getlocation():
	print("in getlocation")
	result = "no location"
	conn = sqlite3.connect('database.db')
	cursor = conn.execute("SELECT * from locations")
	rows = cursor.fetchall()
	for row in rows:
		result = {"longitude" : row[0] , "latitude" : row[1], "speed" : row[2], "course" : row[3]}
	conn.close()
	return result


@app.route('/reset')
def reset():
	conn = sqlite3.connect('database.db')
	conn.execute('DROP TABLE locations')
	conn.execute('CREATE TABLE locations (longitude REAL, latitude REAL, speed REAL, course REAL)')
	conn.commit()
	conn.close()
	return('table reset')

@app.route('/locations')
def getalldata():
	result = ""
	conn = sqlite3.connect('database.db')
	cursor = conn.execute("SELECT * from locations")
	rows = cursor.fetchall()
	for row in rows:
		result = result + str(row[0]) + ";"
	conn.close()
	return result



