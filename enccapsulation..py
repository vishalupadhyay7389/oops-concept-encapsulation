# class Student():
#     __name = 'vishal'
# obj = Student()
# print(obj.__name)
'''
class Student():
    __name = 'Vishal'
    def __init__(self):
        print(self.__name)
        self.__displayinfo()
    def __displayinfo(self):
        print("welcome to wscube tech")
obj = Student()'''
# Ecapsulation private Variable or private method or functions
'''
class Student:
    __name = "vishal"
    def __init__(self):
        print(self.__name)
        self.__displayinfo()
               
    def __displayinfo(self):
        print("Welcome to ws cubetech ")
obj = Student()
'''

# Getter And Setter in Encapsulations

class Student:
    def __init__(self):
        self.__name = ""
        
    def getname(self):
        return self.__name
    def setname(self , name):
        self.__name = name
        
obj = Student()
obj.setname("Testing")
name = obj.getname()
print(name)



        
                
   
        
        
    
    



