# =========================================================
# Student Grade Calculator
# Week 2 Project - Python Developer Internship
# Developed by: Kangana Batghare
# =========================================================

# Import module for saving files
import os

# ANSI color codes for terminal output
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"


# =========================================================
# FUNCTION: Calculate Grade
# =========================================================
def calculate_grade(avg):
    """Returns grade and comment based on average marks"""

    if avg >= 90:
        return "A", "Excellent Performance!"
    elif avg >= 80:
        return "B", "Very Good Work!"
    elif avg >= 70:
        return "C", "Good, Keep Improving."
    elif avg >= 60:
        return "D", "Needs More Practice."
    else:
        return "F", "Failed. Study Harder."


# =========================================================
# FUNCTION: Grade Color
# =========================================================
def get_grade_color(grade):
    """Returns color based on grade"""

    if grade == "A":
        return GREEN
    elif grade == "B":
        return BLUE
    elif grade == "C":
        return YELLOW
    else:
        return RED


# =========================================================
# FUNCTION: Validate Marks Input
# =========================================================
def get_valid_marks(subject):
    """Gets valid marks between 0 and 100"""

    while True:
        try:
            marks = float(input(f"Enter marks for {subject}: "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter numbers only.")


# =========================================================
# FUNCTION: Add Student
# =========================================================
def add_student(student_list):

    print("\n========== ADD STUDENT ==========")

    # Validate name
    while True:
        name = input("Enter student name: ").strip()

        if name != "":
            break
        else:
            print("Name cannot be empty.")

    # Get subject marks
    math = get_valid_marks("Math")
    science = get_valid_marks("Science")
    english = get_valid_marks("English")

    # Calculate average
    average = (math + science + english) / 3

    # Get grade and comment
    grade, comment = calculate_grade(average)

    # Store student data in dictionary
    student = {
        "name": name,
        "math": math,
        "science": science,
        "english": english,
        "average": average,
        "grade": grade,
        "comment": comment
    }

    # Add to list
    student_list.append(student)

    print(f"\nStudent '{name}' added successfully!")


# =========================================================
# FUNCTION: Display Results
# =========================================================
def display_results(student_list):

    if len(student_list) == 0:
        print("\nNo student records found.")
        return

    print("\n" + "=" * 85)
    print("                    STUDENT RESULTS SUMMARY")
    print("=" * 85)

    # Table Header
    print(f"{'Name':<20} {'Math':<10} {'Science':<10} {'English':<10} "
          f"{'Average':<10} {'Grade':<10}")

    print("-" * 85)

    # Display student data
    for student in student_list:

        color = get_grade_color(student["grade"])

        print(
            f"{student['name']:<20} "
            f"{student['math']:<10.1f} "
            f"{student['science']:<10.1f} "
            f"{student['english']:<10.1f} "
            f"{student['average']:<10.1f} "
            f"{color}{student['grade']:<10}{RESET}"
        )

    print("=" * 85)


# =========================================================
# FUNCTION: Show Statistics
# =========================================================
def show_statistics(student_list):

    if len(student_list) == 0:
        print("\nNo data available.")
        return

    averages = []

    for student in student_list:
        averages.append(student["average"])

    class_average = sum(averages) / len(averages)

    highest = max(averages)
    lowest = min(averages)

    # Find topper and lowest student
    for student in student_list:

        if student["average"] == highest:
            topper = student["name"]

        if student["average"] == lowest:
            lowest_student = student["name"]

    print("\n" + "=" * 50)
    print("              CLASS STATISTICS")
    print("=" * 50)

    print(f"Total Students   : {len(student_list)}")
    print(f"Class Average    : {class_average:.2f}")
    print(f"Highest Average  : {highest:.2f} ({topper})")
    print(f"Lowest Average   : {lowest:.2f} ({lowest_student})")

    print("=" * 50)


# =========================================================
# FUNCTION: Search Student
# =========================================================
def search_student(student_list):

    if len(student_list) == 0:
        print("\nNo student records available.")
        return

    search_name = input("\nEnter student name to search: ").strip().lower()

    found = False

    for student in student_list:

        if student["name"].lower() == search_name:

            color = get_grade_color(student["grade"])

            print("\n========== STUDENT DETAILS ==========")
            print(f"Name      : {student['name']}")
            print(f"Math      : {student['math']}")
            print(f"Science   : {student['science']}")
            print(f"English   : {student['english']}")
            print(f"Average   : {student['average']:.2f}")
            print(f"Grade     : {color}{student['grade']}{RESET}")
            print(f"Comment   : {student['comment']}")

            found = True
            break

    if not found:
        print("Student not found.")


# =========================================================
# FUNCTION: Save Results
# =========================================================
def save_to_file(student_list):

    if len(student_list) == 0:
        print("\nNo records to save.")
        return

    filename = "results_sample.txt"

    try:
        with open(filename, "w") as file:

            file.write("STUDENT GRADE REPORT\n")
            file.write("=" * 50 + "\n\n")

            for student in student_list:

                file.write(f"Name     : {student['name']}\n")
                file.write(f"Math     : {student['math']}\n")
                file.write(f"Science  : {student['science']}\n")
                file.write(f"English  : {student['english']}\n")
                file.write(f"Average  : {student['average']:.2f}\n")
                file.write(f"Grade    : {student['grade']}\n")
                file.write(f"Comment  : {student['comment']}\n")
                file.write("-" * 50 + "\n")

        print(f"\nResults saved successfully to '{filename}'")

    except Exception as e:
        print("Error while saving file:", e)


# =========================================================
# FUNCTION: Main Menu
# =========================================================
def main():

    student_list = []

    while True:

        print("\n" + "=" * 50)
        print("         STUDENT GRADE CALCULATOR")
        print("=" * 50)

        print("1. Add Student")
        print("2. Display Results")
        print("3. Show Statistics")
        print("4. Search Student")
        print("5. Save Results to File")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        # Menu operations
        if choice == "1":
            add_student(student_list)

        elif choice == "2":
            display_results(student_list)

        elif choice == "3":
            show_statistics(student_list)

        elif choice == "4":
            search_student(student_list)

        elif choice == "5":
            save_to_file(student_list)

        elif choice == "6":

            print("\nThank you for using Grade Calculator!")
            print("Program Closed.")

            break

        else:
            print("Invalid choice! Please select between 1-6.")


# =========================================================
# PROGRAM START
# =========================================================
if __name__ == "__main__":
    main()