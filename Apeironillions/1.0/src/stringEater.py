import sys
import greekifier
import re

'''
so 1.0 has a fatal flaw, it only shortens illions at powers of ten

1 000 000 000 is
millinillinillinillion
with converter off

and

zillion
with it on

BUT

1 222 222 222 illion is
milliduovigintiducentilliduovigintiducentilliduovigintiducentillion
with converter off

and 

zilliduovigintiducentilliduovigintiducentilliduovigintiducentillion

with it on. These names have the same length!


so a scheme is needed to abberviate consewcutive substrings

like 

1 000 000 000
is 
millitrianillion (using greek not latin prefixes, like naming a polygon)

millinillinillinillinillion becomes millitetranillion

(latin could still be okay so long as no name is used for two different illions)

let 'on' be added to the end of the trucated string, to indicate that 
'''




def ContiguousIlliCounter(s, truncations = 1):
	#contiguous substrings are always going to end in "illi" for zillions, so this should do exactly what I need it too. 
	
	t = s 
	s = truncateIllisFromStringStart(s, truncations) #chop the milli off "millinillinillinillinillinillinillinillinillinillinillinillinillinillinillinillinillinillinillinillinillinillion" and then  count the nillis
	if (t == s):
		return s # in this case, there is only one "illi" like in million, and this function is not needed

	mafongo = ""

	for i in s:
		mafongo += i

		if mafongo.endswith("illi"):
			break #egads!

	# the next step is to convert this tuple to a new string
	#why write nilli eight times, when you can just write "octanillion"
	#(going with greek prefixes), but these shortened strings will always end in "on" to indicate the end of the segment to which "octa" refers)
	#Adding one trillion to millioctanillion results in millioctanilliontrillion

	Fig = (mafongo, s.count(mafongo)) # i dub this tuple a fig just because

	return Fig




def FigTranslator(mafongo, count):
	return greekifier(count) + mafongo + "on"




#FIXME

#print("\n\n" + truncateIllisFromStringStart(sys.argv[1]))

#print ("_______________________________")

#print(ContiguousIlliCounter(sys.argv[1]))


#Had a better idea
#This is a function that eats illis and poops out fig tuples (to a list)



#If there is more than one illi, compare the first illi to the next.
	#If the two illis have a different prefix, bite off the first one and make a fig tuple
	#Otherwise, all contiguous identical illis get concatinated together and bitten off into a fig tuple

#A fig tuple consists of a substring as item 0, and a count of the illis as item 1

#If the string it eats only has one illi (no next illli), the illi gets put in a fig with a count of 1.

#Once out of illis to eat, poop out a list of fig tuples



#For each fig
	#if the fig has a count of one, take item 0, concat an 'on' to it. Done.
	#if the fig has a count more than 1
		#The  thing to do is run the count through the greekifier
		#this results in a prefix (such as di), (prefix + substring fig[0] + on) is what I call a figString
		#concatinate each figString together for our final result! 



def GimmeFirstIlli(s):
	if len(s) < 5:
		return None

	mafongo = ""
	i = 0
	while (not endsWithButItActuallyWorks(mafongo)):
		mafongo += s[i]
		i = i + 1

		#print(mafongo)

	if endsWithButItActuallyWorks(mafongo):
		return mafongo
	return None

def endsWithButItActuallyWorks(mafongo):
	#.endswith() is bizarre. "Triangle".endswith('angle') is false. Tri ends with angle. F

	if (len(mafongo) < 5):
		return False

	return mafongo[len(mafongo) - 4] == "i" and mafongo[len(mafongo) - 3] == "l" and mafongo[len(mafongo) - 2] == "l" and mafongo[len(mafongo) - 1] == "i"





def StringEater(s):
	Figs = []
	#base case
	if (s.count("illi") == 0 or s.count("illi") == 1):
		return s
	
	if (s.count("illi") > 1):
		Illis = GimmmeAllTheIllis(s)
		Figs = itsFigMakingTime(Illis)
		#print(Figs)
		outtie = ""
		for i in Figs:
			outtie += FigTranslator(i[0], i[1]) 

		if (outtie[len(outtie) - 1] != 'n'):
			outtie += "on"

		return outtie

def FigTranslator(mafongo, count):
	if count > 1:
		return greekifier.greekifier(count) + mafongo + "on"
	if count == 1:
		return mafongo

def itsFigMakingTime(Illis):
	i = 0;
	Figs = []

	counter = 1
	while i < len(Illis) - 1:
		if (Illis[i] == Illis[i + 1]):
			counter = counter + 1
		if (Illis[i] != Illis[i + 1]):
			Figs.append((Illis[i], counter))
			counter = 1
		i = i + 1
		
	Figs.append((Illis[i], counter))

	return Figs

			
		




def GimmmeAllTheIllis(s):
	total = s.count("illi")

	Illis = []

	appendME = ""
	c = 0

	while appendME != None:

		appendME = GimmeFirstIlli(s)
		if (not appendME == None):
			Illis.append(appendME)
			s = Truncate(len(Illis[c]), s)
		c = c + 1


	return(Illis)

def Truncate(i, s):
	out = ""

	while i < len(s):
		out += s[i]
		i = i + 1
	return out


if (__name__ == "__main__"):
	print(StringEater("millinillinillion"))
	#expected output:  millidinillion PASSED
	print(StringEater("millinillinillibillion"))
	#expected output:  millidinillionbillion
	print(StringEater("milliduovigintiducentilliduovigintiducentilliduovigintiducentillion"))
	#expected output:  millitriaduovigintiducentillion PASSED