# Karan Varindani
# karan301@bu.edu
# Rock Paper Scissors
# Predicts your next best move
# See README for more

## Import Python 3 Math to use Float for Division
from __future__ import division

## Initialize the array
## Uses 1 instead of 0 to more easily find percentage
A = [[1, 1], [1, 1], [1, 1]]

## Takes in an array position and returns the move type
def index(i):
	if i == 0:
		return "Rock"
	elif i == 1:
		return "Paper"
	elif i == 2:
		return "Scissors"
	else:
		return "Error"

## Increments the array of moves		
def add(input, identifier):
	if input=="R":
		move = 0 
	elif input=="P":
		move = 1 
	elif input=="S":
		move = 2
	else:
		move = -1
	A[move][identifier] += 1 

## Returns the most played move and its probability 	
def probability():
	P = []
	sum = 0 
	move = []
	
	for i in range(3):
		P.append(A[i][1])
	for i in range(3):
		sum += P[i]
	for i in range(3):
		P[i] = P[i]/sum
	
	move = [max(P), P.index(max(P))] 
	return move	

def main():
	print('Enter inputs in the form: R, P, or S')
	
	## Collects input from user
	## raw_input gets command line input as string
	move = raw_input('What did you play? ')
	rebuttal = raw_input('What did the AI play? ')
	
	add(move, 0)
	add(rebuttal, 1)
	
	## Print the next move
	print('Your next move should be ' + index(probability()[1]))
	
main()