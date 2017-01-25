import sys;
from random import randint

#Legend
#V = 'or'
#r = 'not'
#& = 'and'

population = []
a = 0
b = 1
c = 0
d = 1
e = 0
parent1 = []
parent2 = []
temp = []
notDone = True
muteRate = 10

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
			if lastCount == 1:
			 b = not b
			if lastCount == 2:
			 c = not c
			if lastCount == 3:
			 d = not d
			if lastCount == 4:
			 e = not e
		lastCount += 1
	return 0

def crossEven():
	start = (len(parent1) / 2) - 1
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
	return 0

def crossOdd():
	start = int(round(len(parent2) / 2)) - 1
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
	return 0

def changeLiterals(L):
	lastCount = 0
	global a
	global b
	global c
	global d
	global e
	while lastCount < len(L):
		if lastCount == 0:
			 a = parent1[lastCount]
		if lastCount == 1:
			 b = parent1[lastCount]
		if lastCount == 2:
			 c = parent1[lastCount]
		if lastCount == 3:
			 d = parent1[lastCount]
		if lastCount == 4:
			 e = parent1[lastCount]
		lastCount += 1
	
def evaluation():
	for p in population:
		if eval(p) == 0:
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
	if len(L) % 2 != 0:
		crossOdd()
	return 0

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
		
	while evaluation() == False:
		for p in population:
			print(p)
		geneticCross(Literals)
		changeLiterals(Literals)
		Mutate(Literals)

	print("The solution is ")
	printCount = 0
	while printCount < len(Literals):
		if printCount == 0:
			 print(str(a))
		if printCount == 1:
			 print(str(b))
		if printCount == 2:
			 print(str(c))
		if printCount == 3:
			 print(str(d))
		if printCount == 4:
			 print(str(e))
		printCount += 1
main()