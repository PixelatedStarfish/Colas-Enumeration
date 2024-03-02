import parsers

#https://en.wikipedia.org/wiki/List_of_polygons
#https://benpittstoller.com/Misc/ManySidedShapes.html
DESCRIPTION = "This is more like a polygon of n sides generator"
ISOLATE = ["killo", "hena", "di", "tri", "tetra", "penta", "hexa", "hepta", "octa", "nona"] #not using ennea
CW_UNI = ['', 'un', 'do', 'tris', 'tetra', 'penta', 'hexa',
          'hepta', 'octa', 'nona']  
TEN =  ["", "deka", "icosi", "tricontakai", "tetracontakai", "pentacontakai", "hexacontakai", "heptacontakai", "octacontakai", "nonacontakai"] # I use "deka" to distinguish from deci
HUN = ["", "hecta", "dihecta", "trihectakai", "tetrahectakai", "pentahectakai", "hexahectakai", "heptahectakai","octahectakai", "nonahectakai"] # one hundred is technically hecto, but whatever...
PREC_TEN = ['', 'N', 'MS', 'NS', 'NS', 'NS', 'N', 'N', 'MX', '']
PREC_HUN = ['', 'NX', 'N', 'NS', 'NS', 'NS', 'N', 'N', 'MX', '']

METRIC = ['killo', 'mega', 'giga', 'tera', 'peta', 'exa', 'zetta', 'yotta', 'ronna', 'quetta'] #this is the easter egg zone, add as many prefixes as you want
MET_END = METRIC[len(METRIC) - 1]




#Fixed a bug I call the LuckyZero problem, a zero after a nonzero digit is still significant for place values.

#so... lets just take each digit and create tuples with the digit and the corresponding value of ten to put into a hash table 
def GreekGen(n):
    if (n > -1 and n < 21):
        ListOfAnnoyingExceptions = ["", "", "di", "tri", "tetra", "penta", "hexa", "hepta", "octa", "nona", "deka", "undeka", "dodeka", "trisdeka", "tetradeka", "pentadeka", "hexadeka", "heptadeka", "octadeka", "nonadeka", "icosa"]
        #print(n, ListOfAnnoyingExceptions[len(ListOfAnnoyingExceptions)- 1])
        return ListOfAnnoyingExceptions[n] #no cluttering up my nice table
    s = str(n)

    i = 0
    out = ""
    L = len(s)
    while (i < L):
       LuckyZero = i < len(s) - 1 and s[i + 1] == "0"
       if (not s[i] == "0"):
           out += HashTable(int(s[i]), L - (i + 1), LuckyZero)
       i = i + 1
       if (LuckyZero):
        i = i + 1 #skip the zero to avoid an overcount
    return out
 

def HashTable(msd, place, LuckyZero = False): #place = log10(n)  #msd: most significant digit
    out = ISOLATE[msd]
    if (msd == 1):
        out = ""

    if (place == 2):
        return HUN[msd]
    if (place == 1):
        return TEN[msd]
    if (place == 0):
        return ISOLATE[msd] 

    #metric
    if ((place // 3) - 1 < len(METRIC)):
        if (not place % 3  == 0):
            out += GreekGen(msd * (10 * place)) 
        if (place % 3 == 0 or LuckyZero):
            out += METRIC[(place // 3) - 1]
    else: 

        return "apeiro"


        '''
        Implementing the rules in the readme is more trouble than is reasonable

        divmodConst = 3 * len(METRIC)
        p = place % divmodConst #place // 30
        q = place // divmodConst
        print((place // 3) - 1, place, divmodConst)
        
        return "working on it" #GreekGen(10 ** (place % divmodConst)) + MET_END * p
        #10 ^ 60 is quettaquetta
        
        #Notably 10^30 * 2 is diquetta, but 10^33 * 2 is not dikillioquetta
        #Also didekaquetta is not called cosaquetta
        #This is a bug!

        '''

    return out



def GetSmallestNonZeroDigitPlace(n):
    place = 1
    OmNom = len(str(n)) -1
    s = str(n)
    while (s[OmNom] == '0'):
        OmNom = OmNom - 1
        place = place + 1
    return place


def GimmeNumber(innie = -1):
    try: 
        if (innie != -1):
            return GreekGen(int(innie))
        else:
            while True:
                f = parsers.parsertron(input("Give a number to greekify.\n> "))
                if f == "1":
                    return "hena"
                else:
                    print(GreekGen(f))
    except ValueError as ve:
        print("What is that? What's a '" + str(innie) + "'? That's a whole bunch of nothing! Goodbye!")



if (__name__ == "__main__"):
        GimmeNumber(-1)