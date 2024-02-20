#runnable illion converter
import time
import sys

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


def main(short):
    GimmeNumber(-1, short)


def llion(n, modified = False):
    if n < 1:
        return 'N<1 is not defined'
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

def Engineerinify(n, short, printInfo = True):

    #added some (non extended) Hyper E Notation https://googology.fandom.com/wiki/Hyper-E_notation#Original_definition

    TEN_BILLION = 10 ** 10

    HyperE = 1

    while (n >= TEN_BILLION):
        n = n // TEN_BILLION
        HyperE = HyperE + 1
    if short:
        e = str(3 * n +  3)
    if not short:
        e = str(6 * n)
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
            return ("1e+" + str(e), "10^" + str(e))
        if (HyperE > 1):
            return ("1e+" + str(ee), "10^^" + str(HyperE) + "^" + str(e))

def parsertron(s):

    s = s.replace(" ", "").replace(",", "").replace(".", "") # 1 222 = 1222 #This also protects us from abuse of the eval function; python code that needs a dot operator will not work!
    s = s.replace("^", "**") #for exponents

    #print("Interpretation: " + s.replace("**", "^"))
    try:
        return eval(s) #this runs python code! #It also gets slow around 10^10^4
    except Exception:
        return None


def GimmeNumber(innie = -1, short = True): #returns five ways to define the number
    if (innie != -1):
        name = llion(int(innie))
        tup = Engineerinify(innie, short, False)
        return (name, tup[0], tup[1]) #suffix, E, Sci


    else:
        parse = 0 #python likes this 

        while True:
            parse = parsertron(input("\nGive a number to illionize.\n> "))

            if (isinstance(parse, int)):
                time1 = time.time()
                name = llion(int(parse))
        
                print("---\nName:\none " + str(name) + "\n\n" + str(Engineerinify(parse, short)) + "\n---\n")
                
                time2 = time.time()
                timey = round(time2 - time1, 3)
               
                if (timey > 0):
                    print("Completed in " + str(timey) + " seconds")
           
            if parse == None:
                    print ("No thanks.")
                    return


if __name__ == "__main__":
    main()