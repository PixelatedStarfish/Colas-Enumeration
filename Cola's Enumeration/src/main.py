import nameGen
import table
import sys
import os
import time
import traceback
import greekifier
import illionConverter
import random
import tests
import parsers
from os import system, name

debug = False
short = True
MenuCount = 0 #this tracks the number of times the menu loads, for periodic screen clearing. 

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This is the Cola's Enumeration for naming large numbers. Based on Conway's illion Converter by Fish.
# 
# Author: AndrewJ (PixelatedStarfish) 
# Published on https://googology.fandom.com/wiki/User:PixelatedStarfish
# MIT license
#
# Conway's illion Converter is published at https://kyodaisuu.github.io/illion/
# For detailed explanation, see this site.
#
# Author: Fish https://googology.wikia.org/wiki/User:Kyodaisuu
# MIT license

def menu():
	global short
	global debug
	global MenuCount

		#get scale
	scale = "short"
	if (not short):
		scale = "long"


	print("\nWelcome to Cola's Enumeration for Naming Large Numbers by AndrewJ (PixelatedStarfish).\nThis program is a fork of Conway's illion Converter, by Fish (Kyoda).")
	choice = input("\nType a number to select an option:\n1. Play with Cola's Enumeration\n2. Play with Conway's illion Converter\n3. Table of Numbers\n4. What is this? (Read me)\n5. Change Scale" + " (" + scale  + ")\n6. Random Number\n7. Generate Cola's Series\n8. Generate illion Series\n9. Enumerations Comparison\n0. Close\n> ")

	#clear periodically (after an input is made)
	if (MenuCount > 5):
		clear()
		MenuCount = 0
	MenuCount = MenuCount + 1

	if choice == "1":
		nameGen.GimmeNumber(-1, short) #Run Cola's Enumeration
		return
	if choice == "2":
		illionConverter.main(short)
		return
	if choice == "3":
		table.make(short)
		return
	if choice == "4":
		readme = open("src/rm.txt", "r") 
		formatprint(readme.read())
		readme.close() 
		return
	if choice == "5":
		short = not short
		print("Scale changed")
		return
	if choice == "6":
		r = random.randint(1, 10 ** random.randint(1, 9) + 1)
		print("Generated: " + str(r) + "\n")
		p  = nameGen.GimmeNumber(r, short)
		formatprint(p[0] + "\n"  + p[1] + "\n" + p[2])
		return
	if choice == "7":
		miin = parsers.parsertron(input("Give a minimum illion at which to start.\n> "))
		maax = parsers.parsertron(input("Give a maximum illion at which to stop.\n> "))
		if (miin >= maax):
			print("No thanks.")

		for i in range(miin, maax + 1):
			print(i, nameGen.GimmeNumber(i, short)[0])
			time.sleep(.001)
		return
	if choice == "8":
		miin = parsers.parsertron(input("Give a minimum illion at which to start.\n> "))
		maax = parsers.parsertron(input("Give a maximum illion at which to stop.\n> "))
		if (miin >= maax):
			print("No thanks.")
			
		for i in range(miin, maax + 1):
			print(i, illionConverter.GimmeNumber(i, short)[0])
			time.sleep(.001)
		return
	if choice == "9":
		tests.main() #runs a comparison
		return
	if choice == "0":
		sys.exit()
		return
		
	if choice == "-2":
		print("Cola, the goodest boy <3")
		debug = not debug
		if (debug):
			print("Debug mode on")
		if (not debug):
			print("Debug mode off")
		return
	if choice == "-1":
		greekifier.GimmeNumber(-1)
		return
	else:
		print("\nPlease select an option, such as '1', '2', or '3'.")
 
# clear function (https://www.geeksforgeeks.org/clear-screen-python/#)
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')	

def formatprint(s):
	CONST = 68
	#this prevents words from being split over a line
	c = 0
	out = ""
	for i in s:
		if i == "\n":
			c = 0
		if (c > CONST and (i == " " or i == "-")):
			c = -1
			i = "\n"
		out += i
		c = c + 1
	print(out)

def main():
	try: 
		while True:
			menu()
	except Exception as e: 
		print("Error:\n" + str(e) + "\n")
		if (debug):
			traceback.print_exc()
		input("Press enter (return) to close.\n> ")

main()
