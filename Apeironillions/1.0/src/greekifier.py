#https://en.wikipedia.org/wiki/List_of_polygons

DESCRIPTION = "This is more like a polygon of n sides generator"
ISOLATE = ["killo", "mono", "di", "tria", "tetra", "penta", "hexa", "hepta", "octa", "ennea"]
CW_UNI = ['', 'un', 'do', 'triskai', 'tetrakai', 'pentakai', 'hexakai',
          'heptakai', 'octakai', 'enneakai']  
TEN =  ["", "deka", "icosa", "triconta", "tetraconta", "pentaconta", "hexaconta", "heptaconta", "octaconta", "enneaconta"]
HUN = ["", "hecto", "dihecta", "trihecta", "tetrahecta", "pentahecta", "hexahecta", "heptahecta","octahecta", "enneahecta"]
SIMP_UNI = ['', 'un', 'do', 'triskai', 'tetrakai', 'pentakai', 'hexakai',
          'heptakai', 'octakai', 'enneakai']
PREC_TEN = ['', 'N', 'MS', 'NS', 'NS', 'NS', 'N', 'N', 'MX', '']
PREC_HUN = ['', 'NX', 'N', 'NS', 'NS', 'NS', 'N', 'N', 'MX', '']



def greekifier(n, modified = 1):
    if n < 1:
        return 'N<1 is not defined'
    name = ''
    while n > 999:
        name = concat(n % 1000, name, modified)
        n = n // 1000
    name = concat(n, name, modified)
    name = name.replace("monokillo", "killo")

    #10,000's
    name = name.replace("dekkillo", "myria")
    name = name.replace("icoskillo", "dimyria")
    name = name.replace("tricontkillo", "trimyria")
    name = name.replace("tetracontkillo", "tetramyria")
    name = name.replace("pentacontkillo", "pentamyria")
    name = name.replace("hexacontkillo", "hexamyria")
    name = name.replace("heptacontkillo", "heptamyria")
    name = name.replace("octacontkillo", "octamyria")
    name = name.replace("enneacontkillo", "enneamyria")

    #100,000's
    name = name.replace("hectkillo", "decamyria")
    name = name.replace("dihectkillo", "icosamyria")
    name = name.replace("trihectkillo", "tricontamyria")
    name = name.replace("tetrahectkillo", "tetracontamyria")
    name = name.replace("pentahectkillo", "pentacontamyria")
    name = name.replace("hexahectkillo", "hexacontamyria")
    name = name.replace("heptahectkillo", "heptacontamyria")
    name = name.replace("octahectkillo", "octacontamyria")
    name = name.replace("enneahectkillo", "enneacontamyria")

    #metric
    name = name.replace("killokillo", "mega")
    name = name.replace("megakillo", "giga")
    name = name.replace("megamega", "tera")
    name = name.replace("megagiga", "peta")
    name = name.replace("teramega", "exa")
    name = name.replace("teragiga", "zetta")
    name = name.replace("teratera", "yotta")
    name = name.replace("terapeta", "ronna")
    name = name.replace("teraexa", "quetta")

    #ultra metric (the only ones that actually matter are the doublings)
    name = name.replace("yottayotta", "alpha")
    name = name.replace("alphaalpha", "beta")
    name = name.replace("betabeta", "gamma")
    name = name.replace("gammagamma", "delta")
    name = name.replace("deltadelta", "epsilon")
    name = name.replace("epsilonepsilon", "zeta")
    name = name.replace("zetazeta", "eta")
    name = name.replace("etaeta", "theta")
    name = name.replace("thetatheta", "iota")
    name = name.replace("iotaiota", "kappa")
    name = name.replace("kappakappa", "lambda")
    name = name.replace("lambdalambda", "mu")
    name = name.replace("mumu", "nunu")
    name = name.replace("nunu", "xixi")
    name = name.replace("xixi", "omicron")
    name = name.replace("omicronomicron", "pi")
    name = name.replace("pipi", "rho")
    name = name.replace("rhorho", "sigma")
    name = name.replace("sigmasigma", "tau")
    name = name.replace("tautau", "upsilion")
    name = name.replace("upsilionupsilion", "phi")
    name = name.replace("phiphi", "chi")
    name = name.replace("chichi", "psi")
    name = name.replace("psipsi", "omega")
    #I know I could have used an array and loop, nfg















    return name


'''
    #yotta repeats alotta
    name = name.replace("yottayotta", "chilla")
    name = name.replace("chillachilla", "ultra")
    name = name.replace("ultraultra", "supa")
    name = name.replace("supasupa", "dupa")
    name = name.replace("dupadupa", "outta")
    name = name.replace("outtaoutta", "conwa")
    name = name.replace("conwaconwa", "wechsla")
    name = name.replace("wechslawechsla", "kyoda")
    #anachyChess
    name = name.replace("kyodakyoda", "passa")
    name = name.replace("passapassa", "olela")
    name = name.replace("olelaolela", "respa")
    name = name.replace("resparespa", "actua")
    name = name.replace("actuaactua", "cista")
    name = name.replace("cistacista", "bisha")
    name = name.replace("bishabisha", "knighta")
    name = name.replace("knightaknighta", "storma")
    name = name.replace("stormastorma", "crifa")
    name = name.replace("crifacrifa", "ignia")
    name = name.replace("igniaignia", "matea")
    name = name.replace("mateamatea", "domina")
    name = name.replace("dominadomina", "tigra")
'''



def concat(n, suffix, modified):
    result = base(n, modified) + suffix
    return result


def base(n, modified):
    if n < 10:
        return ISOLATE[n]
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
                    name = 'tria'
                else:
                    name = 'hexa'
        if unit == 7 or unit == 9:
            if 'M' in prec:
                name += 'm'
            if 'N' in prec:
                name += 'n'
    name += TEN[ten]
    name += HUN[hun]
    return name[:-1]

def parsertron(s):

    s = s.replace(" ", "").replace(",", "").replace(".", "") # 1 222 = 1222 #This also protects us from abuse of the eval function; python code that needs a dot operator will not work!
    s = s.replace("^", "**") #for exponents

    #print("Interpretation: " + s.replace("**", "^"))
    try:
        return eval(s) #this runs python code!
    except Exception:
        return None


def GimmeNumber(innie = -1):
    try: 
        if (innie != -1):
            return greekifier(int(innie), 1)
        else:
            while True:
                print(greekifier(parsertron(input("Give a number to greekify.\n> ")), 1))
    except ValueError as ve:
        print("What is that? What's a '" + str(innie) + "'? That's a whole bunch of nothing! Goodbye!")

if (__name__ == "__main__"):
        GimmeNumber(-1)



