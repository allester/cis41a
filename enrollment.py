"""
Lab 4  - enrollment.py - De Anza  CIS D041A - Allester Ramayrat
"""


class Enrollment:
    def __init__(self,file):
        """
        Assigns 2 variables with 2 different dictionaries from the text file.
        :param file: user input file of .txt or .csv
        :var _dict1: Keys are student types. Values are quarterly enrollments.
        :var _dict2: Keys are quarter and year. Values are enrollment #s of qtr & yr.
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

        self._dict1 = dict1
        self._dict2 = dict2
        
    def yearlyTotal(self):

        """
        Assigns a list of the total enrollments per school year i.e. 2000-2001 per
        index to _yearlyTot
        :param _dict1: Keys are student types. Values are quarterly enrollments.
        :return none:
        """
        #creates list of 0's the length of the number of school years (qtrs / 4)
        yearlyTot = [0] * (len(self._dict1[list(self._dict1.keys())[0]]) // 4)

        #assigns one index per school year enrollent total
        for key in self._dict1:
            for i in range(len(self._dict1[key])):
                #4 quarters will make up a single index
                yearlyTot[i//4] = yearlyTot[i//4] + int(self._dict1[key][i])

        self._yearlyTot = yearlyTot
               
    def quarterTotal(self, quarter):

        """
        Assigns a list of the total enrollments per quarter to _quarterTot
        :param _dict2: Keys are quarter and year. Values are enrollment #s of qtr & yr.
        :return noen: List of total enrollments per quarter.
        """

        quarterTot = []
        for key in self._dict2:
            tempVal = 0
            if quarter in key:
                #adds values of quarter to tempVal
                for value in self._dict2[key]:
                    tempVal += int(value)
                #appends tempVal to list the resets tempVal to 0
                quarterTot.append(tempVal)

        self._quarterTot = quarterTot

