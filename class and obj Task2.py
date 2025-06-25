# Homework
# Student has features like name, roll and subjects with marks.
# There are 5 subjects for every students with some marks.
# Student has one operation which will display percentage of student.
# Use Dictornary for subject and marks

class Student:
    def __init__(self,name,roll,subjects):
        self.name=name
        self.roll=roll
        self.subjects=subjects
    
    def display_percentage(self):
        total_marks=sum(self.subjects.values())
        percentage = total_marks/len(self.subjects)
        
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("Subjects:",self.subjects)
        print("Total:",total_marks)
        print("Percentage:",percentage)
        
name=input("Enter Student Name:")
roll=input("Enter Roll Number:")
        
subject_marks={}

print("Enter your subjects Names and Marks:\n")
for i in range(1,6):
    subject=input(f"Enter Subject{i}:")
    marks=int(input(f"Marks for Subject{i}:"))
    subject_marks[subject]=marks

s1=Student(name,roll,subject_marks)
s1.display_percentage()

# Output:
# Enter Student Name:Mohini
# Enter Roll Number:23
# Enter your subjects Names and Marks:

# Enter Subject1:Computer Graphics
# Marks for Subject1:88
# Enter Subject2:Reaserch
# Marks for Subject2:98
# Enter Subject3:DBMS
# Marks for Subject3:78
# Enter Subject4:Os
# Marks for Subject4:70
# Enter Subject5:Software Engineering
# Marks for Subject5:89
# Name: Mohini
# Roll: 23
# Subjects: {'Computer Graphics': 88, 'Reaserch ': 98, 'DBMS': 78, 'Os': 70, 'Software Engineering': 89}
# Total: 423
# Percentage: 84.6
          
    
    
    

        
        
        