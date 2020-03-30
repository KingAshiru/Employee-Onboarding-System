import random
import string

#This program creates an account for new employees at HNG tech

class NewUser:
    def __init__(self):
        self.users = {}
        self.firstName = ""
        self.lastName = ""
        self.mailAddress = ""

    def getUserData(self):
        print("Hi there, I'm about to create an employee account for you on HNG platform and I would need a few details")
        self.firstName = str(input("Please enter your first name : "))
        self.lastName = str(input("Enter your last name: "))
        self.mailAddress = str(input("Enter your email address: "))

    def generatePassword(self):
        randomString  = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        return(self.firstName[:2] + randomString + self.lastName[-2:])

    def showDetails(self):
        print("Your First Name is: " + self.firstName)
        print("Your Last Name is: "+ self.lastName)
        print("Your email address is: "+ self.mailAddress)

    def setPassword(self):
        self.userPassword = str(input("Please enter preferred password with not less than 7 characters."))
        while len(self.userPassword) < 7:
            print("Password length is short, please make password at least 7 characters!")
            self.userPassword = str(input("Please enter preferred password with not less than 7 characters."))
        self.showDetails()
        self.password = self.userPassword
        print("Your password is " + self.userPassword)
        
    def checkPassword(self):
        print("Hi "+ self.firstName + " your generated password is: ")
        self.password = self.generatePassword()
        print(self.password)
        print("Would you like to proceed with this password?")
        preferPassword = str(input("Answer y for Yes and n for No!"))
        if preferPassword == 'y' or preferPassword == 'Y':
            self.showDetails()
            print("Your password is " + self.password)
        else:
            self.setPassword()
   
    def userContainer(self):
        self.users[self.firstName+self.lastName] = (self.mailAddress,self.password)

    def main(self):
        self.getUserData()
        self.generatePassword()
        self.checkPassword()
        self.userContainer()
    def printData(self):
        print(self.users)


user1 = NewUser()
user1.main()