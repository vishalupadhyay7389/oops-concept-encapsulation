
# oops concept inhertiance me single object called mutiple funstion
'''
class A:
    def displayA(self):
        print("Welcome to wscubetech A")
class B(A):
    def displayB(self):
        print("Welcome to wscubetech B")
        
obj = B()
obj.displayB()
obj.displayA()
'''


# Multi Lable inheritance in opps reusability of code .
'''
class A:
    def displayA(self):
        print("Welcome to ws cubetech A")
        
class B(A):
    def displayB(self):
        print("Welcome to Ws cube tech  B")
        
class C(B):
    def displayC(self):
        print("Welcome to ws cube teck C ")
        
obj = C()
obj.displayC()
obj.displayB()
obj.displayA()
'''
# multiple inhertiance 

class A:
    def displayA(self):
        print("Welcome to Ws cube tech A")
class B:
    def displayB(self):
        print("Welcome to Ws cube tech B")
        
class C(A , B):
    def displayC(self):
        print("Welcome to ws cube tech C")
        
obj = C()
obj.displayC()
obj.displayB()
obj.displayA()






