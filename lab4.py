"""
Lab 4  - lab4.py - De Anza  CIS D041A - Allester Ramayrat
"""

import enrollment

def writeFile(userin):
    """
    Reads user input, prints to screen the average of option selected by user
    :param userin: user input receive from getChoice()
    :return none:
    """
    if userin == '1':
        enrollment.yearlyTotal()
        average = round(sum(enrollment._yearlyTot) / len(enrollment._yearlyTot))
        print("Yearly average:", f"{average:,}")

    elif userin == '2':
        enrollment.quarterTotal("Summer")
        average = round(sum(enrollment._quarterTot) / len(enrollment._quarterTot))
        print("Summer average:", f"{average:,}")
        
    elif userin == '3':
        enrollment.quarterTotal("Fall")
        average = round(sum(enrollment._quarterTot) / len(enrollment._quarterTot))
        print("Fall average:", f"{average:,}")
        
    elif userin == '4':
        enrollment.quarterTotal("Winter")
        average = round(sum(enrollment._quarterTot) / len(enrollment._quarterTot))
        print("Winter average:", f"{average:,}")
        
    elif userin == '5':
        enrollment.quarterTotal("Spring")
        average = round(sum(enrollment._quarterTot) / len(enrollment._quarterTot))
        print("Spring average:", f"{average:,}")
    
def getChoice():
    """
    Prompts user for a number 1-6 and return the input regardless of range or type.
    Type and range is checked in main function.
    :return userin: str
    """
    print("1. Year\n2. Summer\n3. Fall\n4. Winter\n5. Spring\n6. Quit")

    userin = input("Enter your choice: ")

    if not (userin.isdigit() and int(userin) <= MAX and int(userin) >= MIN):
        print("Choice must be 1-6")
        
    return userin
        
"""
MAIN
"""

MAX = 6
MIN = 1
INFILE = "enroll.csv"

enrollment = enrollment.Enrollment(INFILE)
choiceList = []
userin = 0

while(userin != '6'):
    
    userin = getChoice()

    # writeFile(userin) is called if correct type, range and not in list
    if (userin not in choiceList and userin.isdigit()
        and int(userin) <= MAX and int(userin) >= MIN):
        
        choiceList.append(userin)
        writeFile(userin)

    #if already in list then reruns loops
    elif userin in choiceList:
        print("Refer to output above")
