# Python does NOT support method overloading!
# The second method definition overwrites the first one.
# Solution: Use default arguments or *args

class A:
    # Original attempt (doesn't work - second m() overwrites first):
    # def m(self,a,b):
    #     print(a+b)
    # def m(self,a,b,c):  # This REPLACES the first m()
    #     print(a+b+c)
    
    # Solution 1: Using default argument
    def m(self, a, b, c=None):
        if c is None:
            print(f"Sum of 2 numbers: {a+b}")
        else:
            print(f"Sum of 3 numbers: {a+b+c}")

obj=A()
obj.m(10,20)      # Works! Uses default c=None
obj.m(10,20,30)   # Works! Provides c=30

class A:
    def m(self):
        print('hi')
class B(A):
    def m(self):
        print('bye')
ob=B()
ob.m() #prints bye since it overides the parent class class A: