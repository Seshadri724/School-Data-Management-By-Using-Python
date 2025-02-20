def student_management_system():
    students = {}

    def add_student():
        name = input("Enter Student Name: ")
        roll_number = input("Enter Roll Number: ")
        if roll_number in students:
            print("Student with this roll number already exists.")
            return

        students[roll_number] = (name, [], set())
        print("Student added successfully!")

    def update_marks():
        roll_number = input("Enter Roll Number: ")
        if roll_number not in students:
            print("Student not found.")
            return

        try:
            marks_str = input("Enter Marks (comma-separated): ")
            marks = [int(m.strip()) for m in marks_str.split(",")]
            students[roll_number] = (students[roll_number][0], marks, students[roll_number][2])
            print("Marks updated successfully!")
        except ValueError:
            print("Invalid Marks Input. Please enter numbers separated by commas.")

    def mark_attendance():
        roll_number = input("Enter Roll Number: ")
        if roll_number not in students:
            print("Student not found.")
            return

        date = input("Enter Attendance Date (YYYY-MM-DD): ")
        students[roll_number][2].add(date)
        print("Attendance recorded successfully!")

    def view_student_details():
        roll_number = input("Enter Roll Number to View Details: ")
        if roll_number not in students:
            print("Student not found.")
            return

        name, marks, attendance = students[roll_number]
        print("Name:", name)
        print("Roll Number:", roll_number)
        print("Marks:", marks)
        if marks:
            average_marks = sum(marks) / len(marks)
            print("Average Marks:", "{:.2f}".format(average_marks))
        else:
            print("Average Marks: N/A")
        print("Attendance:", attendance)

    def delete_student():
        roll_number = input("Enter Roll Number to Delete: ")
        if roll_number not in students:
            print("Student not found.")
            return

        del students[roll_number]
        print("Student record deleted successfully!")

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Marks")
        print("3. Mark Attendance")
        print("4. View Student Details")
        print("5. Delete Student Record")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            update_marks()
        elif choice == '3':
            mark_attendance()
        elif choice == '4':
            view_student_details()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

student_management_system()
