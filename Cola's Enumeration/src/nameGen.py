import time
import sys
import greekifier as gr
import parsers


DESCRIPTION = "show name of N'th zillion number"
ISOLATE = ['ni', 'mi', 'bi', 'tri', 'quadri', #nillion is not a number, so nilli can be used here 
           'quinti', 'sexti', 'septi', 'octi', 'noni']
CW_UNI = ['', 'un', 'duo', 'tre', 'quattuor', 'quin', 'se',
          'septe', 'octo', 'nove']  # quinqua is changed to quin
TEN = ['', 'deci', 'viginti', 'triginta', 'quadraginta', 'quinquaginta',
       'sexaginta', 'septuaginta', 'octoginta', 'nonaginta']
HUN = ['', 'centi', 'ducenti', 'trecenti', 'quadringenti',
       'quingenti', 'sescenti', 'septingenti', 'octingenti', 'nongenti']
#SIMP_UNI = ['', 'un', 'duo', 'tre', 'quattuor',
#            'quin', 'sex', 'septen', 'octo', 'novem']
PREC_TEN = ['', 'N', 'MS', 'NS', 'NS', 'NS', 'N', 'N', 'MX', '']
PREC_HUN = ['', 'NX', 'N', 'NS', 'NS', 'NS', 'N', 'N', 'MX', '']



def Apeironillion(n):
    #edge cases
    if (n < -1):
        return Apeironillion((n + 2) * -1) + "th"
    if (n == -1):
        return "" #one
    if (n == 0):
        return "thousand"
    if (n < 1000):
        return llion(n,True)

    #split number up into groups of three digits
    #Load repeats into arrays, forming a jagged array
    #take the length of each array and the first item of each array to make figs for the GreekGen
    #this is still O(n^2) but it should save ops over a substring search
    #Actually, just skip the jagged array and do a count instead

    #No more parsing long strings for contiguous repetiton
    #Still O(n^2) but we still save plenty of ops overall

    Figs = []
    out = ""
    dd = str(n)
    pipi = ""
    #print("len: " + str(len(dd)), "mod3: " + str(len(dd) % 3), "Str: " + dd)
    if (len(dd) % 3 == 0):
        pipi = str(n)
    if (len(dd) % 3 == 1):
        pipi = "00" + str(n)
    if (len(dd) % 3 == 2):
        pipi = "0" + str(n)
    
    dd = pipi
    s1 = dd[0:3]
    s2 = ""
    c = 0

    #print(dd)
    while(len(dd) > 0):
        s2 = dd[0:3]

        if (s1 == s2):
            c = c + 1
        else:
            Figs.append((c, int(s1)))
            c = 1
        dd = dd[3:]
       # print(dd)
        s1 = s2

    Figs.append((c, int(s1)))
    #print(dd, Figs)

    i = 0
    while (i < len(Figs) - 1):
       out += gr.GreekGen(Figs[i][0]) + llion(Figs[i][1], False) #For loop said "NO!"
       i = i + 1
    out += gr.GreekGen(Figs[i][0]) + llion(Figs[i][1], True)
    #print(out + "\n\n")
    return out




def llion(n, finalFlash = True):
    if n < 0:
        return 'N<0 is not defined'
    name = ''
    x = 0
    while n > 999:
        name = concat(n % 1000, name)
        n = n // 1000
        x =x + 1
        #print ("iteration " + str(x))
    name = concat(n, name, finalFlash)
    return name

#O(1)
def concat(n, suffix, finalFlash = True):
    result = base(n, finalFlash) + suffix
    if suffix == '' and finalFlash:
        result += 'lion'
    #print("base is " + result)
    return result

#O(1)
def base(n, finalFlash = True):
    name = ""
    if n < 10:
        return ISOLATE[n] + 'l'
    unit = n % 10
    ten = (n//10) % 10
    hun = n//100
    if ten == 0:
        prec = PREC_HUN[hun]
        if (unit > 0):
            name = CW_UNI[unit]
    else:
        prec = PREC_TEN[ten]

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

    if (not finalFlash):
        return name

    if (finalFlash):
        return name[:-1] + "i"








def GimmeNumber(innie = -1, short = True): #returns five ways to define the number
    if (innie != -1):
        name = Apeironillion(int(innie))
        tup = parsers.Engineerinify(innie, short, False)
        return (name, tup[0], tup[1]) #suffix, E, Sci


    else:
        parse = 0 #python likes this 

        while True:
            parse = parsers.parsertron(input("\nGive a number to illionize.\n> "))

            if (isinstance(parse, int)):
                time1 = time.time()
                name = Apeironillion(int(parse))
        
                print("---\nName:\none " + str(name) + "\n\n" + str(parsers.Engineerinify(parse, short)) + "\n---\n")
                
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


