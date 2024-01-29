import nameGen
import table
import sys
import os

from os import system, name
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This is the Cola's Enumeration for naming large numbers. Based on Conway's illion Converter by Fish.
# 
# Author: PixelatedStarfish https://googology.fandom.com/wiki/User:PixelatedStarfish
# Published on github at https://github.com/PixelatedStarfish/Apeironillions
# MIT license
#
# Conway's illion Converter is published at https://kyodaisuu.github.io/illion/
# For detailed explanation, see this site.
#
# Author: Fish https://googology.wikia.org/wiki/User:Kyodaisuu
# MIT license

def menu():
	print("\nCola's Enumeration for Naming Large Numbers, by PixelatedStarfish.\nBased on Conway's illion Converter, by Fish.")
	choice = input("\nType a number to select an option:\n1. Play with Cola's Enumeration\n2. Play with Conway's illion Converter\n3. Table of Numbers\n4. Readme\n5. Clear Screen\n6. Close\n> ")

	if choice == "1":
		nameGen.GimmeNumber(-1, True) #Run Cola's Enumeration
		return
	if choice == "2":
		nameGen.GimmeNumber(-1, False) #Run Conway's illion Converter
		return
	if choice == "3":
		table.make()
		return
	if choice == "4":
		readme = open("src/rm.txt", "r") 
		formatprint(readme.read())
		readme.close() 
		return
	if choice == "5":
		clear()
		return
	if choice == "6":
		sys.exit()
		return
	if choice == "8":
		print("The current working dir is " + os.getcwd())
		return
	if choice == "0":
		print("Cola, the goodest boy <3")
		return
	if choice == "9":
		c = 1 // 0
		print(c)
		return
	else:
		print("\nPlease select an option, such as '1', '2', or '3'.")
 
# define our clear function (https://www.geeksforgeeks.org/clear-screen-python/#)
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
		if (c > CONST and i == " "):
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
		input("Press enter (return) to close.\n> ")

main()
