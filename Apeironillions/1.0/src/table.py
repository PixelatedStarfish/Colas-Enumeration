# I want to optimize this thing, less parsing and more hash maps 
#Don't reconstruct "million" every time, from a table of prefixes
#Look up  "million" or "millideknillion" in the hash table(s)
#parsing can be used after lookup to add the un to undecillion or whatever
#fill in what gaps there may be


#For this version, my goal is to print tables for a person to read, as a reference.


#these functions need a refactoring. Here is the goal

'''
 Table 1 - 20; step = 1
    million
    billion
    ...
    vingintillion

Table 1 - 100; step = 10
    million
    decillion
    ...
    centillion

Table 1 - 1000; step = 100
    million
    centillion
    ...
    millinillion


#This table introduces the greek modifiers and is a deviation
    millinillion
    dimillion
    triamillion

Do the three tables again, with all values raised by 10^3

Table 1000 - 20 000; step = 1000
    millinillion
    billinillion
    ...
    vingintinillion

Table 1000 - 100 000; step = 10 000
    millinillion
    decinillion
    ...
    centillinillion

Table 1 - 1 000 000; step = 100 000
    million
    centillinillion
    ...
    millidinillion

# this table deviates to demonstrate counting millions after millidinillion
    millidinillion
    millinillimillion
    millinillibillion
    ...
    millinillivingintillion

Table 1 - (10 ^(3 * 20)); step = 10^(3 * n); n = n + 1
    million
    millinillion
    millidinillion
    millitrinillion
    ...
    millicosnillion

Table 1000 - (10 ^(300)); step = 10^(3 * n); n = n + 10
    millinillion
    millideknillion
    millicosnillion
    millitricontnillion
    ...
    millihectnillion

#Then millihect to millikillo
#The milli-metric-nillions
#Finally the milli-Greek-alphabet-nillions 


'''

import Apeironillions as gimmeNumber
import tabulate as t

DATA = []
col_names = ["I", "Suffix", "E(#)", "Powers"]

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









def main():
    tableMakerOne(1, 20, 1)
    tableMakerOne(10, 100, 10, [1])
    tableMakerOne(100, 1000, 100, [1])
    tableMakerOne(1000, 20000, 1000)
    tableMakerOne(10000, 100000, 10000, [1000])
    tableMakerOne(100 * 1000, 1000 ** 2, 100 * 1000, [1000])

    tableMakerTwo(3,60,3)
    tableMakerTwo(30,300,30, [3])
    tableMakerTwo(300,3000,300, [3])


    #tableMakerTwo will be able to print millinillion to millicosanillion by incrementing illi by 1000
    #table maker two can just take and array tbh


if __name__ == "__main__": 
    main()







