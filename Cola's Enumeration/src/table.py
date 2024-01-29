

import nameGen as gimmeNumber
import tabulate as t
import time

DATA = []
col_names = ["I(n)", "Suffix", "e(#)", "Powers"]

def tableMakerTwo(a = 3, b = 63, c = 3, IncludeIllis = None):
    global DATA
    global col_names
    DATA = []
    tempList = []
    titleA = ""
    if not IncludeIllis == None:
        for i in IncludeIllis:
            tup = (gimmeNumber.GimmeNumber(10 ** i))
            tableRow(10 ** i, tup[0], tup[1], tup[2])
        titleA = "one " + gimmeNumber.GimmeNumber(10 ** IncludeIllis[0])[0].title()


    for i in range(a, b + 1, c):
        tempList.append(10 ** i)
    listTableMaker(titleA, tempList)

def listTableMaker(titleA, IncludeIllis = None):
    if titleA == "": 
        titleA = "one " + gimmeNumber.GimmeNumber(IncludeIllis[0])[0].title()
    titleB = "one " + gimmeNumber.GimmeNumber(IncludeIllis[len(IncludeIllis) -1])[0].title()

    for i in IncludeIllis:
        tup = (gimmeNumber.GimmeNumber(i))
        tableRow(i, tup[0], tup[1], tup[2]) 
    tablePrinter(titleA, titleB) 

def tableMakerOne(start = 1, length = 20 , step = 1, IncludeIllis = None):
    global DATA
    global col_names
    DATA = []

    titleA = "one " + gimmeNumber.GimmeNumber(start)[0].title()
    if (not IncludeIllis == None): #takes a list
        for i in IncludeIllis:
            tup = (gimmeNumber.GimmeNumber(i))
            tableRow(i, tup[0], tup[1], tup[2])
        titleA = "one " + gimmeNumber.GimmeNumber(IncludeIllis[0])[0].title()

        
    titleB = "one " + gimmeNumber.GimmeNumber(length)[0].title()



    for i in range(start, length  + 1, step):
        gimme = (i)
        tup = (gimmeNumber.GimmeNumber(gimme))
        tableRow(gimme, tup[0], tup[1], tup[2])

    tablePrinter(titleA, titleB)

     
     #Want to get the title centered. Store table in string, count the length of a line.  

def tablePrinter(titleA, titleB):
    global DATA
    global col_names

    TableTile = titleA.title() + " to " + titleB.title()
    TableToPrint = "\n" + t.tabulate(DATA, headers=col_names, tablefmt='rst', stralign='left') + "\n"

    TableTile = titleCenteringDevice(TableTile, TableToPrint)
    print("\n" + TableTile + "\n" + TableToPrint)


def illiTrunc(illi):

    if (len(str(illi)) > 6):
        return "10^" + str(len(str(illi)) -1) 
    return illi

    
def tableRow(illi, name, E, Sci):
    if (illi > 999 and str(illi)[len(str(illi)) -1] == "0"):
         illi = illiTrunc(illi)


    global DATA
    Listy = [illi, name, E, Sci]
    DATA.append(Listy)

def titleCenteringDevice(Title, Table): #can't find docs on this for tabulate
    halfTableRowLenInChars = len(Table.split("\n")[1]) // 2
    halfTitleLen = len(Title) // 2

    #print(halfTableRowLenInChars, halfTitleLen, halfTableRowLenInChars - halfTitleLen)

    if (halfTableRowLenInChars - halfTitleLen <= 0):
        return Title 

    return (" " * (halfTableRowLenInChars - halfTitleLen)) + Title









def make():

    s = '''
-Tables of Numbers-

Notes on the Tables:
I(n) = 10^(3n + 3) 

^ indicates exponentiation
^^ indicates repeated exponentiation (tetration)
e+ notates a power of 10
e# describes a tetration of 10 (as hyper e notation)
'''
    print(s)
    start= time.time()
    tableMakerOne(1, 20, 1)
    tableMakerOne(10, 100, 10, [1]) #curiosuly, the first tow two tables are formatted differently "e+06" instead of "e+6" 
    tableMakerOne(100, 1000, 100, [1])
    tableMakerOne(1000, 20000, 1000)
    tableMakerOne(10000, 100000, 10000, [1000])
    tableMakerOne(100 * 1000, 1000 ** 2, 100 * 1000, [1000])

    tableMakerTwo(3,60,3)
    tableMakerTwo(30,300,30, [3])
    tableMakerTwo(300,3000,300)
    end= time.time()

    resultTime = round(end - start, 3)
    print("Tables generated in " + str(resultTime) + " seconds.")

    #Larger tables take a long time to generate. evidently casting to string takes a long time!



if __name__ == "__main__": 
    make()







