import nameGen
import time
import illionConverter
import tqdm

def comparitron(maax):
    ROUND = 3 #decimal rounding point
    progressMark = maax // 10
    END = maax * 2

    print("Domain: (1 - " + str(maax) + ")")
    #stats for Cola's Enum
    CEstartTime = time.time() 
    CEcurTime = 0

    CEtimeSum = 0
    CElenSum = 0
    CEtimeMax = 0
    CElenMax = 0

    #stat's for CiC
    CICstartTime = time.time() 
    CICcurTime = 0

    CICtimeSum = 0
    CIClenSum = 0
    CICtimeMax = 0
    CIClenMax = 0

    for i in tqdm.tqdm(range(maax), ncols = 68): #loop with progeress bar
        CEstartTime = time.time() 
        s = nameGen.GimmeNumber(i)[0]
        CEcurTime = time.time()
        CEtimeSum = CEtimeSum + (CEcurTime - CEstartTime)
        CElenSum  = CElenSum + len(s)

        if (CEtimeMax < (CEcurTime - CEstartTime)):
            CEtimeMax = (CEcurTime - CEstartTime)
        if (CElenMax < len(s)):
            CElenMax = len(s)

        CICstartTime = time.time() 
        s = illionConverter.GimmeNumber(i)[0]
        CICcurTime = time.time()
        CICtimeSum = CICtimeSum + (CICcurTime - CICstartTime)
        CIClenSum  = CIClenSum + len(s)

        if (CICtimeMax < (CICcurTime - CICstartTime)):
            CICtimeMax = (CICcurTime - CICstartTime)
        if (CIClenMax < len(s)):
            CIClenMax = len(s)

    print("\n\n-Stats for Cola's Enumeration-\n")
    print("Average Enumeration Time:   " + str(round(CEtimeSum / maax, 12)) + " seconds")
    print("Average Enumeration Length: " + str(round(CElenSum / maax, ROUND)) + " characters")
    print()
    print("Maximum Enumeration Time:   " + str(round(CEtimeMax, ROUND)) + " seconds")
    print("Maximum Enumeration Length: " + str(CElenMax) + " characters")

    print("\n-Stats for Conway's illion Converter-\n")
    print("Average Enumeration Time:   " + str(round(CICtimeSum / maax, 12)) + " seconds")
    print("Average Enumeration Length: " + str(round(CIClenSum / maax, ROUND)) + " characters")
    print()
    print("Maximum Enumeration Time:   " + str(round(CICtimeMax, ROUND)) + " seconds")
    print("Maximum Enumeration Length: " + str(round(CIClenMax, ROUND)) + " characters")


def doubItest(max):
    #tests for doubled i's (miillion)
    s = "b"
    i = 1

    while i < (max + 1) and not "ii" in s:
        info = str(i) + "\t" + nameGen.GimmeNumber(i)[0]
        #info = str(i) + "\t" + illionConverterTest.GimmeNumber(i)[0]
        s = nameGen.GimmeNumber(i)[0]
        print(info)

        if ("ii" in s):
            break
        i = i + 1
    
    #end of loop
    if "ii" in s:
        print ("Test failed.")
        return 
    print("Test passed.")
    return


def adjDup(max):
    #test for adjacent duplicated names like 101 -> centillion 
    #this takes a minute and I do not want to suprise. So I commented it out.
    a = "a"
    b = "b"
    i = 1
    flagOne = False #flips when a == b
    flagTwo = False
    while i < (max + 1) and not a == b:
        info = str(i) + "\t" + nameGen.GimmeNumber(i)[0]
        #info = str(i) + "\t" + illionConverterTest.GimmeNumber(i)[0]
        a = b
        b = nameGen.GimmeNumber(i)[0]
        #print(info)

        if (a == b):
            break
        i = i + 1
    
    #end of loop
    if a == b:
        print ("Test failed.")
        return 
    print("Test passed.")
    return

def main():
    comparitron(10 ** 6 * 3)