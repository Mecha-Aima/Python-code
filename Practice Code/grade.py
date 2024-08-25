marks = int(input("Enter student marks :"))
total = 1100
percent  = (marks*100)/total

if(percent>=90 and percent<=100):
    grade = 'A+'
elif(percent>=80 and percent<90):
    grade = 'A'
elif(percent>=70 and percent<80):
    grade = 'B'
elif(percent>=60 and percent<70):
    grade = 'C'
elif(percent>=50 and percent<60):
    grade = 'D'
else:
    grade = 'F'

print("Student percentage :",percent,"%\n","Student's Grade : ",grade)