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
            
you=Instructor("Taffy", "work")
you.add_skill("rowing")  
  
  
class Workshop:
     def __init__(self, date, subject):
          self.date = date
          self.subject = subject
          self.instructors = []
          self.students = [] 
                                