import random

## Initialize the variables
k = 3 ### Number of moves to keep track of
A = [] ### Array of my moves
B = [] ### Array of AI's moves

def lexicon(i):
	if i==0:
		return "Rock"
	elif i ==1:
		return "Paper"
	elif i==2:
		return "Scissors"
	else:
		return -1
		
## Play the first three rounds to gain data
def start():
	print('Use 0 for Rock, 1 for Paper, 2 for Scissors')
	
	for i in range(k):
		A.append(input('What was your move? '))
		B.append(input('What was the computer\'s move? '))
	
	analysis(0)

## Start predicting against some patterns
def analysis(i):
	i %= len(A) ### Makes sure i doesn't grow greater than k
	
	if B[1]==B[2]:
		print ('Play ' + lexicon(B[1]) + ' next.')
		A[i] = B[1] 
	else:
		print ('Play ' + lexicon(random.randint(0,2)) + ' next.')	
	
	B[i] = input('What was the computer\'s move? ')
	i += 1
	analysis(i)
	
start()