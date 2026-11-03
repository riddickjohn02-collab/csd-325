# Name: Robert Cuevas
# Date: September 22, 2026
# Assignment: Student Cumulative GPA
# Purpose: This program uses a Student class to calculate and
# display a student's cumulative GPA.


class Student:
    # Initialize the student object
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.total_credits = 0
        self.total_grade_points = 0

    # Add a course to the student's GPA calculation
    def add_course(self, credits, grade):
        grade_values = {
            "A": 4.0,
            "B": 3.0,
            "C": 2.0,
            "D": 1.0,
            "F": 0.0
        }

        grade_points = grade_values[grade] * credits

        self.total_credits += credits
        self.total_grade_points += grade_points

    # Calculate the student's cumulative GPA
    def calculate_gpa(self):
        if self.total_credits == 0:
            return 0.0

        return self.total_grade_points / self.total_credits

    # Display the student's cumulative GPA
    def display_gpa(self):
        gpa = self.calculate_gpa()

        print("\n----- Student GPA -----")
        print(f"Student: {self.first_name} {self.last_name}")
        print(f"Total credits: {self.total_credits}")
        print(f"Cumulative GPA: {gpa:.2f}")
        print("-----------------------")


# Display a welcome message
print("Student Cumulative GPA Calculator")

# Get the student's name
first_name = input("Enter the student's first name: ")
last_name = input("Enter the student's last name: ")

# Create the Student object
student = Student(first_name, last_name)

# Enter course information
while True:
    try:
        credits = float(input("\nEnter the number of credits for the course: "))

        if credits <= 0:
            print("Credits must be greater than 0.")
            continue

        grade = input("Enter the course grade (A, B, C, D, or F): ").upper()

        if grade not in ["A", "B", "C", "D", "F"]:
            print("Invalid grade. Please enter A, B, C, D, or F.")
            continue

        # Add the course using the Student class method
        student.add_course(credits, grade)

        another_course = input("Would you like to enter another course? (yes/no): ").lower()

        if another_course != "yes":
            break

    except ValueError:
        print("Invalid input. Please enter a numeric value for credits.")

# Display the final cumulative GPA
student.display_gpa()