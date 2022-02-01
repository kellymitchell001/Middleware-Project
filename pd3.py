from MyClasses import User
from MyClasses import Manufacturer 
from MyClasses import Product 
import hashlib 
users = {
    'TESTUSER':{
        'username': None, 
        'password': None, 
        'firstName': None, 
        'middleName': None, 
        'lastName': None, 
        'companyName': None, 
        'companyType': None, 
        'address': None, 
        'officeNumber': None, 
        'cellNumber': None, 
        'emailAddress': None
    }
}

def userRegistration():
    username = '' # Sets the username to a blank string to use as the check
    while (username == ''): # While the username is black
        tempUsername = input("Enter a username: ")
        taken = 0 # Counter to see if it exists
        for user in users.values(): # This iterates through the values in the dict
            if (user["username"] == tempUsername): # Makes sure the value doesn't already exist
                taken = 1
        if (taken == 1): # If it exists then it will reject it
            print("Sorry, that username is already taken")
        else: 
            username = tempUsername

    user_in = input("Enter a password: ")
    password = hashlib.md5()
    password.update(user_in.encode("utf-8"))
    password = password.hexdigest()
    
    firstName = input("Enter your first name: ")
    middleName = input("Enter your middle name: ")
    lastName = input("Enter your last name: ") 
    companyName = input("Enter the name of your company: ") 
    companyType = input("Enter the type of company you belong to: ") 
    address = input("Enter your address: ") 
    officeNumber = input("Enter your office phone number: ") 
    cellNumber = input("Enter your cell phone number: ") 
    emailAddress = ''
    
    # The email check is identical to the username check, but for the email field
    while (emailAddress == ''):
        tempEAddress = input("Enter your email address: ")
        taken = 0
        for user in users.values():
            if (user["emailAddress"] == tempEAddress):
                taken = 1
        if (taken == 1):
            print("Sorry, that email address is already registered")
        else:
            emailAddress = tempEAddress

    # Generate a userID that is unique to each user based on their unique username and email
    userID = hashlib.md5((username + emailAddress).encode()).hexdigest()
    users[userID] = {
        "username": username, 
        "password": password, 
        "firstName": firstName, 
        "middleName": middleName, 
        "lastName": lastName, 
        "companyName": companyName, 
        "companyType": companyType, 
        "address": address, 
        "officeNumber": officeNumber, 
        "cellNumber": cellNumber, 
        "emailAddress": emailAddress
    }

    return users[userID] #returns the user information in a dictionary



def formatUserTable():
    for key in users.keys():
        print(key)
        for jey in users[key].keys():
            print(jey + " = " + str(users[key][jey]))
        print()



def moduleSetailedSpecifications():
    MDSDict = {
        "Manufacturer": input("Enter the Manufacturer: "), 
        "Location": input("Enter the Location: "), 
        "Contact": input("Enter the Contact: "), 
        "Address": input("Enter the Address: "), 
        "Email": input("Enter the Email: "), 
        "Phone": input("Enter the Phone: "), 
        "ModelNumber": input("Enter the Model Number: "), 
        "Manufacturer": input("Enter the Manufacturer: "), 
        "ManufacturingDate": input("Enter the Manufacturing Date: "), 
        "Length": input("Enter the Length: "), 
        "Width": input("Enter the Width: "), 
        "Weight": input("Enter the Weight: "), 
        "CellArea": input("Enter the CellArea: "), 
        "CellTechnology": input("Enter the Cell Technology: "), 
        "TotalNumberOfCells": input("Enter the Total Number Of Cells: "), 
        "NumberOfCellsInSeries": input("Enter the Number Of Cells In Series: "), 
        "NumberOfSeriesStrings": input("Enter the Number Of Series Strings: "), 
        "NumberOfBypassDiodes": input("Enter the Number Of Bypass Diodes: "), 
        "SeriesFuseRating": input("Enter the Series Fuse Rating: "), 
        "InterconnectMaterial": input("Enter the Interconnect Material: "), 
        "InterconnectSupplier": input("Enter the Interconnect Supplier: "), 
        "SuperstrateType": input("Enter the Superstrate Type: "), 
        "SuperstrateManufacturer": input("Enter the Superstrate Manufacturer: "), 
        "SubstrateType": input("Enter the Substrate Type: "), 
        "FrameMaterial": input("Enter the Frame Material: "), 
        "FrameAdhesive": input("Enter the Frame Adhesive: "), 
        "EncapsulantType": input("Enter the Encapsulant Manufacturer: "), 
        "EncapsulantManufacturer": input("Enter the Encapsulant Manufacturer: "), 
        "JunctionBoxType": input("Enter the Junction Box Type: "), 
        "JunctionBoxManufacturer": input("Enter the Junction Box Manufacturer: "), 
        "JunctionBoxAdhesive": input("Enter the Junction Box Adhesive: "), 
        "CableType": input("Enter the Cable Type: "), 
        "ConnectorType": input("Enter the Connector Type: "), 
        "MaximumSystemVoltage": input("Enter the Maximum System Voltage: "), 
        "RatedVoc": input("Enter the Rated Voc: "), 
        "RatedIsc": input("Enter the Rated Isc: "), 
        "RatedVmp": input("Enter the Rated Vmp: "), 
        "RatedImp": input("Enter the Rated Imp: "), 
        "RatedPmp": input("Enter the Rated Pmp: "), 
        "RatedFf": input("Enter the Rated Ff: "),
    }
    return MDSDict

def manRegistration():
    manDict = {
        "name": input("Enter the name: "),
        "registered_country": input("Enter the registered country: "),
        "contact_person": input("Enter the contact person: ")
    }
    return manDict

def readFile(filename):
    filein = open(filename, 'r')
    return filein

def main():
    # This gets all the datas that it needs
    userInfo = userRegistration()
    newUser = User(*list(userInfo.values()))
    manInfo = manRegistration()
    newMan = Manufacturer(*list(manInfo.values()))
    productInfo = list(moduleSetailedSpecifications().values())
    newProduct = Product(*productInfo[4:])

    # This displays the product information
    print(newProduct.getManufacturer() + ", " + newMan.getContact() + ", " +     newUser.getEmail() + ", " +     newProduct.getModelNumber() + ", " +     newProduct.getCellTechnology() + ", " +     newProduct.getMaximumSystemVoltage() + ", " +     newProduct.getRatedPmp())

    # This reads the file and outputs the needed lines
    readedFile = readFile('test_results.csv')
    for i in readedFile:
        if i.split(',')[1] == "Baseline":
            print(i, end='')

main()
