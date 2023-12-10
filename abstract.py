from abc import ABCMeta,abstractclassmethod
class person(metaclass=ABCMeta):
    nbr=0
    def __init__(self ,name ,age , code, last_name ) :
        self.name =name
        self.age =age
        self.code =code
        self.last_name =last_name
        person.nbr+= 1
    @property
    def Name(self):
        return self.name 
    def getLast_name(self):
        return self.last_name 
    def getCode(self):
        return self.code
    @Name.setter
    def Name(self , name):
        self.name =name
    
    def setLast_name(self,last_name):
        self.last_name = last_name

    def setCode(self,code):
        self.code =code
    def setName(self ,name):
        self.name =name
    @abstractclassmethod
    def equals(self):
     pass
    @abstractclassmethod
    def tostring(self):
        pass

class employee(person):
   
    def ___init__(self,name ,age , code, last_name,grade):
     super().__init__(self,name,age ,code ,last_name)
     self.grade= grade
     
    def tostring(self):
       print("name",{self.name},"last_name",{self.last_name},"age",{self.age},"code",{self.code})

    def equals(self ,code):
        return self.code == code
    
class student (person ):
   
    def ___init__(self,moyenne , niveau,name ,age , code, last_name):
        super().__init__(name ,age , code, last_name)
        self.moyenne =moyenne
        self.niveau = niveau
       
      

    def tosrtring(self):
       print("name",{self.name},"last_name",{self.last_name},"age",{self.age},"code",{self.code},"moyen",{self.moyenne},"niveau",{self.niveau})
        
var1=employee("sara","20","12","nour")
print( var1.tostring())

var2=student("nour","hoda","15","0000","12","bac")
print( var2.tostring())




