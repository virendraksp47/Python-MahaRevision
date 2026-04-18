class employee():
    company="ITC"

    def show_details(self,name,language,salary):
        self.name=name
        self.language=language
        self.salary=salary
        print(f"The name is {self.name} and the language is {self.language}")

    def salary(self):
        print(f"The salary of {self.name} is {self.salary}")

class programmer(employee):
    company="Microsoft"
    
    def domain(self):
        print(f"The domain of {self.name} is {self.domain}")

a=employee()
print(a.company)
b=programmer()
print(b.company)

print(b.show_details("Alice", "Python", 50000))