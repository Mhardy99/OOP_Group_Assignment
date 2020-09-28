# Pet Shop OOP Assingment

# Shannon Murray
# J.R. Smith
# Alex Bennett
# Miller Hardy

# Write a program that prompts the user to enter in the number of customers for your Pet Boarding company. You
# do NOT need to store each customer in a list since we haven't talked about that yet. However, you need to
# implement this using classes.

class Customer :
    # Class variable(s)
    # company_name is of type string with the value of Critter Watch
    company_name = "Critter Watch"
    # Instance variables
    def __init__(self, fName, lName, cusAddress1, cusAddress2, cusCity, cusState, cusZip) :
        # first_name of type string
        self.first_name = fName
        # last_name of type string
        self.last_name = lName
        # address1 of type string
        self.address1 = cusAddress1
        # cust_id of type string
            # calculate the cust_id by calling gen_id method passing first_name, last_name, and
            # address1. Make sure there are no trailing or leading spaces in the passed values.
        self.cust_id = self.gen_id(self.first_name.strip(), self.last_name.strip(), self.address1.strip())
        # address2 of type string
        self.address2 = cusAddress2
        # city of type string
        self.city = cusCity
        # state of type string
        self.state = cusState
        # zip of type string
        self.zip = cusZip
        # balance of type float (How much they owe)
        self.balance = 0.0
        # cust_pet of type Pet 
            # (In a class diagram when the arrow from the pet class points to the
            # Customer class that indicates that a Customer object "has a" Pet object. So you will need
            # to include cust_pet (or some name that you want to use) so that the Customer object can
            # hold a pet object. 
        self.cust_pet = None
    def gen_id(self, fName, lName, firstAddress) :
        # gen_id() receives the first_name, last_name, address1 and takes the first 3 letters from
        # the first name, first 3 letters from the last name, and first 5 letters from the address to
        # create the cust_id and returns that string value which when called will be assigned back to
        # the cust_id attribute in the Customer class
            # Replace any spaces in the string with no space ('')
        newCusID = fName[0:3] + lName[0:3] + firstAddress[0:5]
        newCusID = newCusID.replace(" ", "")
        return(newCusID)

    def return_bill(self) : 
        # Return the following string (NOT print)
        # Customer greand2677e with name greg anderson owes $123.50 for charlie's stay from 10/01/2020 to 10/20/2020

    def make_payment(self, fPayment) :
        self.balance = self.balance - fPayment
        # make_payment() should receive a float value and subtract the amount from the balance attribute and update the balance attribute



# class Pet:
class Pet() :
    # Instance Variables:
    def __init__(self, petName, sBreed, iAge, oOwner) :
    # pet_name is of type string
        self.pet_name = petName
    # breed is of type string
        self.breed = sBreed
    # age is of type int
        self.age = iAge
    # owner will be the customer object
        self.owner = oOwner
    # appointment of type Appointment
    # When creating the Appointment object and assigning to the appointment attribute
    # in the Pet constructor, pass the owner to the Appointment constructor
        # self.appointment = Appointment(owner)
 


# class Appointment :

# Code to recieve inputs from the user
fName = input("Enter First Name: ")
lName = input("Enter Last Name: ")
cusAddress1 = input("Enter first address: ")
cusAddress2 = input("Enter second address: ")
cusCity = input("Enter city: ")
cusState = input("Enter state: ")
cusZip = input("Enter zip code: ")

oCustomer = Customer(fName, lName, cusAddress1, cusAddress2, cusCity, cusState, cusZip)
print(oCustomer.cust_id)