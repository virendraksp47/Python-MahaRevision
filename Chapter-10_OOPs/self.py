
class employee:
    language="python" 
    company="google"
    def getInfo(self):
        print(f"the language is {self.language} and the company is {self.company}")

    @staticmethod
    def getGreet():
        print("Good Morning")

virendra=employee()
virendra.language="java" 
virendra.getInfo()
employee().getGreet()
