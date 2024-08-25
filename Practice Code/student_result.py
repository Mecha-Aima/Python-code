# Ask user for marks of 3 students
marks1 = int(input("Enter student 1 marks : "))
marks2 = int(input("Enter student 2 marks : "))
marks3 = int(input("Enter student 3 marks : "))

# Calculate percentage of each student
p1 = (marks1/75)*100
p2 = (marks2/75)*100
p3 = (marks3/75)*100

# Calculate overall percentage
percent = ((marks1+marks2+marks3))/225 * 100

# Check if student has passed or failed
if(p1>=33 and p2>=33 and p3>=33 and percent>=40):
    print("You have PASSED!")
else:
    print("You have FAILED")

# Print overall percentage
print("Total Percentage : ",percent,"%")
