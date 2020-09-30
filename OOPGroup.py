# Pet Shop OOP Assingment

# Shannon Murray
# J.R. Smith
# Alex Bennett
# Miller Hardy

# This program prompts the user to enter the number of cusotmers for the "Critter Watch" Pet Boarding company.
# Data on each customer, their pet, and their pet's appointment is recorded, and a bill statement is printed.
# The user can then specify a payment, and an updated bill statement is printed for the current customer.

from datetime import datetime

#Cusotmer class
class Customer :

    # Class variable
    company_name = "Critter Watch"

    # Constructor - receives parameters from user to assign to attributes
    def __init__(self, fName, lName, cusAddress1, cusAddress2, cusCity, cusState, cusZip) :
        self.first_name = fName
        self.last_name = lName
        self.address1 = cusAddress1
        # calculates cust_id by calling the gen_id method; passes parameters with leading/trailing spaces removed
        self.cust_id = self.gen_id(self.first_name.strip(), self.last_name.strip(), self.address1.strip())
        self.address2 = cusAddress2
        self.city = cusCity
        self.state = cusState
        self.zip = cusZip
        self.balance = 0.0
        # cust_pet intended to hold a list Pet object
        self.cust_pet = []

    # generates customer id using the first 3 letters from first and last name, and the first 5 letters of the address
    def gen_id(self, fName, lName, firstAddress) :
        newCusID = fName[0:3] + lName[0:3] + firstAddress[0:5]
        # Replace any spaces in the string with no space ('')
        newCusID = newCusID.replace(" ", "")
        return(newCusID)

    # Return summary statement for the customer pet appointment bill
    def return_bill(self) : 
        return("Customer " + self.cust_id + " with name " + self.first_name + " " + self.last_name + " owes $" + \
            str(self.balance) + " for " + self.cust_pet[len(self.cust_pet) - 1].pet_name + "'s stay from " + \
                str(self.cust_pet[len(self.cust_pet) - 1].appointment[len(self.cust_pet[len(self.cust_pet) - 1].appointment) - 1].begin_date.strftime("%m/%d/%Y")) + " to " + \
                str(self.cust_pet[len(self.cust_pet) - 1].appointment[len(self.cust_pet[len(self.cust_pet) - 1].appointment) - 1].end_date.strftime("%m/%d/%Y")))

    # receives payment from the user and updates the customer balance
    def make_payment(self, fPayment) :
        self.balance = round(self.balance - fPayment, 2)

# Pet class:
class Pet() :
    # Instance Variables:
    def __init__(self, petName, sBreed, iAge, oOwner) :
        self.pet_name = petName
        self.breed = sBreed
        self.age = iAge
        self.owner = oOwner
        self.appointment = []
        # creates new appointment object 
        self.appointment.append(Appointment(self.owner))

# Appointment class:
class Appointment() :

    # constructor
    def __init__(self, oOwner) :
        self.owner = oOwner

    # receives parameters from the user and stores them to attributes
    def set_appointment(self, beginDate, endDate, dayRate) :
        self.begin_date = beginDate
        self.end_date = endDate
        self.day_rate = dayRate
        # calls the calc_days() method to generate additional attributes
        self.calc_days()
        # add cost to customer balance
        self.owner.balance = self.total_cost

    # determines how many days the appointment lasted and the total cost of the appointment
    def calc_days(self) :
        self.total_days = (self.end_date - self.begin_date).days
        # If the appointment began and ended on the same day, count it as 1 day
        if(self.total_days <= 0) :
            self.total_days = 1
        self.total_cost = self.total_days * self.day_rate
        

# collect customer, pet, and appointment information for each customer 
# determine number of customers
numCustomers = int(input("Enter number of customers to enter: "))

# collect information for each Customer
for iCount in range (0, numCustomers) :

    # collect customer information
    print("\nInformation for customer number " + str(iCount + 1))
    fName = input("\nEnter first name: ")
    lName = input("Enter last name: ")
    cusAddress1 = input("Enter first address: ")
    cusAddress2 = input("Enter second address: ")
    cusCity = input("Enter city: ")
    cusState = input("Enter state: ")
    cusZip = input("Enter zip code: ")

    oCustomer = Customer(fName, lName, cusAddress1, cusAddress2, cusCity, cusState, cusZip)

    # determine number of pets for current customer
    petCount = int(input("\nEnter number of pets: "))

    # collect pet information for each pet by iterating through the list
    for jCount in range (0, petCount) :
        print("\nInformation for pet number " + str(jCount + 1))
        petName = input("\nEnter pet's name: ")
        petBreed = input("Enter pet's breed: ")
        petAge = int(input("Enter pet's age: "))

        # creates new pet object and appends to customer list
        oCustomer.cust_pet.append(Pet(petName, petBreed, petAge, oCustomer))

        # determine number of appointments for current pet
        appointCount = int(input("\nEnter number of appointments for " + oCustomer.cust_pet[len(oCustomer.cust_pet) - 1].pet_name + ": "))

        # collect appointment information for each appointment by iterating through the list
        for kCount in range (0, appointCount) :
            print("\nInformation for appointment number " + str(kCount + 1))
            beginDate = datetime.strptime(input("\nEnter the appointment start date in the format m/d/y: "), "%m/%d/%Y").date()
            endDate = datetime.strptime(input("Enter end appointment end date in the format m/d/y: "), "%m/%d/%Y").date()
            dayRate = float(input("Enter the rate per day: "))
            print("\n")

            oCustomer.cust_pet[len(oCustomer.cust_pet) - 1].appointment[len(oCustomer.cust_pet[len(oCustomer.cust_pet) - 1].appointment) - 1].set_appointment(beginDate, endDate, dayRate)
            print(oCustomer.return_bill())

            payment = float(input("Enter a payment amount: "))
            oCustomer.make_payment(payment)

            print(oCustomer.return_bill())
            print("\n")
