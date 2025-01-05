class Employee:
    def __init__(self ,name, age ,salary , position , hire_date):
        self.name=name
        self.age=age
        self.salary=salary
        self.position=position
        self.hire_date=hire_date

    def __str__(self):
        return f"Emp: {self.name},Postion: {self.position}"
    
    def  __repr__(self):
        return f"Emp:{self.}"