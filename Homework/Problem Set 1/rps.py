Me = [0, 0, 0]
AI = [0, 0, 0]
		
def sort(input, identifier):
	if identifier == 0:
		array = Me
	else:
		array = AI
	
	if input=="R":
		array[0] += 1 
	elif input=="P":
		array[1] += 1 
	else:
		array[2] += 1 


def main():
	print('Enter inputs in the form: R, P, or S')
	
	move = input('Input your move:')
	rebuttal = input('What did the computer do?')
	
	sort(move, 0)
	sort(rebuttal, 1)
			
	print(Me)
	print(AI)
	
main()