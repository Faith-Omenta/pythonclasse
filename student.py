class Student:
    name="Glenah"
    first_name="Faith"
    last_name="Omenta"
    age=22
    school="akiraChix"
    country="Kenya"
    nationality="Kenyan"

class Student:
    school="AkiraChix"
    def __init__(self,first_name,last_name,name,age,country,nationality):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.name=name
        self.country=country
        self.nationality=nationality
        
        

    def greet_student(self):

        return f"Hello {self.name},welcome to {self.school},proudly {self.nationality}"
    
# Update the Student Class to include these attributes 
# - first_name, last_name, age, country
# Add these methods to the Student class 
            #  show_full_name
            #  - year_of_birth
            #  - show_initials
    def show_full_name(self):
        return f"Hello,My name is {self.first_name} {self.last_name}"
    
    def year_of_birth(self):
        return f"I was born in {self.year_of_birth}"
    
    def show_initials(self):
        return f"My initials are{self.first_name[0].upper} {self.last_name[0].upper} "
    
#  Create 3 files in the classes directory car.py, fruit.py, and bank.py.
#  Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.

# come up with the attributes and three methods (behaviours)
#  for each class and implement them

# Then do the following in the interpreter 
# Create two instances of each class. 
# Call each of the methods you defined.




  
    
       