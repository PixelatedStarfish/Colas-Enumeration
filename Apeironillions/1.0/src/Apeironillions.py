import stringEater
import time
import sys

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Apeironillions.py - extending Fish's zillions to new heights
#
#
# Published at https://github.com/PixelatedStarfish/Apeironillions
# For a detailed explanation, see the readme.
#
# Original Author: Fish https://googology.wikia.org/wiki/User:Kyodaisuu
# Mod Author: PixelatedStarfish
# MIT license


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


def noDoubVowels(s):
    #ee is ok
    s = s.replace("aa", "a")
    s = s.replace("ii", "i")
    s = s.replace("oo", "o")
    s = s.replace("uu", "u")
    s = s.replace("yy", "y")
    return s


def llion(n, modified = 0):
    if n < 1:
        return 'N<1 is not defined'
    name = ''
    while n > 999:
        name = concat(n % 1000, name, modified)
        n = n // 1000
    name = concat(n, name, modified)
    return noDoubVowels(stringEater.StringEater(name)) #this is my modification


def concat(n, suffix, modified):
    result = base(n, modified) + suffix
    if suffix == '':
        result += 'on'
    return result


def base(n, modified):
    if n < 10:
        return ISOLATE[n] + 'lli'
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


def parsertron(s):

    s = s.replace(" ", "").replace(",", "").replace(".", "") # 1 222 = 1222 #This also protects us from abuse of the eval function; python code that needs a dot operator will not work!
    s = s.replace("^", "**") #for exponents

    #print("Interpretation: " + s.replace("**", "^"))
    try:
        return eval(s) #this runs python code!
    except Exception:
        return None



def Engineerinify(n, printInfo = True):

    #added some (non extended) Hyper E Notation https://googology.fandom.com/wiki/Hyper-E_notation#Original_definition

    TEN_BILLION = 10 ** 10

    HyperE = 1

    while (n >= TEN_BILLION):
        n = n // TEN_BILLION
        HyperE = HyperE + 1

    e = str(3 * n +  3)
    ee = ""

   
    if HyperE > 1:
        ee = e + "#" + str(HyperE)

    if (printInfo):

        if (HyperE == 1):
            return "E Notation:\n1E" + str(e) + "\n\nExponentiation:\n10^" + str(e)

        if (HyperE > 1):
            return "Hyper E Notation:\n1E" + str(ee) + "\n\nTetration:\n" + "10^^" + str(HyperE) + "^" + str(e)
    else:
        if (HyperE == 1):
            return ("1E" + str(e), "10^" + str(e))
        if (HyperE > 1):
            return ("1E" + str(ee), "10^^" + str(HyperE) + "^" + str(e))




def GimmeNumber(innie = -1): #returns three ways to define the number
    if (innie != -1):
        name = llion(int(innie), 0)
        tup = Engineerinify(innie, False)
        return (name, tup[0], tup[1]) #suffix, E, Sci


    else:
        parse = 0 #python likes this 
        while True:
            parse = parsertron(input("\nGive a number to illionize.\n(illi(n) = 10^(3n + 3))\n> "))

            if (isinstance(parse, int)):
                time1 = time.time()
                print("---\nName:\none " + str(llion(parse, 0)) + "\n\n" + str(Engineerinify(parse)) + "\n---\n")
                time2 = time.time()
                timey = round(time2 - time1, 3)
                if (timey > 0):
                    print("Completed in " + str(timey) + " seconds")
            if parse == None:
                    print ("No thanks.")
                    return

def main():
    if len(sys.argv) < 2:
        GimmeNumber(-1)
    if len(sys.argv) == 2:
        GimmeNumber(int(sys.argv[1]))
if (__name__ == "__main__"):
    main()


#MegaPi = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989