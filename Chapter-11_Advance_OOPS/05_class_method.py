class employee():
    salary="25000"
    @classmethod
    def show_details(cls):
        cls.name="xyz"
        cls.domain="finance"
        print(f"The name is {cls.name} and the salary is {cls.salary}")

a=employee()
a.show_details()
a.salary="0000"
a.show_details()