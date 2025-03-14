import csv

class Member:
     def __init__(self, full_name):
          self.full_name = full_name
          
     def introduce(self):
          print(f"Hi, this is me {self.full_name}")     
          
chris = Member("Chris")
chris.introduce()

class Student(Member):
     def __init__(self, full_name, reason):
          super().__init__(full_name)
          self.reason = reason 

class Instructor(Member):                    
     def __init__(self, full_name, bio):
          super().__init__(full_name)
          self.bio = bio
          self.skills = []    
     def add_skill(self, skill):
          self.skills.append(skill)
          print(f"{skill} ssss")                   
          
paul=Instructor("Paul", "figheting fires")  
paul.add_skill("building decks and siding houses. I'm modest") 
paul.intruduce()

class Workshop:
     def __init__(self, date, subject):
          self.date = date
          self.subject = subject
          self.instructors = []
          self.students = []

     members = []
     workshops = []

     with open("members.csv", mode = "r") as file:
          reader = csv.DictReader(file)
          for row in reader:
               if row["type"]== "Student":
                    members.append(Student(row["full_name"], row["reason_or_bio"]))
               elif row["type"] == "Instructor":
                    members.append(Instructor(row["full_name"], row["reason_or bio"])) 
                        

