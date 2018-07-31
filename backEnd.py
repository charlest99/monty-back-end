from flask import Flask, render_template, request, session
import json
import random
import os
app = Flask(__name__)

win = 0
score = 0
games = 0


@app.route("/")
def hello():
    session['tmp'] = 43
    return render_template("runIt.html")


@app.route("/guessOne", methods = [ "POST" ])
def firstGuess():
	global win
	sel = json.loads(request.data.decode("utf-8"))["door"]
	generated = True
	win = random.randint(1,3)
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
	global win
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
	global score
	score+=1
	return str(score)

@app.route("/gameUpdate")
def updateGame():
	global games
	games+=1
	return str(games)

@app.route("/resetGame")
def resetScores():
	global games
	global score
	score = 0
	games = 0
	return "0" 



if __name__ == "__main__":
	app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
