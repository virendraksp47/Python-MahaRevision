class method():
    a=1
    @classmethod
    def num(cls):
        print(f"The value of a is {cls.a}")

    @property
    def name(self):
        print(f"{self.fname} {self.lname}")

    @name.setter
    def name(self,name):
        self.fname= name.split(" ")[0]
        self.lname= name.split(" ")[1]

e=method()
e.name="satyarth kumar"
e.name
print(e.fname)