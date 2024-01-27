import nameGen as A
import time 

def BoringSpeedTest(t = .1, Greek = True, threshold = 0, wrench = 0): # how high can we count in 1 tenth of a second
    #a threshold of 0 indicates no threshold, this is not true for the wacky test
    DATA = []
    STOP = ""
    AVGTIME = 0
    AVGLEN = 0
    #print("\nSpeed Test (t = " + str(t) + ")\n")
    i = 1
    result = 0
    step = 1
    metaStep = 10
    mafongo = ""
    while (result < t and (i < threshold or threshold == 0)): #a threshold of 0 is no threshold
        time1 = time.time()
        mafongo = A.GimmeNumber(int(i) + wrench, Greek) #prime number is just to throw a wrench in things
        time2 = time.time()
        result = round(time2 - time1, 64)
        i = i + step
        step = step + (metaStep // 10)
        if (step >= metaStep):
            metaStep = metaStep * 10
        DATA.append((str(mafongo), str(A.Engineerinify(i, False)) , result))
    STOP = "\nStopped at: " + " " + str(A.Engineerinify(i, False)[1]) + " " + "\n"
    if (not threshold == 0):
        STOP += "\nThreshold met or exceed: " + str(i >= threshold)
    AVGTIME = getAvgTimes(DATA)
    AVGLEN = getAvgLenNames(DATA)
    return (AVGTIME, AVGLEN, STOP)


#this guy has a bug that generates all kinds of wacky inputs, quite fortuitous 
def WackySpeedTest(t = .1, Greek = True, threshold = 0, wrench = 17): # how high can we count in 1 third of a second
    DATA = []
    STOP = ""
    AVGTIME = 0
    AVGLEN = 0
    #print("\nSpeed Test (t = " + str(t) + ")\n")
    i = 1
    result = 0
    step = 1
    mafongo = ""
    while (result < t and i < threshold):
        time1 = time.time()
        mafongo = A.GimmeNumber(int(i) + wrench, Greek) #prime number is just to throw a wrench in things
        time2 = time.time()
        result = round(time2 - time1, 64)
        i = i + step
        step = step + step
        if (step % 10 == 0):
            step = step * 10
        DATA.append((str(mafongo), str(A.Engineerinify(i, False)) , result))
    STOP = "\nStopped at: " +  " " + str(A.Engineerinify(i, False)[1]) + " " + "\n\nThreshold met or exceed: " + str(i >= threshold)
    AVGTIME = getAvgTimes(DATA)
    AVGLEN = getAvgLenNames(DATA)
    return (AVGTIME, AVGLEN, STOP)

def getAvgLenNames(DATA):
    sum = 0
    for i in DATA:
        sum += len(i[0])
    return sum / len(DATA)

def getAvgTimes(DATA):
    sum = 0
    for i in DATA:
        sum += i[2]
    return sum / len(DATA)

def compare(a, b):
    if (a == b):
        return 0
    if (a < b):
        return -1
    if (a > b):
        return 1



def TableAccuracyTest():
    print("\n-Name Table Accuracy Test-\n")
    #This compares the results we get to the expected results in the tables via a series of inputs
    
    inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

    #this was a bug, now a feature, dropping the first 'lli' after i(10000). Easier to read, still unique.
    expected = ['millinillion', 'billinillion', 'trillinillion', 'quadrillinillion', 'quintillinillion', 'sextillinillion', 'septillinillion', 'octillinillion', 'nonillinillion', 'decinillion', 'undecinillion', 'duodecinillion', 'tredecinillion', 'quattuordecinillion', 'quindecinillion', 'sedecinillion', 'septendecinillion', 'octodecinillion', 'novendecinillion', 'vigintinillion', 'trigintanillion', 'quadragintanillion', 'quinquagintanillion', 'sexagintanillion', 'septuagintanillion', 'octogintanillion', 'nonagintanillion', 'centinillion', 'ducentinillion', 'trecentinillion', 'quadringentinillion', 'quingentinillion', 'sescentinillion', 'septingentinillion', 'octingentinillion', 'nongentinillion', 'millidinillion']
    outputs = []

    for i in inputs:
        outputs.append(A.GimmeNumber(i * 10 ** 3)[0])
    #print("\n\n" + str(outputs))

    i = 0
    fails = 0

    while (i < len(expected)):
        if(not expected[i] == outputs[i]):
            print("Expected: " + expected[i] + "\nReturned: " + outputs[i] + "\nI: " + str(inputs[i] * 10 ** 3) + "\nFAILED\n\n")
            fails = fails + 1
        #else:
            #print("Expected: " + expected[i] + "\nReturned: " + outputs[i] + "\nI: " + str(inputs[i] * 10 ** 3) + "\nPASSED\n\n")
        i = i + 1
    if (fails == 0):
        print("Accurate to tables. Passed.\n")
        return True
    else:
        print("Fails: " + str(fails))
        return False

def SpeedTests(maxTime, threshold, test = "", rounder = 5):
    print("\n>>Speed Tests: maxTime = " + str(maxTime) + " seconds. Threshold: " + A.Engineerinify(threshold, False)[1] + "")
    
    if (test == "B"):
        print("\n--Boring Speed Test--\n")
        ApeiroData = BoringSpeedTest(maxTime, True, threshold)
        IllionData = BoringSpeedTest(maxTime, False, threshold)
    if (test == "W"):
        print("\n--Wacky Speed Test--\n")
        ApeiroData = WackySpeedTest(maxTime, True, threshold)
        IllionData = WackySpeedTest(maxTime, False, threshold)

    print("\n-Apeironillons Coverter-\n")
    print("Average Time of Convertion: " + str(round(ApeiroData[0], rounder)))
    print("Average Name Length: " + str(round(ApeiroData[1], 2)))
    print(ApeiroData[2])

    print("\n-Conway's Illion Coverter-\n")
    print("Average Time of Convertion: " + str(round(IllionData[0], rounder)))
    print("Average Name Length: " + str(round(IllionData[1], 2)))
    print(IllionData[2])




def main():
    if TableAccuracyTest():

        #various tests with large numbers at high thresholds. The Boring tests are typical inputs, the wacky test generates numbers that are difficult to pronounce by name.
        SpeedTests(.1, 97 / 3, "B") #gogol
        SpeedTests(.1, 97 / 3, "W") 
        
        SpeedTests(.1, 10**9, "B")
        SpeedTests(.1, 10**9, "W") 

        SpeedTests(.1, 10**10**3, "B")
        SpeedTests(.1, 10**10**3, "W")

    else:
        print("Debug naming function to continue.")



if __name__ == "__main__":
    main()
