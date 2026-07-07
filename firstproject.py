students = []
while True:
    print("\n" + "=" * 45)
    print("        STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")
    print("=" * 45)    

    choice = int(input("Enter your choice: "))

    if choice == 1:
        student = []
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        student.append(name)
        student.append(age)
        students.append(student)
        print("\nStudent Added Successfully")
        print("----------------------------")
        print("Name :", name)
        print("Age  :", age)
        print("----------------------------")

    elif choice == 2:
        if len(students) == 0:
            print("\nNo Students Available")
        else:
            count = 1
            for student in students:
                print("----------------------------")
                print("Student", count)
                print("Name :", student[0])
                print("Age  :", student[1])
                print("----------------------------")
                print()
                count += 1
                
    elif choice == 3:
        search_name = input("Enter Student Name: ")    
        found = False
        for student in students :
            if student[0] == search_name:
                print("\nStudent Found")
                print("----------------------------")
                print("Name :", student[0])
                print("Age  :", student[1])
                print("----------------------------")
                found = True
                break
        if found == False:
            print("\n----------------------------")
            print("Student Not Found")
            print("----------------------------")   

    elif choice == 4:
        delete_name = input("Enter Student Name: ")
        found = False
        for student in students:
            if student[0] == delete_name:
                students.remove(student)
                found = True
                print("\nStudent Deleted Successfully")
                break
        if found == False:
            print("\n----------------------------")
            print("Student Not Found")
            print("Nothing Was Deleted")
            print("----------------------------")
    
    elif choice == 5:
        update_name = input("Enter Student Name: ")
        found = False
        for student in students:
            if student[0] == update_name:
                new_name = input("New Name: ")
                new_age = int(input("New Age: "))
                student[0] = new_name
                student[1] = new_age
                found = True
                print("\nStudent Updated Successfully")
                print("----------------------------")
                print("Name :", student[0])
                print("Age  :", student[1])
                print("----------------------------")
                break
        if found == False:
            print("\n----------------------------")
            print("Student Not Found")
            print("Nothing Was Updated")
            print("----------------------------")           
    
    elif choice == 6:
        print("\n====================================")
        print("Thank You For Using")
        print("Student Management System")
        print("====================================")
        break
    else:
        print("\n----------------------------")
        print("Invalid Choice")
        print("Please Enter A Number Between 1 And 6")
        print("----------------------------")