#single inheritance
class vehicle:
    def Vehicle_Info(self):
        print('in Parent(vehicle)class')
class car(vehicle):
    def car_info(self):
        print('in child(car) class')
car=car()
car.Vehicle_Info() 
car.car_info()
#multiple inheritance
class Person:
    def person_info(self,name,age):
        print('Inside person class')
        print('Name:',name,'Age:',age)
class Company:
    def company_info(self,company_name,location):
        print('Inside company class')
        print('Name:',company_name,'location:',location)
class Employee(Person,Company):
    def employee_info(self,salary,skill):
        print('Inside Employee class')
        print('Salary:',salary,'Skill',skill)
emp=Employee()
emp.person_info('Jessa',34)
emp.company_info('google','ATL')
emp.employee_info(1220000,'Machine Learning')