#This program create student grades (dictionary) from student scores (dictionary)
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇
for name in student_scores:
    if student_scores[name] <= 70:
        student_grades[name]= "Fail"
    elif student_scores[name] >=71 and student_scores[name] <=80:
        student_grades[name]= "Acceptable"
    elif student_scores[name] >=81 and student_scores[name] <=90:    
        student_grades[name]= "Exceeds Expectations"
    elif student_scores[name] >=91 and student_scores[name] <=100:    
        student_grades[name]= "Outstanding"
        
    


print(student_grades)
