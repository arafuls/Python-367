import sys
import time

def LD(S, T):
	rows = len(S) + 1
	cols = len(T) + 1
	D = [[0 for x in range(cols)] for x in range(rows)]
	E = [[0 for x in range(cols)] for x in range(rows)]

	#print obtained strings
	print("Input Sequences")
	print("----------------------------")
	print(S); print(T)
	print("----------------------------")

	#priming empty lists/matrices
	for i in range(1, rows): D[i][0] = i
	for i in range(1, cols): D[0][i] = i
	for i in range(1, rows): E[i][0] = i
	for i in range(1, cols): E[0][i] = i

	#levenshtein distance algorithm
	for i in range(1, rows):
		for j in range(1, cols):
			deletion 	 = D[i-1][j]   + 1										#upper
			insertion 	 = D[i]  [j-1] + 1										#left
			substitution = D[i-1][j-1] + (0 if S[i - 1] == T[j - 1] else 1)		#diagonal

			#recording edits made into matrix E[][]
			smallest = min(deletion, insertion, substitution)
			if   smallest == deletion: 		E[i][j] = 1	#record deletion
			elif smallest == insertion: 	E[i][j] = 2 #record insertion
			elif smallest == substitution:  E[i][j] = 0 #record substitution

			#record minimum distance into matrix D[][]
			D[i][j] = smallest

	#creating modified sequences S_RESULT and T_RESULT
	S_RESULT = list()
	T_RESULT = list()
	i = rows-1
	j = cols-1

	max = 0
	if rows > cols:
		max = rows
	elif cols > rows:
		max = cols

	#backtracing to enter char (backwards) into RESULT based on operation previously used
	while i > 0 and j > 0:
		if E[i][j] == 0:	#if substitution
			S_RESULT.insert(0, S[i-1])
			T_RESULT.insert(0, T[j-1])
			if i > 0: i-=1
			if j > 0: j-=1
		elif E[i][j] == 1:	#if deletion
			S_RESULT.insert(0, S[i-1])
			T_RESULT.insert(0, '-')
			if i > 0: i-=1
		elif E[i][j] == 2:	#if insertion
			S_RESULT.insert(0, '-')
			T_RESULT.insert(0, T[j-1])
			if j > 0: j-=1

	print("Aligned Sequences")
	print("----------------------------")
	print(S_RESULT); print(T_RESULT)
	print("----------------------------")
	print("The minimum edit distance is", D[rows-1][cols-1])

#####################################################################

start_time = time.time()

if len(sys.argv) > 1:
	file1 = open(sys.argv[1], "r")
	file2 = open(sys.argv[2], "r")
	contents1 = file1.read()
	contents2 = file2.read()
	file1.close()
	file2.close()
	LD(contents1, contents2)

print("Completed in", round(time.time() - start_time, 4), "seconds.")