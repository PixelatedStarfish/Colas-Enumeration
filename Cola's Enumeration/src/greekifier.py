#https://en.wikipedia.org/wiki/List_of_polygons
#https://benpittstoller.com/Misc/ManySidedShapes.html
DESCRIPTION = "This is more like a polygon of n sides generator"
ISOLATE = ["killo", "hena", "di", "tria", "tetra", "penta", "hexa", "hepta", "octa", "nona"] #not using ennea
CW_UNI = ['', 'un', 'do', 'tris', 'tetra', 'penta', 'hexa',
          'hepta', 'octa', 'nona']  
TEN =  ["", "deka", "cosi", "tricontakai", "tetracontakai", "pentacontakai", "hexacontakai", "heptacontakai", "octacontakai", "nonacontakai"] # I use "deka" to distinguish from deci
HUN = ["", "hecta", "dihecta", "trihectakai", "tetrahectakai", "pentahectakai", "hexahectakai", "heptahectakai","octahectakai", "nonahectakai"] # one hundred is technically hecto, but whatever...
PREC_TEN = ['', 'N', 'MS', 'NS', 'NS', 'NS', 'N', 'N', 'MX', '']
PREC_HUN = ['', 'NX', 'N', 'NS', 'NS', 'NS', 'N', 'N', 'MX', '']


#hennamillihennanillion is not a name; henna is redundant here.

#Fixed a bug I call the LuckyZero problem, a zero after a nonzero digit is still significant for place values.

#so... lets just take each digit and create tuples with the digit and the corresponding value of ten to put into a hash table 
def GreekGen(n):
    if (n > -1 and n < 21):
        ListOfAnnoyingExceptions = ["", "", "di", "tria", "tetra", "penta", "hexa", "hepta", "octa", "nona", "deka", "undeka", "dodeka", "trisdeka", "tetradeka", "pentadeka", "hexadeka", "heptadeka", "octadeka", "nonadeka", "cosa"]
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
    SUPER = 48 * 24
    out = ISOLATE[msd]
    if (msd == 1):
        out = ""

    #"Hash table" is just this. Forgive me. Doubled vowels are corrected for readability. Alpha is the sqaure of Yotta. The prefixes between quetta and alpha are for bridging the gap. Jana and Ortensia are based on "Jane" and "Hortensia". That easter egg based on a family story from when Papa was a toddler. (May Jane and Hortensia be glorified eternally). Conway and Wechsler are then honored. Finally, "kyoda" is named for the author of Conway's illion Converter   
    metric = ['killo', 'mega', 'giga', 'tera', 'peta', 'exa', 'zetta', 'yotta', 'ronna', 'quetta', 'jana', 'ortensa', 'conwa', 'wechsla', 'kyoda', 'alpha', 'killoalpha', 'megalpha', 'gigalpha', 'teralpha', 'petalpha', 'exalpha', 'zettalpha', 'yottalpha', 'ronnalpha', 'quettalpha', 'janalpha', 'ortensalpha', 'conwalpha', 'wechslalpha', 'kyodalpha', 'beta', 'killobeta', 'megabeta', 'gigabeta', 'terabeta', 'petabeta', 'exabeta', 'zettabeta', 'yottabeta', 'ronnabeta', 'quettabeta', 'janabeta', 'ortensabeta', 'conwabeta', 'wechslabeta', 'kyodabeta', 'gamma', 'killogamma', 'megagamma', 'gigagamma', 'teragamma', 'petagamma', 'exagamma', 'zettagamma', 'yottagamma', 'ronnagamma', 'quettagamma', 'janagamma', 'ortensagamma', 'conwagamma', 'wechslagamma', 'kyodagamma', 'delta', 'killodelta', 'megadelta', 'gigadelta', 'teradelta', 'petadelta', 'exadelta', 'zettadelta', 'yottadelta', 'ronnadelta', 'quettadelta', 'janadelta', 'ortensadelta', 'conwadelta', 'wechsladelta', 'kyodadelta', 'epsilon', 'killoepsilon', 'megaepsilon', 'gigaepsilon', 'teraepsilon', 'petaepsilon', 'exaepsilon', 'zettaepsilon', 'yottaepsilon', 'ronnaepsilon', 'quettaepsilon', 'janaepsilon', 'ortensaepsilon', 'conwaepsilon', 'wechslaepsilon', 'kyodaepsilon', 'zeta', 'killozeta', 'megazeta', 'gigazeta', 'terazeta', 'petazeta', 'exazeta', 'zettazeta', 'yottazeta', 'ronnazeta', 'quettazeta', 'janazeta', 'ortensazeta', 'conwazeta', 'wechslazeta', 'kyodazeta', 'eta', 'killoeta', 'megaeta', 'gigaeta', 'teraeta', 'petaeta', 'exaeta', 'zettaeta', 'yottaeta', 'ronnaeta', 'quettaeta', 'janaeta', 'ortensaeta', 'conwaeta', 'wechslaeta', 'kyodaeta', 'theta', 'killotheta', 'megatheta', 'gigatheta', 'teratheta', 'petatheta', 'exatheta', 'zettatheta', 'yottatheta', 'ronnatheta', 'quettatheta', 'janatheta', 'ortensatheta', 'conwatheta', 'wechslatheta', 'kyodatheta', 'iota', 'killoiota', 'megaiota', 'gigaiota', 'teraiota', 'petaiota', 'exaiota', 'zettaiota', 'yottaiota', 'ronnaiota', 'quettaiota', 'janaiota', 'ortensaiota', 'conwaiota', 'wechslaiota', 'kyodaiota', 'kappa', 'killokappa', 'megakappa', 'gigakappa', 'terakappa', 'petakappa', 'exakappa', 'zettakappa', 'yottakappa', 'ronnakappa', 'quettakappa', 'janakappa', 'ortensakappa', 'conwakappa', 'wechslakappa', 'kyodakappa', 'lambda', 'killolambda', 'megalambda', 'gigalambda', 'teralambda', 'petalambda', 'exalambda', 'zettalambda', 'yottalambda', 'ronnalambda', 'quettalambda', 'janalambda', 'ortensalambda', 'conwalambda', 'wechslalambda', 'kyodalambda', 'mu', 'killomu', 'megamu', 'gigamu', 'teramu', 'petamu', 'examu', 'zettamu', 'yottamu', 'ronnamu', 'quettamu', 'janamu', 'ortensamu', 'conwamu', 'wechslamu', 'kyodamu', 'nu', 'killonu', 'meganu', 'giganu', 'teranu', 'petanu', 'exanu', 'zettanu', 'yottanu', 'ronnanu', 'quettanu', 'jananu', 'ortensanu', 'conwanu', 'wechslanu', 'kyodanu', 'omicron', 'killoomicron', 'megaomicron', 'gigaomicron', 'teraomicron', 'petaomicron', 'exaomicron', 'zettaomicron', 'yottaomicron', 'ronnaomicron', 'quettaomicron', 'janaomicron', 'ortensaomicron', 'conwaomicron', 'wechslaomicron', 'kyodaomicron', 'pi', 'killopi', 'megapi', 'gigapi', 'terapi', 'petapi', 'exapi', 'zettapi', 'yottapi', 'ronnapi', 'quettapi', 'janapi', 'ortensapi', 'conwapi', 'wechslapi', 'kyodapi', 'rho', 'killorho', 'megarho', 'gigarho', 'terarho', 'petarho', 'exarho', 'zettarho', 'yottarho', 'ronnarho', 'quettarho', 'janarho', 'ortensarho', 'conwarho', 'wechslarho', 'kyodarho', 'sigma', 'killosigma', 'megasigma', 'gigasigma', 'terasigma', 'petasigma', 'exasigma', 'zettasigma', 'yottasigma', 'ronnasigma', 'quettasigma', 'janasigma', 'ortensasigma', 'conwasigma', 'wechslasigma', 'kyodasigma', 'tau', 'killotau', 'megatau', 'gigatau', 'teratau', 'petatau', 'exatau', 'zettatau', 'yottatau', 'ronnatau', 'quettatau', 'janatau', 'ortensatau', 'conwatau', 'wechslatau', 'kyodatau', 'upsilion', 'killoupsilion', 'megaupsilion', 'gigaupsilion', 'teraupsilion', 'petaupsilion', 'exaupsilion', 'zettaupsilion', 'yottaupsilion', 'ronnaupsilion', 'quettaupsilion', 'janaupsilion', 'ortensaupsilion', 'conwaupsilion', 'wechslaupsilion', 'kyodaupsilion', 'phi', 'killophi', 'megaphi', 'gigaphi', 'teraphi', 'petaphi', 'exaphi', 'zettaphi', 'yottaphi', 'ronnaphi', 'quettaphi', 'janaphi', 'ortensaphi', 'conwaphi', 'wechslaphi', 'kyodaphi', 'chi', 'killochi', 'megachi', 'gigachi', 'terachi', 'petachi', 'exachi', 'zettachi', 'yottachi', 'ronnachi', 'quettachi', 'janachi', 'ortensachi', 'conwachi', 'wechslachi', 'kyodachi', 'psi', 'killopsi', 'megapsi', 'gigapsi', 'terapsi', 'petapsi', 'exapsi', 'zettapsi', 'yottapsi', 'ronnapsi', 'quettapsi', 'janapsi', 'ortensapsi', 'conwapsi', 'wechslapsi', 'kyodapsi', 'omega', 'killoomega', 'megaomega', 'gigaomega', 'teraomega', 'petaomega', 'exaomega', 'zettaomega', 'yottaomega', 'ronnaomega', 'quettaomega', 'janaomega', 'ortensaomega', 'conwaomega', 'wechslaomega', 'kyodaomega']
    if (place == 2):
        return HUN[msd]
    if (place == 1):
        return TEN[msd]
    if (place == 0):
        return ISOLATE[msd] 
    
    #if place == (4):
    #    return out + "myria" #this is just hard to read, no thanks...

    #supermetric
    if ((place // 3) - 1 < len(metric)):
        #print(place, (place // 3) - 1, metric[(place // 3) - 1], LuckyZero)
        if (place % 3 == 1):
            out += "deka" 
        if (place % 3 == 2):
            out += "hecta" 
        if (place % 3 == 0 or LuckyZero):
            out += metric[(place // 3) - 1]
    else:
        greekAlphabet = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa", "lambda", "mu", "nu", "omicron", "pi", "rho", "sigma", "tau", "upsilion", "phi", "chi", "psi", "omega"]

        #there are fifteen metric prefixes inbetween each greek letter
        lenGR = len(greekAlphabet)
        SuperConst = (len(metric) // lenGR) * 72
        AnotherConst = ((place - SuperConst) // 48) 
        supreNum = (AnotherConst // 23) + 1 #should be superprefix number, which goes up by 1 each time we exceed omega 
        GrPlace = AnotherConst % (lenGR)  #this must always be in range of greekAlphabet. So this actually needs the modulo. Exceed omega means add 1 to superprefix and set this to 0
        #print(place, SuperConst, supreNum, greekAlphabet[GrPlace])
        return GimmeNumber(supreNum) + "wow" + greekAlphabet[GrPlace]







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