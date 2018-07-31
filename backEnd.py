from flask import Flask, render_template, request, session
import json
import random
import os
app = Flask(__name__)
app.secret_key = 'charles has a secret key'


@app.route("/")
def hello():
    #session_start()
    return render_template("runIt.html")

@app.route("/startses", methods = [ "POST" ])
def session_start():
	inp = json.loads(request.data.decode("utf-8"))["id"]
	if inp not in session:
		session['win'] = random.randint(1,3)
		session['score'] = 0
		session['games'] = 0


@app.route("/guessOne", methods = [ "POST" ])
def firstGuess():
	sel = json.loads(request.data.decode("utf-8"))["door"]
	generated = True
	win = session['win']
	if generated:
		if (win == 1):
			if (sel == 1):
				return str(random.randint(2,3))
			elif sel == 2:
				return "3"
			else:
				return "2"
		elif (win == 2):
			if (sel == 2):
				if random.randint(1,2) == 1:
					return "1"
				else:
					return "3"
			elif (sel == 1):
				return "3"
			else:
				return "1"
		else:
			if (sel == 3):
				return str(random.randint(1,2))
			elif (sel == 1):
				return "2"
			else:
				return "1"




@app.route("/guessTwo", methods = [ "POST" ])
def winOrLose():
	win = session['win']
	sel = json.loads(request.data.decode("utf-8"))["door"]
	if 	(sel == 1) and (win == 1):
		return '1'
	elif (sel == 2) and (win == 2):
		return '2'
	elif (sel == 3) and (win == 3):
		return '3'
	elif(sel == 1):
		return '4'
	elif(sel == 2):
		return '5'
	else:
		return '6'

@app.route("/scoreUpdate")
def updateScore():
	session['score'] = session['score'] + 1
	return str(session['score'])

@app.route("/gameUpdate")
def updateGame():
	session['games']= session['games'] + 1
	session['win'] = random.randint(1,3)
	return str(session['games'])

@app.route("/resetGame")
def resetScores():
	session['score'] = 0
	session['games'] = 0
	session['win'] = random.randint(1,3)
	return "0" 



if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
