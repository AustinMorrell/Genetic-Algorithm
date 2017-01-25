import sys;
from random import randint

#Legend
#V = 'or'
#r = 'not'
#& = 'and'

population = []
a = 1
b = 1
c = 0
d = 1
e = 0
parent1 = []
parent2 = []
temp = []
notDone = True
muteRate = 50

def Mutate(L):
	if (randint(0, 100)) < muteRate:
		global a
		global b
		global c
		global d
		global e
		lastCount = 0
		while lastCount < int(round(len(L) / 2)) - 1:
			if lastCount == 0:
			 a = not a
			elif lastCount == 1:
			 b = not b
			elif lastCount == 2:
			 c = not c
			elif lastCount == 3:
			 d = not d
			elif lastCount == 4:
			 e = not e
		lastCount += 1

def crossEven():
	global parent1
	global parent2
	start = (len(parent1) / 2)
	tempCount = start
	while tempCount < len(parent1):
		temp[tempCount] = parent1[tempCount]
		tempCount += 1
	tempCount = start
	while tempCount < len(parent1):
		parent1[tempCount] = parent2[tempCount]
		parent2[tempCount] = temp[tempCount]
		tempCount += 1
	tempCount = start
	while tempCount < len(parent1):
		parent1[tempCount - start] = not parent1[tempCount]
		parent2[tempCount - start] = not parent2[tempCount]
		tempCount += 1

def crossOdd():
	global parent1
	global parent2
	start = int(round(len(parent1) / 2))
	tempCount = start
	while tempCount < len(parent1):
		temp[tempCount] = parent1[tempCount]
		tempCount += 1
	tempCount = start
	while tempCount < len(parent1):
		parent1[tempCount] = parent2[tempCount]
		parent2[tempCount] = temp[tempCount]
		tempCount += 1
	tempCount = start
	while tempCount < len(parent1):
		parent1[tempCount - start] = not parent1[tempCount]
		parent2[tempCount - start] = not parent2[tempCount]
		tempCount += 1

def changeLiterals(L):
	lastCount = 0
	global a
	global b
	global c
	global d
	global e
	global parent1
	global parent2
	print(parent1)
	while lastCount < len(L):
		if lastCount == 0:
			 a = parent1[lastCount]
		elif lastCount == 1:
			 b = parent1[lastCount]
		elif lastCount == 2:
			 c = parent1[lastCount]
		elif lastCount == 3:
			 d = parent1[lastCount]
		elif lastCount == 4:
			 e = parent1[lastCount]
		lastCount += 1
		
def changeLiterals2(L):
	lastCount = 0
	global a
	global b
	global c
	global d
	global e
	global parent1
	global parent2
	print(parent2)
	while lastCount < len(L):
		if lastCount == 0:
			 a = parent2[lastCount]
		elif lastCount == 1:
			 b = parent2[lastCount]
		elif lastCount == 2:
			 c = parent2[lastCount]
		elif lastCount == 3:
			 d = parent2[lastCount]
		elif lastCount == 4:
			 e = parent2[lastCount]
		lastCount += 1
	
def evaluation(L):
	changeLiterals(L)
	for p in population:
		if eval(p) == False:
			print("nope")
			break
	changeLiterals2(L)
	for p in population:
		if eval(p) == False:
			print("nope")
			return False
	print("yep")
	return True

def geneticCross(L):
	county = 0
	global notDone
	while county < len(L) and notDone:
		parent1.append(eval(L[county]))
		parent2.append(eval('not ' + L[county]))
		temp.append(0)
		county += 1
	notDone = False
	if len(L) % 2 == 0:
		crossEven()
	elif len(L) % 2 != 0:
		crossOdd()

def main():
	
	counter = 0
	Literals = ""
	file = open("CNF.txt")
	next = file.read(1)
	population.append("")
	while next != "":
		if Literals.find(next) == -1:
			if next != '(' and next != 'V' and next != ')' and next != '&' and next != 'r' and next != " ":
				Literals += next
		if next != '&' and next != 'V' and next != 'r':
			population[counter] += next
		if next == '&' and population[counter] != "":
			population[counter] += 'and'
		if next == 'V':
			population[counter] += 'or'
		if next == 'r':
			population[counter] += 'not '
		if next == ')':
			counter += 1
			if file.read(1) != "":
				population.append("")
		next = file.read(1)
		
	geneticCross(Literals)
	while evaluation(Literals) == False:
		for p in population:
			print(p)
		geneticCross(Literals)
		Mutate(Literals)

	print("The solution is ")
	printCount = 0
	while printCount < len(Literals):
		if printCount == 0:
			 print(str(a))
		elif printCount == 1:
			 print(str(b))
		elif printCount == 2:
			 print(str(c))
		elif printCount == 3:
			 print(str(d))
		elif printCount == 4:
			 print(str(e))
		printCount += 1
main()