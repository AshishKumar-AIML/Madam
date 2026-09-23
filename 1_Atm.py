'''
class atm:
    # constructor(is a spacial function(magic mathod))-> has a superpower
    # this is automatically called when an object is created.it is used to 
    # initialize the object data
    def __init__(self):

       self.pin=""
       self.balance=0
obj=atm()       
print(type(obj))
print(obj.balance)
    
#two type of classes 1.built in class(int,tuple,list,str,dic) 2.user defined class
'''
class Atm:
   # constructor
   def __init__(self):
    self.pin=""
    self.balance=10000
    self.manu()
   def manu(self):
    print("""hi how can i help you?
    1. press 1 to creat pin
    2. press 2 to check balance
    3. press 3 to change the pin
    4. press 4 to withdraw the balance   
    5. press 5 to elese the exit """ )  
    user_input=int(input("enter a choice"))
    
    if user_input==1 :
      self.creat_pin()
      #creat pin
    elif user_input==2:
      self.check_balance()
      #check balance
    elif user_input==3: 
      self.change_pin() 
      # change pin
    elif user_input==4:
      self.withdrow_balance()
      #whithdrow balance
    elif user_input==5:
      self.deposite_balance()
      # deposite balance
    else:
      print("you exit the ATM")


   def creat_pin(self):  
    user_pin=input("enter your pin")
    self.pin=user_pin 

    user_balance=int(input("enter your balance"))
    self.balance=user_balance
    print("pin crest successfully") 
    self.manu()  

   def check_balance(self): 
     
     user_pin=input("enter a pin")
     if user_pin==self.pin:
       print("your balance is:",self.balance)
       self.manu()  
     else:
       print("wrong pin")
       self.manu()

   def change_pin(self):
     old_pin=input("enter a old pin")
     if old_pin==self.pin:
       new_pin=input("enter a new pin")
       self.pin=new_pin  
       print("change pin successfully",self.pin)
       self.manu() 
     else:
       print("pin change karne nahi de sakta hu")        
       self.manu() 

   def withdrow_balance(self):
     
     withdrow_amount=int(input("enter a balnce:"))
     old_pin=input("enter a old_pin")
     if old_pin==self.pin:
       self.balance-=withdrow_amount
       print("Now is your balance is:",self.balance)
       self.manu()
     else:
       print("enter a corract pin")  
       self.manu()
  
   def deposite_balance(self):

    deposite_amount=int(input("enter a balnce:"))
    old_pin=input("enter a old_pin")
    if old_pin==self.pin:
      self.balance+=deposite_amount
      print("Now is your balance is:",self.balance)
      self.manu()
    else: 
      print("enter a corract pin")  
      self.manu() 
hg=Atm()
print(hg.check_balance())

# in python inside the classs,called method
# outside yhe class ,called function
# like that
'''
l=[4,5,7,8]
len(l)   this is a function
l.append(4)   this is a method
'''
