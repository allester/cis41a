"""
Lab 3  - lab3.py - De Anza  CIS D041A - Allester Ramayrat
"""

def readFile(file):
    """
    Returns 2 dictionaries from the text file.
    :param file: user input file of .txt or .csv
    :return dict1: Keys are student types. Values are quarterly enrollments.
    :return dict2: Keys are quarter and year. Values are enrollment #s of qtr & yr.
    """
    enroll = open(file)

    
    dict1 = {}

    #reads file line by line
    for line in enroll:
        #turns line into list
        line = line.strip().split(',')
        #makes index 0 the key and the list from index 1 and on the values
        dict1[line[0]] = line[1:]

    dict2 = {}
    #gets first key in from dict1 ("Enrollment")
    firstKey = list(dict1.keys())[0]
    #uses first key in dict 1 and assigns the values of "Enrollment" to dict2 keys
    for quarter in dict1[firstKey]:
        dict2[quarter] = []
        #appends values of dict1 to corresponding key in dict2
        for key in dict1:
            #appends value 
            if key != firstKey:
                dict2[quarter].append(dict1[key][dict1[firstKey].index(quarter)])
    #remove firstKey from dict1 as no longer needed and will cause problems if left
    dict1.pop(firstKey)

    enroll.close()
    #acknowledgement statement
    print("Read in", len(dict1), "types of students,", len(dict2), "quarters\n")

    return (dict1, dict2)

def yearlyTotal(dict1):
    """
    Returns a list of the total enrollemts per school year i.e. 2000-2001 per
    index
    :param dict1: Keys are student types. Values are quarterly enrollments.
    :return yearlyTot: List of yearly totals per school years
    """
    #creates list of 0's the length of the number of school years (qtrs / 4)
    yearlyTot = [0] * (len(dict1[list(dict1.keys())[0]]) // 4)

    #assigns one index per school year enrollent total
    for key in dict1:
        for i in range(len(dict1[key])):
            #4 quarters will make up a single index
            yearlyTot[i//4] = yearlyTot[i//4] + int(dict1[key][i])

    return(yearlyTot)

def quarterTotal(dict2, quarter):
    """
    Creates a list of the total enrollments per quarter.
    :param dict2: Keys are quarter and year. Values are enrollment #s of qtr & yr.
    :param quarter: ["Summer", "Fall", "Winter", "Spring"] refer to writeFile #c
    :return quarterTot: List of total enrollments per quarter.
    """
    
    quarterTot = []
    for key in dict2:
        tempVal = 0
        if quarter in key:
            #adds values of quarter to tempVal
            for value in dict2[key]:
                tempVal += int(value)
            #appends tempVal to list the resets tempVal to 0
            quarterTot.append(tempVal)
    return(quarterTot)

def writeFile(INFILE, OUTFILE):
    """
    Reads user input file, prints to screen school year and quarter averages, and prints
    to outfile school year and quarter totals
    :param INFILE: user input file
    :param OUTFILE: output file printed to
    :return none:
    """

    #reads in input file
    dict1, dict2 = readFile(INFILE)
    #creates output file
    outFile = open(OUTFILE, "w")

    #a) Prints to Output File year totals
    firstKey2 = list(dict2.keys())[0]
    year1 = int(firstKey2[-4:])
    print("Year", file = outFile)
    for yearlyTot in yearlyTotal(dict1):
        print(year1, '-', year1+1, ": ", f"{yearlyTot:,}", sep = '', file = outFile)
        year1 += 1

    #b) Prints to Screen Average Yearly Enrollment
    overallTot = 0
    count = 0
    for yearlyTot in yearlyTotal(dict1):
        overallTot += yearlyTot
        count += 1
    yearAvg = round(overallTot / count)
    print("Year average:", f"{yearAvg:,}")

    #c) Prints to Output File Quarter Enrollments
    #d) Prints to Screen Average Quarter Enrollments
    quarterList = ["Summer", "Fall", "Winter", "Spring"]
    
    for quarter in quarterList:
        #prints to out file quarter name
        print(quarter, file = outFile) #c
        #gets school year
        year1 = int(firstKey2[-4:]) #c
        quarterTot = 0 #d
        count = 0 #d
        for value in quarterTotal(dict2,quarter):
            print(year1, "-", year1+1, ": ", f'{value:,}', sep = '', file = outFile) #c
            year1 += 1 #c
            quarterTot += value #d
            count += 1 #d
        print(quarter, "average:", f"{round(quarterTot/count):,}") #d

    print("\nWritten data to lab3out.txt") #d

"""
MAIN
"""

INFILE = "enroll.csv"
OUTFILE = "lab3out.csv"

writeFile(INFILE, OUTFILE)
