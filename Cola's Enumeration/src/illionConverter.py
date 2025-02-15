#runnable illion converter
import time
import sys
import parsers

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


def main(short = True):
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



def GimmeNumber(innie = -1, short = True): #returns five ways to define the number
    if (innie != -1):
        name = llion(int(innie))
        tup = parsers.Engineerinify(innie, short, False)
        return (name, tup[0], tup[1]) #suffix, E, Sci


    else:
        parse = 0 #python likes this 

        while True:
            parse = parsers.parsertron(input("\nGive a number to illionize.\n> "))

            if (isinstance(parse, int)):
                time1 = time.time()
                name = llion(int(parse))
        
                print("---\nName:\none " + str(name) + "\n\n" + str(parsers.Engineerinify(parse, short)) + "\n---\n")
                
                time2 = time.time()
                timey = round(time2 - time1, 3)
               
                if (timey > 0):
                    print("Completed in " + str(timey) + " seconds")
           
            if parse == None:
                    print ("No thanks.")
                    return


if __name__ == "__main__":
    main()