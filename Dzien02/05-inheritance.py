
# OOP - dziedziczenie

class Person:
    def __init__(self, id, fname, lname):
        self.id = id
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.id} - {self.fname} {self.lname}"

class Customer(Person):

    def __init__(self, id, fname, lname, email):
        Person.__init__(self, id, fname, lname)
        self.email = email

    def set_email(self, email):
        self.email = email

    def __str__(self):
        return f"{self.id} - {self.fname} {self.lname} - {self.email}"

class VIPCustomer(Customer):
    
    def get_discount(self):
        return 10

customer = Customer(1, "Jan", "Kowalski", "adres@email.pl")
customer.email = "jk@host.pl"
print(customer)

vip = VIPCustomer(1, "Jan", "Kowalski", "adres@email.pl")
vip.get_discount()