
class employee:
    language="python" 
    company="google"

    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language

        print("I am creating an object")
    def getInfo(self):
        print(f"the language is {self.language} and the company is {self.company}")

    @staticmethod
    def getGreet():
        print("Good Morning")

virendra=employee("vk",21000,"C")
#virendra.language="java" 
"""virendra.getInfo()
employee().getGreet()"""

print(virendra.name,virendra.salary,virendra.language)