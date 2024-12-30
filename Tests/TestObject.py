#Literal Test created as an object to hold attributes required for entry
class TestObject:

    #Initializes the name of the test, ID number, and currently a test index
    #Attributes such as container ID, barcode, etc. are planned but not implemented
    def __init__(self, name=str, idn=int, index=int):
        self.name = name
        self.idn = idn
        self.index = index
