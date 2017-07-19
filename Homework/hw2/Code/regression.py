# Karan Varindani
# karan301@bu.edu
# Machine Learning
# Problem Set 2

import numpy as np
import scipy.io as sio
import math

## Index of columns (without given FTP and WE)
vars = ["UEMP", "MAN", "LIC", "GR", "NMAN", "GOV", "HE"]

def regression():
	## Read in (and strip for) Matlab data
	extract = sio.loadmat('../Others/detroit.mat')
	data = extract['data']
	
	matrix = []
	
	vector = []
	for i in range(len(data)):
		vector.append(data[i][-1])
	vector = np.array(vector)
	
	## Format array for numpy
	for k in range(1,8):
		temp = []
		for i in range(len(data)):
			row = []
			row.append(data[i][0])
 			row.append(data[i][8])
 			row.append(data[i][k])
			temp.append(row)
		matrix.append(temp)
	
	errors = []
	for i in range(7):
		X = np.array(matrix[i]) ### Let x be the design matrix
		
		phi = [0.0, 0.0, 0.0]
		t = 0.0
		for j in range(len(X)):
 			phi += X[j]
			t += vector[j]
		## Get the average
		phi /= len(X) 
		t /= len(vector)
		
		weights = ((np.linalg.inv((X.T).dot(X))).dot(X.T)).dot(vector)
		
		result = 0.0
		for j in range(len(phi)):
			result += weights[j]*phi[j]
		w0 = t - result
		
		loss = 0.0
		for n in range(len(X)):
			third = (weights.T).dot(X[n])
			loss += (vector[n] - w0 - third) ** 2
		loss /= 2
		errors.append(loss)
	
	## Print the column with the least errors
	best = errors.index(min(errors))
	print("The third variable is " + vars[best])
	
regression()
