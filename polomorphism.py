'''
l = [10,20,30,40,5,10]
print(len(l))

l = "welcome to wscubetech "
print(len(l))
'''


'''
class Ws:
    def displayinfo(self , name):
        print("Welcome to wscubetech" + name)
        
obj = Ws()
obj.displayinfo()
obj.displayinfo(" vishal kumar upadhyay")
'''

# Polomorphism this also concept of overloding
'''
class Ws:
    def displayinfo(self , name=" "):
        print("Welcome to ws cubetech " + name)
        
obj = Ws()
obj.displayinfo()
obj.displayinfo('python')
'''

# polomorphism overriding inheritance concept also opps

class A:
    def displayinfo(self):
        print(" Welcome to ws cube tech ")
        
class B(A):
    def displayinfo(self):
        super().displayinfo()
        print("This is my page with this")
obj = B()
obj.displayinfo()
        