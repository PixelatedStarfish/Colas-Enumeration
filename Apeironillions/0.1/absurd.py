

def generateIllions(nameList):
	#this little guy generates a truly absurd number of illions using a name list and prefixes
	#the result is stored in RAM, not as a file.

	ones = ["", "mono", "di", "tria", "tetra", "penta", "hexa", "hepta", "octa", "ennea"] #the non prefix gets used alot already 
	tens = ["", "deca", "icosa", "conta", "conta", "conta", "conta", "conta", "conta", "conta"]
	hundreds = ["", "hecto", "hecta", "hecta", "hecta", "hecta", "hecta", "hecta","hecta", "hecta", "hecta"]
	thousands = ["", "chilia", "chilia", "chilia", "chilia", "chilia", "chilia", "chilia", "chilia", "chilia", "chilia"]
	#ten thousand is myriagon, not deca, icosa, or contachiliagon, a string replacement 
	
	#use the prefixes for polygons 
	#https://en.wikipedia.org/wiki/List_of_polygons

	#things get metric fpr the illion prefixes, each remains unchanged
	metric = ["", "mega", "giga", "tera", "peta", "exa", "zetta", "yotta", "ronna", "quetta"]

	#trisepatetracontahectachilazllinillion

	#you know what? rather than sticking these between new names, i think they come after 
	#instead of "plenty" you get monozillion
	#the out of range index gets the length of the isomod lis subtracted off
	#the remaining number goes in here, and a prefix is generated 
	#I can work out the kinks

	#in excess of the quettazillions, the monobazillions begin and so on, or mabye monos first, the dis, etc...

#takes too long
'''
	#r/ProgrammingHorror, call me a junior dev, put me in optimization jail, I'm on valium ffs
	bigOleList = []
	for i in nameList:
		bigOleList.append(i)
		for j in ones:
			bigOleList.append(j + i)
		for j in bigOleList:
			for k in tens:
				bigOleList.append(j.split(i)[0] + k + i)
			for k in hundreds:
				bigOleList.append(j.split(i)[0] + k + i)
			for k in thousands:
				bigOleList.append(j.split(i)[0] + k + i)

	print(bigOleList)
	'''

#"tria", "tetra", "penta", "hexa", "hepta", "octa", "ennea"
	for i in test:
		d = '''
		$
		mono$
		di$
		tria$
		tetra$
		penta$
		hexa$
		hepta$
		octa$
		ennea$
		deca$
		monodeca$
		dideca$
		triadeca$
		tetradeca$
		pentadeca$
		hexadeca$
		heptadeca$
		octadeca$
		enneadeca$
		icosa$
		#geenrate this as some text file

		'''

test = ["zillion", "bazillion", "trazillion"]
generateIllions(test)