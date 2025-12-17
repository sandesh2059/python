student_marks = {'sandesh':[100, 99, 98], 'flins':[89, 88, 90], 'columbina':[98, 77, 99]}
name = input("enter students name: ")

if name in student_marks:
    print("checking results for ", name)
    marks = student_marks[name]
    average = sum(marks) / len(marks)

    if average >= 60:
        print("Congratulations ", name , "has passed the test")
        print("the marks obtained by", name, " is: ", average)
    else:
        print("sorry,", name, " has failed the test")
        print("the marks obtained by", name, " is: ", average)

else:
    print("Student not found") 