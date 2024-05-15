class Student:
    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
        if self.district_code == 'I':
            tuition_rate = 250.00
        else:
            tuition_rate = 500.00
        return self.enrolled_credits * tuition_rate

    def get_details(self):
        return (f"Student Name: {self.first_name} {self.last_name}, "
                f"District Code: {self.district_code}, "
                f"Enrolled Credits: {self.enrolled_credits}")

# Create an instance of Student
student = Student("Jane", "Doe", "O", 12)

# Display student details
print(student.get_details())

# Compute and display the tuition owed
tuition = student.compute_tuition()
print(f"Tuition Owed: ${tuition:.2f}")
