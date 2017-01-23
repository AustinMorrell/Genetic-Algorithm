import sys;
a = 0
b = 1
c = 0
d = 1
e = 0
parent1 = ""
parent2 = ""

def evaluation():

def geneticCross():

def main():
	
	counter = 0
	population = []
	population.append("")
	population.append("")
	population.append("")
	population.append("")
	population.append("")
	population.append("")
	Literals = ""
	file = open("CNF.txt")
	next = file.read(1)
	while next != "":
		if Literals.find(next) == -1:
			if next != '(' and next != 'V' and next != ')' and next != '&' and next != '?':
				Literals += next
		if next != '&':
			population[counter] += next
		if next == ')':
			counter += 1
		next = file.read(1)
	
	while !evaluation():
		geneticCross()

	print("The solution is " + a + " " + b + " " + c + " " + d + " " + e)
main()