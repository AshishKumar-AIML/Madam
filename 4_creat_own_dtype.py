class fraction:
    #parameterized constructor
    def __init__(self,x,y):  #ye ek magic method hai,rule
        print(id(self))   #ye koi value retun nahi karte,
        print(id(x)) # always none value retturn karta hai
        self.nume=x
        self.deno=y
        print("creat constructer")
    def __str__(self):  # object ko dekhne ke liye
        return "Ashish"    
f1=fraction(4,7) 
print(id(f1))
print(type(f1))     
print(f1)  

class Fraction:
    #parameterized constructor or magic method
    def __init__(self,x,y):
        self.nume=x
        self.deno=y
        print("creat constructer")

    def __str__(self):  # object ko dekhne ke liye
        return '{}/{}'.format(self.nume,self.deno) 
     
    def __add__(ram,shyam):  # ram,shyam is a object
        new_nume=ram.nume *shyam.deno + shyam.nume*ram.deno
        New_deno=ram.deno*shyam.deno
        return "{}/{}".format(new_nume,New_deno)
        print("hiii")

    def __sub__(madam,maya):
            new_nume=madam.nume *maya.deno - maya.nume*madam.deno
            New_deno=madam.deno*maya.deno
            return "{}/{}".format(new_nume,New_deno)
    
    def __mul__(a,b):
            new_nume=a.nume * b.nume  
            New_deno=a.deno * b.deno
            return "{}/{}".format(new_nume,New_deno)
    
    def __truediv__(c,d):
            new_nume=c.nume *d.deno  
            New_deno=c.deno*d.nume
            return "{}/{}".format(new_nume,New_deno)

    def convert_to_decimal(mam):
         return mam.nume/mam.deno
    
    
f2=Fraction(4,7) 
print(type(f2))    
print(f2)
f3=Fraction(5,9)
print(f3) 
print(f2+f3) 
print(f3-f2)
print(f2*f3)
print(f2/f3)
print(f2.convert_to_decimal())
# print(f2+f3) unsported operand type +
# if q1={1,3,5}  q2={2,5,8}
# print(q1+q2) same error yaani set ka class banane 
# wale ne adding ka koi rule nahi bnaya hai
print(f2)
p1=Fraction(1,9)
p2=Fraction(6,8)
print(p1)
print(p1.__str__())
print(type(p1))
print(p1+p2) # + operater dekhte hi python __add__  magic
print(p2.__sub__(p1)) # method pe chala gaya
# internally kam aise hota hai