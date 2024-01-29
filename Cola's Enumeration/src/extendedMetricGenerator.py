#This extends the metric system to an obscenely long set of prefixes.
m = ["killo", "mega", "giga", "tera", "peta", "exa", "zetta", "yotta", "ronna", "quetta", "jana", "ortensa", "conwa", "wechsla", "kyoda"] #the prefixes after quetta are easter eggs, I wanted each to have a unique starting letter (but I am still keeping kyoda and pesca)
greekAlphabet = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa", "lambda", "mu", "nu", "omicron", "pi", "rho", "sigma", "tau", "upsilion", "phi", "chi", "psi", "omega"]


out = [] #this used to be out = m; which is evil because reasons...

for i in m: #we need this because we do, not bothering with how to deep copy for a list.
    out.append(i)

z = 0
for i in greekAlphabet:
    z = z + 1
    out.append(i)
    for j in m:
        z = z + 1
        s = j + i
        s = s.replace("aa", "a")
        s = s.replace("ii", "i")
        s = s.replace("uu", "u")
        s = s.replace("yy", "y")
        out.append(s)
        print(str(z) + "/" + str(len(m) * len(greekAlphabet))) #these debug statements are nessecary...
    if (z > 500):
        print ("Python, what are you doing?") #see rant on line 33
        break

print(out)










# excuse me for a moment...

#DID YOU KNOW PYTHON PASSES ARRAYS (sorry, lists) BY REFERENCE. I DID NOT! 
#I SET OUT TO M SO OUT WOULD BEGIN WITH METRIC PREFIXES, NOT SO OUT WOULD POINT TO M.
#I WAS JUST SITTING THERE, TRYING TO FIGURE OUT HOW FOR LOOPS COULD POSSIBLY PRODUCE AN INFINITE LOOP
#WHEN MY LOOP APPENDED A VALUE TO OUT, IT WAS ACTUALLY APPENDING IT TO M, OUT WAS JUST A POINTER.
#THEN M WOULD GROW AND THE LOOP WOULD CONTINUE FOR EACH ITEM IN M!

#And that was how I got my first bsod... F

#I'm seriously considering just doing everything in C now... even if the memory management is manual