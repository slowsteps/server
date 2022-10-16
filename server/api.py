from flask import Flask,request,render_template
import sqlite3
import time

app = Flask(__name__)



@app.route('/')
def home():
	return render_template('index.html')


# use setlocation?location=somenew56794
@app.route('/setlocation')
def sendlocation():
	newlocation = request.args.get('location')
	print(newlocation)
	conn = sqlite3.connect('database.db')
	conn.execute("INSERT INTO locations VALUES (?)",(newlocation,))
	conn.commit()
	return 'setlocation'

@app.route('/getlocation')
def getlocation():
	result = "no location"
	conn = sqlite3.connect('database.db')
	cursor = conn.execute("SELECT * from locations")
	rows = cursor.fetchall()
	for row in rows:
		result = row[0]
	conn.close()
	return result


@app.route('/reset')
def reset():
	conn = sqlite3.connect('database.db')
	conn.execute('DROP TABLE locations')
	conn.execute('CREATE TABLE locations (location TEXT)')
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



