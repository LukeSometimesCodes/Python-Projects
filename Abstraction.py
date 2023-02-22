#Importing so it works in hte first place

from abc import ABC, abstractmethod

class testabstraction(ABC):
    #function w abstract method
    def payslip(self, amount):
        print('You have spent ', amount)

    @abstractmethod
    def payment(self, amount):
        pass
    
#child class that defines implementation
class PaymentTest(testabstraction):
    def payment(self, amount):
        print ('Your purchase amount of {} is more then your 100 dollar limit'.format(amount))
        
obj = PaymentTest()
obj.payslip('$70,000')
obj.payment('70,000')
