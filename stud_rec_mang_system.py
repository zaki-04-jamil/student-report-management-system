students={}
#each student data is referred an id => unique set
student_ids= set()
#set will not allow duplicates
#courses are fixed in college ==> tuple
courses= ("ECE","MCA","CSE","AI","CSD")

#METHODS

def add_stud():
    sid=int(input("Enter the student id: "))
    if sid in students:
        print("Student id already exist")
        return
    #student details
    name=input("Enter the student's name: ")
    age=int(input("Enter student's age: "))
    branch=input(f"Enter student's branch{courses}")
    marks=float(input("Enter the student's marks:"))
    #each students details must be stored in a dictionary
    student = {
        "Name": name,
        "Age":age,
        "Branch" : branch,
        "Marks" : marks
    } #subdictionary 1 dimensional
    students[sid] = student
    student_ids.add(sid)
    print("Student record added successfully\n")


def view_stud():
    if not students:
        print("Student details are not present")
        return
    print("\nStudent Records")
    for k,v in students.items():
        print(k,v)


def ser_stud():
    sid=int(input("Enter student id:"))
    if sid not in student_ids:
        print("Student not present")
        return
    for x in student_ids:
        if x==sid:
            print("Student is available")
            print("\nStudent Records")
            print(students[sid])


def del_stud():
    sid=int(input("Enter student id:"))
    if sid not in student_ids:
        print("Student not present")
        return
    for x in student_ids:
        if x==sid:
            students.pop(sid)
            print("Student deleted successfully")
            print(students[sid])

while True:
    print("---STUDENT RECORD MANAGEMENT SYSTEM---")
    print("1.Add student")
    print("2.View students")
    print("3.Search student")
    print("4.Delete student")
    print("5.Exiting program")

    choice=int(input("Enter a choice number(1-5): "))
    if(choice==1):
        add_stud()
    elif (choice==2):
        view_stud()
    elif (choice==3):
        ser_stud()
    elif(choice==4):
        del_stud()
    elif(choice==5):
        print("Exiting the application: ")
        break
    else:
        print("Invalid choice")

    