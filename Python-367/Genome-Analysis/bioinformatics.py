''' generates 100 random motifs, searches each random motif
    for matches and returns average match probability       '''
def genRandCmpAvgs(N):
    count = 0
    l = []
    while count != 100:
        rand_motif = genRandMotif(a_freq, t_freq, g_freq, c_freq, N)
        match = patCount(rand_motif, motif)
        l.append(match)
        count += 1
    return sum(l)/len(l)

''' searches a motif for a pattern
    returns number of occurences    '''
def patCount(motif, pattern):
    count = 0
    start = 0
    flag = True
    while flag:
        pat = motif.find(pattern, start)
        if pat == -1:
            flag = False
        else:
            count += 1
            start = pat + 1
    return count

''' generates and returns a random motif of size N '''
def genRandMotif(A, T, G, C, N):
    rand_motif = ""
    count = 0
    while count != N:
        r_num = random.random() * 100
        if   r_num < A: rand_motif += 'A'
        elif r_num >= A and r_num < (A + T): rand_motif += 'T'
        elif r_num >= (A + T) and r_num < (A + T + G): rand_motif += 'G'
        elif r_num >= (A + T + G): rand_motif += 'C'
        count += 1
    return rand_motif
  
''' calcualtes probability based on nucleotides occurances '''
def calcProbability(motif):
    P = int(1)
    for x in range(0, motif.count('A')): P *= (a_freq / 100)
    for x in range(0, motif.count('T')): P *= (t_freq / 100)
    for x in range(0, motif.count('G')): P *= (g_freq / 100)
    for x in range(0, motif.count('C')): P *= (c_freq / 100)    
    return P

###############################################################################
import matplotlib.pyplot as plt
import random

validInput = "ATCG"
while True:
	motif = input("Motif: ")
	motif = motif.upper()
	if all(c in validInput for c in motif) == False:
		print("Invalid character found.")
	else: break
N = len(motif)
    
# Nucleobase Frequencies
print("Enter frequencies for each Nucleobase (0-100):")
while True:
	a_freq = int(input("A = "))
	t_freq = int(input("T = "))
	g_freq = int(input("G = "))
	c_freq = int(input("C = "))
	sum_freq = a_freq + t_freq + g_freq + c_freq 
	if   a_freq < 0 or a_freq > 100:   print("Invalid percentage")
	elif t_freq < 0 or t_freq > 100:   print("Invalid percentage")
	elif g_freq < 0 or g_freq > 100:   print("Invalid percentage")
	elif c_freq < 0 or c_freq > 100:   print("Invalid percentage")
	elif sum_freq != 100:              print("Total percentage does not equal 100%.")
	else: break

# Calculating Probability
P = calcProbability(motif)

# Graph 1
print("Probability of appearing in a sequence N =", N, "is", P, "(", P * 100,"%)")
plt.figure(1)
axes = plt.gca()
axes.set_ylim([0,1])
axes.set_xlim([0,5000])
probability_list = []
for i in range(N, 5000):
    probability_list.append(1-(1-P)**i)
plt.plot(probability_list, 'b')
plt.ylabel('Probability of Finding at Least One of These Motifs')
plt.xlabel('Sequence Length')
plt.show()

# Graph 2
print("Expected number of motifs in sequences of length N = 100, N = 1000, N = 2000, N = 5000, and N = 10000")
plt.figure(2)
axes = plt.gca()
axes.set_ylim([0,45])
axes.set_xlim([0,10000])
m_size = 35
m_outline = 1
plt.plot(100,   genRandCmpAvgs(100),   'ro', markersize=m_size, markeredgewidth=m_outline, markeredgecolor='black')
plt.plot(1000,  genRandCmpAvgs(1000),  'ro', markersize=m_size, markeredgewidth=m_outline, markeredgecolor='black')
plt.plot(2000,  genRandCmpAvgs(2000),  'ro', markersize=m_size, markeredgewidth=m_outline, markeredgecolor='black')
plt.plot(5000,  genRandCmpAvgs(5000),  'ro', markersize=m_size, markeredgewidth=m_outline, markeredgecolor='black')
plt.plot(10000, genRandCmpAvgs(10000), 'ro', markersize=m_size, markeredgewidth=m_outline, markeredgecolor='black')
plt.ylabel('Expected number of motifs in sequences')
plt.xlabel('Sequence Length')
plt.show()