class A:
    print('hello')
ob=A()

#as you can see in this the hi is not printed inside def i.e method
class A:
    print('hello')
    def method(self):
        print('hi')
    def sum(self,a,b):
        print(a+b)
ob=A()
ob.method() #1 default argument is passed that is self
ob.sum(3,4) #sum(self,3,4)