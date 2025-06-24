class Employee:
    name="Mohini"
    salary="35000"
    phone="7744943700"
    email="arjun@gmail.com"
    
    def display_detail():
        print("Name of Emp:",Employee.name)
        print("Email:",Employee.email)
        print("Salary:",Employee.salary)
    
#calling Function/ Methods
Employee.display_detail()