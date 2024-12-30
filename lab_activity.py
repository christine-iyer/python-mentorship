import csv

class Member:
     def __init__(self, full_name):
          self.full_name = full_name
          
     def introduce(self):
          print(f"Hi, my name is {self.full_name}")  
             
me=Member("Chris")
me.introduce()

class Student(Member):
     def __init__(self, full_name, reason):
          super().__init__(full_name)
          self.reason=reason
          
class Instructor(Member):
     def __init__(self, full_name, bio):
          super().__init__(full_name)
          self.bio=bio
          self.skills = []
     def add_skill(self,skill):
          self.skills.append(skill)
          print(f"{skill} sssss")
            
you=Instructor("Taffy", "work")
you.add_skill("rowing")  
you.introduce()
  
  
class Workshop:
     def __init__(self, date, subject):
          self.date = date
          self.subject = subject
          self.instructors = []
          self.students = [] 
                            
                            
import csv

members = []
workshops = []

# Load Members
with open("members.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["type"] == "Student":
            members.append(Student(row["full_name"], row["reason_or_bio"]))
        elif row["type"] == "Instructor":
            instructor = Instructor(row["full_name"], row["reason_or_bio"])
            if row["skills"]:
                instructor.skills = row["skills"].split(",")
            members.append(instructor)

# Load Workshops
with open("workshops.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        workshops.append(Workshop(row["date"], row["subject"]))
  
def save_workshops(workshops):
    with open("workshops.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "subject", "students", "instructors"])
        for workshop in workshops:
            students = ";".join([student.full_name for student in workshop.students])
            instructors = ";".join([instructor.full_name for instructor in workshop.instructors])
            writer.writerow([workshop.date, workshop.subject, students, instructors])
                                
                                