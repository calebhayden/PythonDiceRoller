import random

def parse_dice():
	print("Enter a dice roll in AdX+B format:")
	roll = input()
	valid = True
	numDice = 0
	diceSides = 0
	modifier = 0
	
	if roll.__contains__("d"):
		diceNums = roll.split("d")
		numDice = diceNums[0]
		diceSides = diceNums[1]
		if diceSides.__contains__("+"):
			diceSides.split("+")
			diceSides = int(diceSides[0])
		else:
			diceSides = int(diceNums[1])
		numDice = int(diceNums[0])		
	else:
		valid = False

	if roll.__contains__("+"):
		getModifier = roll.split("+")
		modifier = int(getModifier[1])


	if not valid:
		print("This is invalid, dummy")
		return
	
	total = 0
	index = 1
	random.seed()
	while numDice >= index:
		randInt = random.randint(1,diceSides)
		print(randInt)
		total += randInt
		index += 1

	total += modifier
	print("+", modifier)
	print("total",total)


while 1:
	parse_dice()	




