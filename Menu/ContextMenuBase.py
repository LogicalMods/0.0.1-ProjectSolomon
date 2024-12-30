#Context menu object, reusable structure for creating quick context menus
#Currently accepts only a handful of options, if only 1 parameter space is needed it will skip it
class ContextMenuBase:
    #Initializes option slots for the menu
    def __init__(self, option=None, option2=None, option3=None, option4=None):
        self.option = option
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        #Assign all options to iterable list
        oplist = [option, option2, option3, option4]
        #Console spacer
        print("==================")
        #For loop that is fired to only print the filled out options
        #Parameters are meant to be flexible but mostly for quick printing of non-null strings presented as options
        for opt in oplist:
            #Passes any empty options
            if opt is None:
                pass
            #Only prints filled paramters
            else:
                print(opt)
        print("==================")