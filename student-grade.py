students = []

while True:
    print("\n--- Student Grade Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        marks = []
        for i in range(5):
            mark = float(input(f"Enter marks for subject {i + 1}: "))
            marks.append(mark)

        total = sum(marks)
        average = total / len(marks)
        percentage = (total / 500) * 100

        if percentage >= 90:
            grade = "A"
        elif percentage >= 80:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 60:
            grade = "D"
        else:
            grade = "F"

        student = {
            "name": name,
            "marks": marks,
            "total": total,
            "average": average,
            "percentage": percentage,
            "grade": grade
        }

        students.append(student)

        print("\nStudent added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("\nNo students found.")
        else:
            print("\n--- Student Details ---")

            for student in students:
                print("\nName:", student["name"])
                print("Marks:", student["marks"])
                print("Total:", student["total"])
                print("Average:", student["average"])
                print("Percentage:", student["percentage"], "%")
                print("Grade:", student["grade"])

    elif choice == "3":
        search_name = input("Enter student name to search: ")

        found = False

        for student in students:
            if student["name"].lower() == search_name.lower():
                print("\nStudent Found!")
                print("Name:", student["name"])
                print("Marks:", student["marks"])
                print("Total:", student["total"])
                print("Average:", student["average"])
                print("Percentage:", student["percentage"], "%")
                print("Grade:", student["grade"])

                found = True
                break

        if not found:
            print("\nStudent not found.")

    elif choice == "4":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice. Please try again.")
