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
    company_name = "Critter Watch"

    # Instance variables
    def __init__(self, fName, lName, cusAddress1, cusAddress2, cusCity, cusState, cusZip) :
        self.first_name = fName
        self.last_name = lName
        self.address1 = cusAddress1
        # calculates cust_id by calling the gen_id
        self.cust_id = self.gen_id(self.first_name.strip(), self.last_name.strip(), self.address1.strip())
        self.address2 = cusAddress2
        self.city = cusCity
        self.state = cusState
        self.zip = cusZip
        self.balance = 0.0
        # cust_pet intended to hold a Pet object
        self.cust_pet = None

    def gen_id(self, fName, lName, firstAddress) :
        # generates customer id using the first 3 letters from first and last name, and the first
        # 5 letters of the address
        newCusID = fName[0:3] + lName[0:3] + firstAddress[0:5]
        # Replace any spaces in the string with no space ('')
        newCusID = newCusID.replace(" ", "")
        return(newCusID)

    def return_bill(self) : 
        # Return summary statement for the customer pet appointment bill
        return("Customer " + self.cust_id + " with name " + self.first_name + " " + self.last_name + " owes $" + str(round(self.balance, 2)) + " for " + self.cust_pet.pet_name + "'s stay from " + str(self.cust_pet.appointment.begin_date) + " to " + str(self.cust_pet.appointment.end_date))
        # Customer greand2677e with name greg anderson owes $123.50 for charlie's stay from 10/01/2020 to 10/20/2020

    def make_payment(self, fPayment) :
        self.balance = round(self.balance - fPayment, 2)
        # make_payment() should receive a float value and subtract the amount from the balance attribute and update the balance attribute

# class Pet:
class Pet() :
    # Instance Variables:
    def __init__(self, petName, sBreed, iAge, oOwner) :
        self.pet_name = petName
        self.breed = sBreed
        self.age = iAge
        self.owner = oOwner
        self.appointment = Appointment(self.owner)

# class Appointment :
class Appointment() :

    def __init__(self, oOwner) :
        self.owner = oOwner

    def set_appointment(self, beginDate, endDate, dayRate) :
        self.begin_date = beginDate
        self.end_date = endDate
        self.day_rate = dayRate
        self.calc_days()
        self.owner.balance = self.total_cost

    def calc_days(self) :
        self.total_days = (self.end_date - self.begin_date).days
        if(self.total_days <= 0) :
            self.total_days = 1
        self.total_cost = self.total_days * self.day_rate
        

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

petName = input("Enter your pet's name: ")
petBreed = input("Enter your pet's breed: ")
petAge = int(input("Enter your pet's age: "))

oCustomer.cust_pet = Pet(petName, petBreed, petAge, oCustomer)

from datetime import datetime

beginDate = datetime.strptime(input("Enter Start date in the format m/d/y: "), "%m/%d/%Y").date()
endDate = datetime.strptime(input("Enter End date in the format m/d/y: "), "%m/%d/%Y").date()
dayRate = float(input("Enter the rate per day: "))

oCustomer.cust_pet.appointment.set_appointment(beginDate, endDate, dayRate)
print(oCustomer.return_bill())

payment = float(input("Enter a payment amount: "))
oCustomer.make_payment(payment)

print(oCustomer.return_bill())
