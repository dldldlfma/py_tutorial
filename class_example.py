class Person:
    def __init__(self,name,age):
        self.name =name
        self.age =age
    def print_info(self):
        print(self.name, self.age)

class Employee(Person):
    def __init__(self,name=None,age=None,selary=None,Number='x'):
        super().__init__(name,age)
        self.No = Number
        self.selary = selary
    
    def print_info2(self):
        print(self.name, self.age,self.selary,self.No)

    def __add__(self, value):
        print(self.name,value)
    
    def __str__(self):
        v=str(self.age)
        return v

    

if __name__ == "__main__":
    a = Employee('ksg',29,4000,5)
    #a = Employee('ksg')
    a.print_info()
    a.print_info2()
    print(a)
    print(dir(a))