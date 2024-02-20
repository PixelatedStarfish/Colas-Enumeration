#https://en.wikipedia.org/wiki/List_of_polygons
#https://benpittstoller.com/Misc/ManySidedShapes.html
DESCRIPTION = "This is more like a polygon of n sides generator"
ISOLATE = ["killo", "hena", "di", "tri", "tetra", "penta", "hexa", "hepta", "octa", "nona"] #not using ennea
CW_UNI = ['', 'un', 'do', 'tris', 'tetra', 'penta', 'hexa',
          'hepta', 'octa', 'nona']  
TEN =  ["", "deka", "cosi", "tricontakai", "tetracontakai", "pentacontakai", "hexacontakai", "heptacontakai", "octacontakai", "nonacontakai"] # I use "deka" to distinguish from deci
HUN = ["", "hecta", "dihecta", "trihectakai", "tetrahectakai", "pentahectakai", "hexahectakai", "heptahectakai","octahectakai", "nonahectakai"] # one hundred is technically hecto, but whatever...
PREC_TEN = ['', 'N', 'MS', 'NS', 'NS', 'NS', 'N', 'N', 'MX', '']
PREC_HUN = ['', 'NX', 'N', 'NS', 'NS', 'NS', 'N', 'N', 'MX', '']

METRIC = ['killo', 'mega', 'giga', 'tera', 'peta', 'exa', 'zetta', 'yotta', 'ronna', 'quetta'] #this is the easter egg zone, add as many prefixes as you want
MET_END = METRIC[len(METRIC) - 1]




#Fixed a bug I call the LuckyZero problem, a zero after a nonzero digit is still significant for place values.

#so... lets just take each digit and create tuples with the digit and the corresponding value of ten to put into a hash table 
def GreekGen(n):
    if (n > -1 and n < 21):
        ListOfAnnoyingExceptions = ["", "", "di", "tri", "tetra", "penta", "hexa", "hepta", "octa", "nona", "deka", "undeka", "dodeka", "trisdeka", "tetradeka", "pentadeka", "hexadeka", "heptadeka", "octadeka", "nonadeka", "cosa"]
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

    #supermetric
    if ((place // 3) - 1 < len(METRIC)):
        #print(place, (place // 3) - 1, metric[(place // 3) - 1], LuckyZero)
        if (place % 3 == 1):
            out += "deka" 
        if (place % 3 == 2):
            out += "hecta" 
        if (place % 3 == 0 or LuckyZero):
            out += METRIC[(place // 3) - 1]
    else: 

        p = place // 30

        if (p > 5):
            return GreekGen(10 ** (place % 30)) + "("+ str(p) + ")" + MET_END 
        if (p < 6):
            return GreekGen(10 ** (place % 30)) + MET_END * p

        #possibilities  
        #quetta, to killoquetta, to quettaquetta, killoquettaquetta, on and on (or run the number of quettas through the enumeration and drop the illion for wau_quetta, such that quettaquetta is waubiquetta, followed by wautriquetta and wauquadraquetta, up to waumilliquettaniquetta and even waumilliwaubiquettaniquetta)

    return out



def GetSmallestNonZeroDigitPlace(n):
    place = 1
    OmNom = len(str(n)) -1
    s = str(n)
    while (s[OmNom] == '0'):
        OmNom = OmNom - 1
        place = place + 1
    return place

def parsertron(s):


    s = s.replace(" ", "").replace(",", "").replace(".", "") # 1 222 = 1222 #This also protects us from abuse of the eval function; python code that needs a dot operator will not work!
    s = s.replace("^", "**") #for exponents

    #print("Interpretation: " + s.replace("**", "^"))
    try:
        ee = eval(s) #this runs python code!
        return ee 
    except Exception:
        return None


def GimmeNumber(innie = -1):
    try: 
        if (innie != -1):
            return GreekGen(int(innie))
        else:
            while True:
                f = parsertron(input("Give a number to greekify.\n> "))
                if f == "1":
                    return "henna"
                else:
                    print(GreekGen(f))
    except ValueError as ve:
        print("What is that? What's a '" + str(innie) + "'? That's a whole bunch of nothing! Goodbye!")


#This is bad practice but it's fine
def Engineerinify(n, printInfo = False):

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


if (__name__ == "__main__"):
        GimmeNumber(-1)