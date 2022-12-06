"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, total_pay,contract_type,
                 work_hour,hourly_payment,contract_number,contract_payment
    ):
        self.name = name
        self.contract_type = contract_type
        self.total_pay = total_pay
        self.work_hour = work_hour
        self.hourly_payment = hourly_payment
        self.contract_number = contract_number
        self.contract_payment = contract_payment

    def salary_contract(self):
        # Earn montly salary
        return f"monthly salary of {self.total_pay}"

    def setType(self):
        contract_text = ""
        if(self.contract_type == "salary_contract"):
            contract_text += self.salary_contract()
        if(self.contract_type == "hourly_contract"):
            self.total_pay = self.work_hour * self.hourly_payment
            contract_text +=self.hourly_contract()
        if(self.contract_number != None):
                contract_text +=self.get_commission()
        else:
            contract_text +=self.get_bonusCommission()
        return contract_text

    def get_commission(self):
        return f" and receives a commission for {self.contract_number} contract(s) at {self.contract_payment}/contract"

    def get_bonusCommission(self):
        return f" and receives a bonus commission of {self.contract_payment}"

    def hourly_contract(self):
        return f"contract of {self.work_hour} hours at {self.hourly_payment}/hour"

    def set_pay(self):
        if (self.contract_number != None):
            self.total_pay += self.contract_number * self.contract_payment
            self.get_commission()
        else:
            if (self.contract_payment != None):
                self.total_pay +=self.contract_payment
                self.get_bonusCommission()
        return self.total_pay

    def get_pay(self):
        return self.total_pay

    def __str__(self):
        return f'^{self.name} works on a {self.setType()}.\s+Their total pay is {self.set_pay()}.$'

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',4000,"salary_contract",None,None,None,None)
print(billie.__str__())
print(billie.get_pay()==4000)
print("\n")
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',2500,"hourly_contract",100,25,None,None)
print(charlie.__str__())
print(charlie.get_pay()==2500)
print("\n")
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000,"salary_contract",None,None,4,200)
print(renee.__str__())
print(renee.get_pay()==3800)
print("\n")
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',None,"hourly_contract",150,25,3,220)
print(jan.__str__())
print(jan.get_pay()==4410)
print("\n")
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',2000,"salary_contract",None,None,None,1500)
print(robbie.__str__())
print(robbie.get_pay()==3500)
print("\n")
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',4200,"hourly_contract",120,30,None,600)
print(ariel.__str__())
print(ariel.get_pay()==4200)
