# Evil Hangman - the classic hangman with an evil touch where the chosen word changes to make the player lose more turns
# simple GUI
import sys
import stdio
import random
import draw
import stddraw

# read a text file (list of words to be used) in the argument and put them in a list
mlist = open(sys.argv[1])
words = mlist.readlines()
mlist.close()

# initializing game variables
letters = []
wrong_letters = []
correct_letters = []
word = ""
guesses = 8
list_of_words = []
list_of_letters = []
number_of_letter = []
secret_word = []
number = 0
goal = 0
biggest = 0
array = []
found = False
num = 0
correct_guess = 0
correct_letters = []
dublicate = False

# pick a random word from the list of words
while len(word)< 4 or len(word)>9:
	number = random.randrange(0,len(words))
	word = words[number].rstrip()
for i in range (len(words)):
	words[i] = words[i].rstrip()
for i in words:
	if len(i) == len(word):
		list_of_words.append(i)
for i in range (len(word)):
	secret_word.append("-")
for i in list_of_words	:	
	for j in range(len(i)):
		letters.append(["-",i[j]])
	list_of_letters.append(letters)
	letters = []
	
# show the current status in gui
draw.draw_hangman_dash(word)
stddraw.show(0)

# while the player has turns, keep playing
while guesses > 0 and correct_guess != len(word):
	
	# print the number of guesses remaining
	print("The secret word looks like:")
	for i in range(len(word)):
		stdio.write(secret_word[i])
	if len(wrong_letters) > 0:
		print ("\nYour bad guesses so far: " + (' '.join(wrong_letters)))
	if len(wrong_letters) > 0:
		print("You have " + str(guesses) + " guesses remaining.")
	else:
		print("\nYou have " + str(guesses) + " guesses remaining.")
	
	# input the next letter from the player
	letter = input("What's your next guess? ")
	for j in range(len(list_of_letters)):		
		for i in range (len(word)):
			if letter == list_of_letters[j][i][1]:
				list_of_letters[j][i][0] = letter
	for i in range(len(list_of_letters)):
		array.append([])
	for m in range(len(list_of_letters)):			
		for j in range(len(list_of_letters)):		
			for i in range (len(word)):
				if list_of_letters[m][i][0] == list_of_letters[j][i][0]:
					number +=1
			if number == len(word):
				array[m].append(list_of_letters[j])
			number = 0
	for i in range (len(array)):
		if len(array[i]) == 0:
			num += 1
	if num == len(array):
		for i in range(len(list_of_letters)):
			array[i] = list_of_letters[j]
	num = 0
	temp = 0
	t = []
	for i in range(len(array)):
		if len(array[i]) > temp:
			temp = len(array[i])
			t = array [i]
	
	list_of_letters = t
	t = []
	array = []
	random.shuffle(list_of_letters)
	for i in range(len(word)):
		if letter in list_of_letters[0][i][1] and found == False:
			print("Nice guess!\n")
			correct_letters.append(letter)
			found = True
			for i in range (len(word)):
				if list_of_letters[0][i][0] != "-":
					secret_word[i] = list_of_letters[0][i][0]
					draw.draw_letters(i,letter)
					correct_guess += 1
	if found == False:
		for i in wrong_letters:
			if i == letter:
				dublicate = True
		for i in correct_letters:
			if i == letter:
				dublicate = True
		if dublicate:
			print("You have already guessed " +'"'+letter+'"\n')
		else:
			print("Sorry, there is no " +'"'+letter+'"\n')
			wrong_letters.append(letter)
			guesses -= 1
			draw.draw_wrong_letters(wrong_letters)
			draw.draw_hangman(guesses)
		dublicate = False
	for j in range(len(list_of_letters)):		
		for i in range (len(word)):
			list_of_letters[j][i][0] = "-" 
	found = False

# check if the player has won or lost		
if guesses > 0:
	print("Congragulations!")
	stdio.write("You guessed the secret word: ")
	for i in range (len(word)):
		stdio.write(list_of_letters[0][i][1])
else:
	print("You lose")
	stdio.write("You did not guess the secret word: ")
	for i in range (len(word)):
		stdio.write(list_of_letters[0][i][1])
stddraw.show()
