#Method holding file for all tests related actions
#After full expansion this may be segmented into for concise files
import Menu.MenuActioner
from Tests.TestObject import TestObject
import random

#Global dictionary for testing, actual csv writing will replace this with multilple fields
objdict = {}

#Simple test look up method, currently only accepting values passed as string
def getbyidentifier():
    #Recieves simple input into if statements, attempted case statement, did not yield results
    userin = input()
    if userin == int():
        for keys, val in objdict.items():
            if userin == keys:
                print(val)
    else:
        for val, keys in objdict.items():
            if userin == val:
                print(keys)
    Menu.MenuActioner.launchmainmenu()

#Test entry method that creates test with randomized range of ints for testing
#Currently only takes in name of test being added but will be expanded to fulfill other attribute requirments - 12/29
def testentry():
    #Receives simple input
    name = str(input("Please enter the name of the test you'd like to add,"
                     " this must be 0-5 characters>>"))

    #Currently only assigns random integers to index and ID values
    idn = random.randint(100, 999)
    index = random.randint(100, 999)

    #Makes sure that userin is with test acronym requirements
    while len(name) < 0 or len(name) > 6:
        print("Please input 5 letter code>>")
    else:
        #Simple validity check
        if name is not None:
            newtest = TestObject(name, idn, index)
            objdict.update({newtest.idn : newtest.name})
            #Prints simple console output
            print(name + " successfully added with ID number: " + str(idn)
                  + " at index " + str(index))
            #Currently testing writing to file for multiple values - 12/29
            with('testlist', 'w') as writer:
                #Currently only writes the values indvidually and then creates a new line
                writer.write(newtest.name, newtest.idn + "\n")

    Menu.MenuActioner.launchmainmenu()

def edittest():
    pass