import os
import filecmp
import csv
from dateutil.relativedelta import *
from datetime import date

#THIS IS TEST TEST TEST TEST


# .  cd /Users/benrogers/documents/Github/project1
#      python project1-206.py

# THIS IS A TEST COMMENT TO TRY OUT GITHUB



def getData(file):
    # get a list of dictionary objects from the file
    # Input: file name
    # Ouput: return a list of dictionary objects where

    dataList = []
    dataDict = {}
    inFile = open(file, "r")
    line = inFile.readlines()
    inFile.close()

    with open(file, 'r') as inFile:
        csv_reader = csv.reader(inFile)

        next(csv_reader)

        for values in csv_reader:
            dataDict['First'] = values[0]
            dataDict['Last'] = values[1]
            dataDict['Email'] = values[2]
            dataDict['Class'] = values[3]
            dataDict['Birthday'] = values[4]
            dataList.append(dataDict)
            dataDict = {}
        return dataList


# the keys are from the first row in the data. and the values are each of the other rows


def mySort(data, col):
    # Sort based on key/column
    # Input: list of dictionaries and col (key) to sort on
    # Output: Return the first item in the sorted list as a string of just: firstName lastName
   
    dictDataSorted = sorted(data, key=lambda k: k[col], reverse = True)
    for i in dictDataSorted:
    	firstString = i['First']
    	lastString = i['Last']
    return firstString + " " + lastString



def classSizes(data):
    # Create a histogram
    # Input: list of dictionaries
    # Output: Return a list of tuples sorted by the number of students in that class in
    # descending order
    # [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
    classSizeDictionary = {}
    sortedClassSize = []

    for dictionary in data:
        currentClass = dictionary['Class']
        classSizeDictionary[currentClass] = classSizeDictionary.get(currentClass, 0) + 1

    sortedClassSize = sorted(classSizeDictionary.items(), key=lambda k: k[1], reverse=True)

    return sortedClassSize


def findMonth(a):
    # # Find the most common birth month form this data
    # # Input: list of dictionaries
    # # Output: Return the month (1-12) that had the most births in the data
    monthDictionary = {}
    for dictionary in a:
        fullBirthday = dictionary['Birthday']
        birthdaySplit = fullBirthday.split('/')
        month = int(birthdaySplit[0])

        monthDictionary[month] = monthDictionary.get(month, 0) + 1
        monthSort = sorted(monthDictionary.items(), key=lambda k: k[1], reverse=True)
        firstTuple = monthSort[0]
    return firstTuple[0]




def mySortPrint(a, col, fileName):
    # #Similar to mySort, but instead of returning single
    # #Student, the sorted data is saved to a csv file.
    # # as fist,last,email
    # #Input: list of dictionaries, col (key) to sort by and output file name
    # #Output: No return value, but the file is written
    data = []

    dictDataSorted = sorted(a, key=lambda k: k[col])

    outputfile = open(fileName, 'w')
    for values in dictDataSorted:
        firstName = values["First"]
        lastName = values["Last"]
        email = values["Email"]
        outputfile.write("{},{},{}\n".format(firstName, lastName, email))
        print(outfile)




def findAge(a):
    # # def findAge(a):
    # # Input: list of dictionaries
    # # Output: Return the average age of the students and round that age to the nearest
    # # integer.  You will need to work with the DOB and the current date to find the current
    # # age in years.

    currentDate_day = date.today()

    currentDate_Month = currentDate_day.month

    currentDate_year = currentDate_day.year

    avgAge = 0

    count = 0

    #######################################
    monthDictionary = {}
    for dictionary in a:
        fullBirthday = dictionary['Birthday']
        birthdaySplit = fullBirthday.split('/')
        month = int(birthdaySplit[0])
        dayOfMonth = int(birthdaySplit[1])
        yearofBirth = int(birthdaySplit[2])

        if (currentDate_day and currentDate_Month) >= (dayOfMonth and month):
            age = (currentDate_year - yearofBirth) + 1
            count += 1
            avgAge += age

        else:
            avgAge += age
            count += 1
    return int(avgAge // count)






# print(getData("P1DataA.csv"))
#dataTest = getData("P1DataA.csv")
#print(mySort(dataTest, "Last"))
# mySortPrint(dataTest, 'Last', 'outfile.csv')
# mySortPrint(dataTest, 'First', 'anotherTest.csv')
# print(findAge(dataTest))
# print(findMonth(dataTest))
# print(mySort(dataTest, 'Last'))
# print(mySortPrint(dataTest))

# .  cd /Users/benrogers/documents/Github/project1
#      python project1-206.py                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

###############################################################
# DO NOT MODIFY ANY CODE BELOW THIS
###############################################################

#We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score

#files: p1dataA.csv , p1DataB.csv
#wriite to:    outfile.csv

#ain() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

#Standard boilerplate to call the main() function that tests all your code

dataTest = getData("P1DataA.csv")
print(mySort(dataTest, 'Last'))
if __name__ == '__main__':
    main()
