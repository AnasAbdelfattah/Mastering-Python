# Start program

# Create a list of students
students = []

# Add student
def add_student(student_name, student_id, courses, grades):
    student = {
        "name": student_name,
        "id": student_id,
        "courses": courses.split(','),  
        "grades": [int(grade) for grade in grades.split(',')] 
    }

    students.append(student)
    print("Student added successfully!")

# End function

# Remove student
def remove_student(student_id):
    for student in students:
        if student_id == student["id"]:
            students.remove(student)
            print("Student removed successfully!")
            return
    print("Student not found!")

# End function

# Show student information
def show_information(student_id):
    for student in students:
        if student_id == student["id"]:
            print("Information for student:")
            print(f"Name: {student['name']}")
            print(f"ID: {student['id']}")
            print(f"Courses: {', '.join(student['courses'])}")
            print(f"Grades: {', '.join(map(str, student['grades']))}")
            return

    print(f"Student with ID {student_id} not found.")

# End Function

# Display all students and their information.
def display_all_students():
    if not students:
        print("No students available.")
        return

    counter = 1
    for student in students:
        print(f"\nThe student number {counter}:")
        for key, value in student.items():
            print(f"{key.capitalize()}: {value}")
        counter += 1

# End Function 

# Calculate the average grade
def average_grades(student_id):
    for student in students:
        if student_id == student["id"]:
            if not student["grades"]:
                print("No grades available for the student.")
                return

            total_grades = sum(student["grades"])
            average = total_grades / len(student["grades"])
            print(f"The average of grades: {average:.2f}")
            return
    print("Student not found!")

# End of the function

# Start UI
print("---------- Student Information System ----------\n")
run_again = 'y'

while run_again.lower() == 'y':
    print("---------- Choose an Option ----------\n")
    print("1. Add Student\n2. Remove Student\n3. Show Student Information\n4. Calculate the Average Grade\n5. Display All Students")

    order = input("Enter your choice (1-5): ")

    # Start while
    while not order.isdigit() or not (1 <= int(order) <= 5):
        print("Error! Please enter a valid numeric option (1-5).")
        order = input("Enter your choice (1-5): ")
    # End while
    
    # Start if 
    if order == '1':
        student_name = input("Enter the student name: ")
        student_id = input("Enter the student id: ")
        courses = input("Enter the student's courses (comma-separated): ")
        grades = input("Enter the grades of each course (comma-separated): ")
        add_student(student_name, student_id, courses, grades)

    elif order == '2':
        if not students:
            print("No students available for removal.")
        else:
            student_id = input("Enter the student ID to remove: ")
            remove_student(student_id)

    elif order == '3':
        if not students:
            print("No students available for information.")
        else:
            student_id = input("Enter the student ID to display information: ")
            show_information(student_id)

    elif order == '4':
        if not students:
            print("No students available for average calculation.")
        else:
            student_id = input("Enter the student ID to calculate average grade: ")
            average_grades(student_id)

    elif order == '5':
        display_all_students()

    else:
        print("Invalid option!")

    # End if

    run_again = input("Do you want to run another operation? (Y/N): ").lower()
    while run_again not in ['y', 'n']:
        print('Please enter only Y or N: ', end='')
        run_again = input().lower()

print("Goodbye! Exiting the Student Information System.")

# End UI
# End Program
