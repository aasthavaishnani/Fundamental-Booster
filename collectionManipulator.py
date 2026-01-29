print("Welcome to the Student Data Organizer!")
print("Manage student records easily.")

students = []
id = 101

while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("0. Exit")

    choice = input("Enter your choice: ")

    #add student
    if choice == '1':
        print("\nEnter Student Details as following ...")
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        subjects = set(input("Subjects (comma-separated): ").split(','))
        dob = input("Date of Birth (DD-MM-YYYY): ")

        student = {
            "id": (id,),
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects,
            "dob": (dob,)
        }
        students.append(student)
        print("Student added successfully!")
        id += 1

    #display all students
    elif choice == '2':
        if not students:
            print("\nNo student records found.\n")
        else:
            print("1. Show all students")
            print("2. Show student by ID")
            sub_choice = input("Enter your choice (1 or 2): ")

            # Show all students
            if sub_choice == '1':
                print("\nAll Students:")
                for s in students:
                    print(
                        f"ID: {s['id'][0]}, \n"
                        f"  Name: {s['name']} \n"
                        f"  Age: {s['age']} \n"
                        f"  Grade: {s['grade']} \n"
                        f"  Subjects: {', '.join(s['subjects'])}\n"
                        f"  DOB: {s['dob'][0]}\n"
                    )

            # Show student by ID
            elif sub_choice == '2':
                sid = int(input("Enter student ID: "))
                for s in students:
                    if s['id'][0] == sid:
                        print(
                            f"\nID: {s['id'][0]}\n"
                            f"  Name: {s['name']}\n"
                            f"  Age: {s['age']}\n"
                            f"  Grade: {s['grade']}\n"
                            f"  Subjects: {', '.join(s['subjects'])}\n"
                            f"  DOB: {s['dob'][0]}"
                        )
                        break
                else:
                    print("Student ID not found.")
            else:
                print("Invalid option.")
    #update student information
    elif choice == '3':
        if not students:
            print("\nNo student records found.\n")
        else:
            sid = int(input("Enter student ID to update: "))
            for s in students:
                if s['id'][0] == sid:
                    new_age = input(f"New age (current {s['age']}): ")
                    if new_age:
                        s['age'] = int(new_age)

                    new_subjects = input(f"New subjects (current {', '.join(s['subjects'])}): ")
                    if new_subjects:
                        s['subjects'] = set(new_subjects.split(','))

                    print("Student Details updated successfully!")
                    break
            else:
                print("Student ID not found.")

    #delete student
    elif choice == '4':
        if not students:
            print("\nNo student records found.\n")
        else:
            sid = int(input("Enter student ID to delete: "))
            for s in students :
                if s['id'] == sid:
                    students.remove(s)
                    print("Student deleted successfully!")
                    break
            else:
                print("Student ID not found.")

    #display subjects offered
    elif choice == '5':
        if not students:
            print("\nNo student records found so no subject offered.\n")
        else:
            all_subjects = set()
            for s in students:
                all_subjects.update(s['subjects'])

            if all_subjects:
                print("Subjects Offered:", ', '.join(all_subjects))
            else:
                print("No subjects available.")

    #exit
    elif choice == '0':
        print("Thank you for using the Student Data Organizer. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")