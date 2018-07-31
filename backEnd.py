from flask import Flask, render_template, request
import random
import os
app = Flask(__name__)

win = 0
generated = False

@app.route("/")
def hello():
    return render_template("runIt.html")


@app.route("/num")
def randGenerator():
	return random.randint(1, 3)

@app.route("/guessOne", methods = [ "POST" ])
def firstGuess():
	global win
	global generated
	print(request.data)
	sel = 1 #REQUEST
	if (generated == False):
		generated = True
		win = randGenerator()


	if generated:
		if (win == 1):
			if (sel == 1):
				return str(random.randint(1,2))
			elif sel == 2:
				return "3"
			else:
				return "2"
		elif (win == 2):
			if (sel == 2):
				return str(random.randint(1,2))
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




@app.route("/guessTwo")
def winOrLose():
	global win
	sel = 0#IN A GOOD PLACE IF CAN FIGURE OUT REQUEST AND FUNCTION STRUCTURE
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

	




if __name__ == "__main__":
	app.run(port= 3500, debug=True)
