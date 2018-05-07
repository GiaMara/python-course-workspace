'''
The program calculates and displays students' average test score and letter grade.
'''
student = 1
studentData = 0
studentList = []
score1 = []
score2 = []
score3 = []
average = 0
totalScore = 0


studentData = int(input("How many students?"+"\n"))

for studentGrades in range (1, studentData+1, 1):
    print("Enter name of student", student,":")
    studentList.append(input())
    student += 1

student = 0
for i in range(1,studentData+1,1):
    print("Enter test 1 for ", studentList[student],":")
    score1.append(float(input()))
    print("Enter test 2 for ", studentList[student],":")
    score2.append(float(input()))
    print("Enter test 3 for ", studentList[student],":")
    score3.append(float(input()))
    student += 1

student = 0
for i in range(1,studentData+1,1):
    totalScore =  score1[student]+score2[student]+score3[student]
    average = totalScore/3
    print()
    print(studentList[student],"'s test average is ", average)
    if average >= 90:
        Grade = "A"
    elif average >= 80:
        Grade = "B"
    elif average >= 70:
        Grade = "C"
    elif average >= 60:
        Grade = "D"
    else:
        Grade = "F"
    print(studentList[student],"'s letter grade is ", Grade)
    student +=1
