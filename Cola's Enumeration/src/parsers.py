#parsers for use by enumerators
def parsertron(s):

    s = s.replace(" ", "").replace(",", "").replace(".", "") # 1 222 = 1222 #This also protects us from abuse of the eval function; python code that needs a dot operator will not work!
    s = s.replace("^", "**") #for exponents

    #print("Interpretation: " + s.replace("**", "^"))
    try:
        return eval(s) #this runs python code! #It also gets slow around 10^10^4
    except Exception:
        return None

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
