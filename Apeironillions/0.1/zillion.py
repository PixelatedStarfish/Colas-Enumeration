import sys
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# zillion.py - show name of N'th zillion number
#
# Published at https://kyodaisuu.github.io/illion/
# For detailed explanation, see this site.
#
# Author: Fish https://googology.wikia.org/wiki/User:Kyodaisuu
# MIT license


# Hi Fish! I modded your converter to allow for made up numbers!
# "millinillinillinillion" is just hard to say.
#So I thought it was best to just call it something else!
#All "illinillinillinillions" can get a new name from a text file

#Have fun!

#FIXME:
#222222222222222222222222222222222 is still "duovigintiducentilli" repeated.
#related issues arise
#FIXME: zillinillion bug, 1 000 000 000 is a zillion but 1 000 000 000 000 is not zillinillion 
#NOTE: 1 000 000 000 000 000 000 000 000 000 outputs trazllionillion, not trazillion
#FIXME: inconsistant outputs in a loop of calls

#So I commented out the resetter function
#NOTE how 1 gives million, and 1000 gives millinillion
#when zillion is output, arrays are modifed, and not reset
#1 gives zillion
#1000 does not give zillinillion, but zillion
#The bug must be in the converter
#setting isomodIndex to -1 again has no effect

#FIXME cranky little converter aint doing shit now. Meh.

TXT_FILE = ""
CONVERTER = 1

DESCRIPTION = "show name of N'th zillion number"
ISOLATE = ['ni', 'mi', 'bi', 'tri', 'quadri',
           'quinti', 'sexti', 'septi', 'octi', 'noni']
CW_UNI = ['', 'un', 'duo', 'tre', 'quattuor', 'quin', 'se',
          'septe', 'octo', 'nove']  # quinqua is changed to quin
TEN = ['', 'deci', 'viginti', 'triginta', 'quadraginta', 'quinquaginta',
       'sexaginta', 'septuaginta', 'octoginta', 'nonaginta']
HUN = ['', 'centi', 'ducenti', 'trecenti', 'quadringenti',
       'quingenti', 'sescenti', 'septingenti', 'octingenti', 'nongenti']

SIMP_UNI = ['', 'un', 'duo', 'tre', 'quattuor',
            'quin', 'sex', 'septen', 'octo', 'novem']
PREC_TEN = ['', 'N', 'MS', 'NS', 'NS', 'NS', 'N', 'N', 'MX', '']
PREC_HUN = ['', 'NX', 'N', 'NS', 'NS', 'NS', 'N', 'N', 'MX', '']

isoModIndex = 0
isoMods = []


def llion(n, modified): #I do not know if modified does anything; it appears to be a bool with no effect
    if n < 1:
        return ''
    name = ''

    while n > 999:
        name = concat(n % 1000, name, modified)
        n = n // 1000
    name = concat(n, name, modified)
    return name


def concat(n, suffix, modified):
    result = base(n, modified) + suffix
    if suffix == '':
        result += 'on'
    return result


def base(n, modified):
    if n < 10:
        gt = ISOLATE[n]
        if (modified < 2):
            gt += "illi" #this just prevents what I'm calling "hanging illis" in the convert() function
        return gt
    unit = n % 10
    ten = (n//10) % 10
    hun = n//100

    if ten == 0:
        prec = PREC_HUN[hun]
    else:
        prec = PREC_TEN[ten]
    if modified:
        name = SIMP_UNI[unit]
    else:
        name = CW_UNI[unit]
        if unit == 3 or unit == 6:
            if 'S' in prec:
                name += 's'
            if 'X' in prec:
                if unit == 3:
                    name = 'tres'
                else:
                    name = 'sex'
        if unit == 7 or unit == 9:
            if 'M' in prec:
                name += 'm'
            if 'N' in prec:
                name += 'n'
    name += TEN[ten]
    name += HUN[hun]
    return name[:-1] + 'illi'  # Replace the final vowel


def getIllion(n): #sanitized inputs
    reseter()
    n = n.replace(" ", "")
    n = n.replace(",", "")
    n = n.replace(".", "")
    try: 
        n = int(n)

        
    except ValueError as ve:
        return "Not a numberillion!"


    #get output
    out = convert(n)

    return out

def convert(n, out = ""):
    global isoMods
    global isoModIndex
    global CONVERTER

    if (CONVERTER == 0 or n < (10 ** (9 * isoModIndex))):
        out = (llion(n,1)) #converter is off, or no further converting is needed (base case)

    else: 
        #neither recursion nor iteration are what I'd hoped
        #I think a partitioning strategy is more reliable

        #scan right to left
        #every nine digits gets a partition to itself
        #these partitions could be strings, which will need to be reversed
        #get illions and combine

        #start by reversing our n as a string and making a loop to generate partitions

        temp = ""
        c = 0
        #outticusFinch = []
        for i in str(n)[::-1]:
            temp += i
            c = c + 1
            if (c == 9):
                temp += " "
                c = 0
        partitions = temp.split(" ")
        c = 0
        temp = ""
        for i in partitions:
            i = i.strip() #CYA
            i = i[::-1]
            c = c + 1

            if (c > 0):
                reseter()
                try:
                    modILLINAMELISTS(isoMods[c - 2])
                except IndexError as ie:
                    return "plenty"
            temp = llion(int(i), 2).strip("\n").lower().replace("llion", "lli")
            #outticusFinch.append(temp.split("\n")[0])
            out = temp.split("\n")[0] + out
        #print(outticusFinch)
            
    return out.strip("on") + "on" #prevents onon 

    
def reseter():  #to normal
    global ISOLATE
    global TEN
    global HUN
    global isoModIndex 

    ISOLATE = ['ni', 'mi', 'bi', 'tri', 'quadri',
           'quinti', 'sexti', 'septi', 'octi', 'noni']
    TEN = ['', 'deci', 'viginti', 'triginta', 'quadraginta', 'quinquaginta',
       'sexaginta', 'septuaginta', 'octoginta', 'nonaginta']
    HUN = ['', 'centi', 'ducenti', 'trecenti', 'quadringenti',
       'quingenti', 'sescenti', 'septingenti', 'octingenti', 'nongenti']

    isoModIndex = 1


def powOfTenIllion(n):
    getIllion((n // 3) - 1)


def GimmeANumber(n = -1):
    if (n == -1):
        while True:
            print(getIllion(input("Give a positive integer to illionize.\n> ")))
            
    else:
        return getIllion(n)


        # undecicentilliundecicentilliundecicentillion (latin for 111 111 111)
        # repeats undecicentilli twice

def FindLongNumber(maxLen):
    n = 1
    while len(getIllion(str(n)))  < maxLen:
        n = n + 1
    illi = getIllion(str(n))
    print("max value within length " + str(maxLen) + " is \n\n" + illi + "\n\n" + str(n) + " 10^" + str(n * 3 + 3) + "\n\n") 
  
def RangeOfNumbers(a, b, c = 1):
    for i in range (a, b + 1, c):
        print(getIllion(str(i)))
        # undecicentilliundecicentilliundecicentillion (latin for 111 111 111)
        # repeats undecicentilli twice  

def modILLINAMELISTS(s):
    if (s == chr(7)):
        return #bail! It's a bug!

    global ISOLATE
    ISOLATE[1] = s
    
    ISOLATE[2] += s
    ISOLATE[3] += s
    ISOLATE[4] += s
    ISOLATE[5] += s
    ISOLATE[6] += s
    ISOLATE[7] += s
    ISOLATE[8] += s
    ISOLATE[9] += s

    global TEN
    TEN[1] += s
    TEN[2] += s
    TEN[3] += s
    TEN[4] += s
    TEN[5] += s
    TEN[6] += s
    TEN[7] += s
    TEN[8] += s
    TEN[9] += s

    global HUN
    HUN[1] += s
    HUN[2] += s
    HUN[3] += s
    HUN[4] += s
    HUN[5] += s
    HUN[6] += s
    HUN[7] += s
    HUN[8] += s
    HUN[9] += s
    
    return


def Table(a = 1, b = -1):
    a = a - 1
    global isoMods
    global TXT_FILE

    if (b == -1):
        b = 83 + len(isoMods)

    print("\nTABLE OF THE ILLIONS")
    print("\n(The table is in the range of "+ str(a + 1) + " to " + str(b) + "illions, and is using the file '" + TXT_FILE + "')")
    print()
    if (b < a or b < 0 or a < 0): 
        return "Cannot generate table in the range (+ "+ str(a + 1) + "," + str(b) + ")"
    try:
        Listy = '''
One Million                        10^6
One Billion                        10^9
One Trillion                       10^12
One Quadrillion                    10^15
One Quintillion                    10^18
One Sextillion                     10^21
One Septillion                     10^24
One Octillion                      10^27
One Nonillion                      10^30
One Decillion                      10^33
One Vigintillion                   10^63
One Trigintillion                  10^93
One Quadragintillion               10^123
One Quinquagintillion              10^153
One Sexagintillion                 10^183
One Septuagintillion               10^213
One Octogintillion                 10^243
One Nonagintillion                 10^273
One Centillion                     10^303
One Ducentillion                   10^603
One Trecentillion                  10^903
One Quadringentillion              10^1203
One Quingentillion                 10^1503
One Sescentillion                  10^1803
One Septingentillion               10^2103
One Octingentillion                10^2403
One Nongentillion                  10^2703
One Millinillion                   10^3003
One Billinillion                   10^6003
One Trillinillion                  10^9003
One Quadrillinillion               10^12003
One Quintillinillion               10^15003
One Sextillinillion                10^18003
One Septillinillion                10^21003
One Octillinillion                 10^24003
One Nonillinillion                 10^27003
One Decillinillion                 10^30003
One Vigintillinillion              10^60003
One Trigintillinillion             10^90003
One Quadragintillinillion          10^120003
One Quinquagintillinillion         10^150003
One Sexagintillinillion            10^180003
One Septuagintillinillion          10^210003
One Octogintillinillion            10^240003
One Nonagintillinillion            10^270003
One Centillinillion                10^300003
One Ducentillinillion              10^600003
One Trecentillinillion             10^900003
One Quadringentillinillion         10^1200003
One Quingentillinillion            10^1500003
One Sescentillinillion             10^1800003
One Septingentillinillion          10^2100003
One Octingentillinillion           10^2400003
One Nongentillinillion             10^2700003
One Millinillinillion              10^3000003
One Billinillinillion              10^6000003
One Trillinillinillion             10^9000003
One Quadrillinillinillion          10^12000003
One Quintillinillinillion          10^15000003
One Sextillinillinillion           10^18000003
One Septillinillinillion           10^21000003
One Octillinillinillion            10^24000003
One Nonillinillinillion            10^27000003
One Decillinillinillion            10^30000003
One Vigintillinillinillion         10^60000003
One Trigintillinillinillion        10^90000003
One Quadragintillinillinillion     10^120000003
One Quinquagintillinillinillion    10^150000003
One Sexagintillinillinillion       10^180000003
One Septuagintillinillinillion     10^210000003
One Octogintillinillinillion       10^240000003
One Nonagintillinillinillion       10^270000003
One Centillinillinillion           10^300000003
One Ducentillinillinillion         10^600000003
One Trecentillinillinillion        10^900000003
One Quadringentillinillinillion    10^1200000003
One Quingentillinillinillion       10^1500000003
One Sescentillinillinillion        10^1800000003
One Septingentillinillinillion     10^2100000003
One Octingentillinillinillion      10^2400000003
One Nongentillinillinillion        10^2700000003
        '''.split("\n")

        l = len(Listy)
        if (b < len(Listy)):
            l = b

        for i in range(a, l):
            print(Listy[i])

            if ((i % 9 == 0)):
                print()

        if (b >= len(Listy)):
            c = b - len(Listy)
            s = "One " + IllionVowelCorrect(isoMods[0].strip())
            print(s.title() + spaces(s, 35) + "10^(3(10^9)+3)")
            print("\n")
            
            n = 19
            for k in range(1, c):
                s = "One " + IllionVowelCorrect(isoMods[k].strip())
                print(s.title() + spaces(s, 35) + "10^(3(10^" + str(n) + ")+3)")
                n = 2 * n + 1
                if ((k % 9 == 0)):
                    print()

    except IndexError:
        pass
    print("END OF TABLE")

def spaces(s, const): #for use in table formatting
    
    spaces = (const - (len(s)))
    return " " * spaces

def IllionVowelCorrect(s): #no vowels before an illion suffix
    firsty = s.split("illion")[0]
    f = firsty[len(firsty) -1]
    if (f == 'a' or f == 'e' or f == 'i' or f == 'o' or f == 'u'):
        return firsty + "llion"
    return firsty + "illion"

def main():
    #init
    global isoMods
    global TXT_FILE
    global CONVERTER 

    try:
        f = open("Numbers/"+ sys.argv[1] + ".txt", "r")
        TXT_FILE = sys.argv[1]
        isoMods = f.readlines()
        f.close()
    except IndexError as ie: #use default file
        f = open("Numbers/zil.txt", "r")
        TXT_FILE = "zil.txt"
        isoMods = f.readlines()
        f.close()
    except FileNotFoundError as fnfe:
        if (sys.argv[1] == "OFF"):
            CONVERTER = 0
            print ("Zillion Converter disabled. Conway's Illion Converter will be run unmodified.")
        else:
            print("File 'Numbers/" + sys.argv[1] + "' not found.")

    isoMods.append(chr(7)) # this exists to squash a bug in converter
    #FindLongNumber(100)
    GimmeANumber()

main()
