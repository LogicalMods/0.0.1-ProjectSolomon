#Method holding file for all menu interactions
#Mostly using for calling external methods related to the test catalog
#Less data driven, more for simple user interaction, essential framework that
# will be coverted into a GUI interface
import Tests.TestActioner
from Menu.ContextMenuBase import ContextMenuBase

#Opening menu, always looped back to after actions are completed, the home screen.
def launchmainmenu():
    #Options presented passed into a context menu object
    #Takes in simple input for case statement interaction
    option = "1. Search test menu"
    option2 = "2. Edit test request"
    option3 = "3. Check for updates"
    ContextMenuBase(option, option2, option3)
    userin = int(input("Please make selection>> "))

    match userin:
        case 1:
            launchsearch()

        case 2:
            launcheditmenu()

        case 3:
            updatecycle()

        case _:
            print("No such selection>> ")

#Search menu for test lookup
def launchsearch():
    option = "Enter test by 0-5 character code or 3 digit ID"
    ContextMenuBase(option)
    Tests.TestActioner.getbyidentifier()

#Launches IT menu, mostly will be interaction with TestActioner
def launcheditmenu():
    #Menu presentation and case statement interaction
    option = "1. Create test entry"
    option2 = "2. Edit existing test"
    ContextMenuBase(option, option2)
    userin = int(input("Please input selection>>"))

    match userin:
        case 1:
            Tests.TestActioner.testentry()
        case 2:
            Tests.TestActioner.edittest()
        case _:
            print("No idea dude...")

#Not implemented yet, planned to connect to back end catalog(s) of tests
#For quick updating of test changes and will be interacting will backup functionality
def updatecycle():
    pass