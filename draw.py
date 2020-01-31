import stddraw
stddraw.setFontSize(40)
def draw_hangman(guesses):
		stddraw.setPenColor(stddraw.BLACK)
		if guesses == 7:
			#head
			stddraw.circle(0.5,0.8,0.07)
		elif guesses == 6:
			#body
			stddraw.line(0.5,0.73,0.5,0.5)
		elif guesses == 5:
			#left hand
			stddraw.line(0.5,0.67,0.55,0.53)
		elif guesses == 4:
			#right hand
			stddraw.line(0.5,0.67,0.45,0.53)
		elif guesses ==3:
			#left leg
			stddraw.line(0.5,0.5,0.55,0.36)
		elif guesses == 2:
			#right leg
			stddraw.line(0.5,0.5,0.45,0.36)
		elif guesses == 1:
			#gallows
			stddraw.line(0.5,0.87,0.5,0.95)
			stddraw.line(0.5,0.95,0.8,0.95)
			stddraw.line(0.8,0.95,0.8,0.3)
			stddraw.line(0.9,0.3,0.4,0.3)
			stddraw.line(0.4,0.3,0.4,0.28)
			stddraw.line(0.9,0.3,0.9,0.28)
			stddraw.line(0.0,0.28,1.0,0.28)
		else:
			#face
			stddraw.line(0.47,0.8,0.488,0.82)
			stddraw.line(0.488,0.8,0.47,0.82)
			stddraw.line(0.518,0.8,0.536,0.82)
			stddraw.line(0.536,0.8,0.518,0.82)
			stddraw.line(0.47,0.77,0.53,0.77)
		stddraw.show(0)
def draw_hangman_dash(word):
	stddraw.setPenColor(stddraw.BLACK)
	for i in range (len(word)):
		stddraw.text(i*0.07 + 0.1,0.2,"-")
		
		
def draw_letters(i,letter):
	stddraw.setPenColor(stddraw.BLUE)
	stddraw.text(i*0.07 + 0.1,0.25,letter)
	stddraw.show(0)
	
def draw_wrong_letters(wrong_letters):	
	stddraw.setPenColor(stddraw.RED)
	for i in range (len(wrong_letters)):
		stddraw.text(i*0.07 + 0.1,0.04,wrong_letters[i])
		