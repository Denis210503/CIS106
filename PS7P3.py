student_count = 0

while True:
    choice = input("Do you want to continue? (Enter 'Yes' to continue): ")
    if choice.lower() == "yes":
        last_name = input("Enter your last name: ")
        exam1 = float(input("Enter your first exam score: "))
        exam2 = float(input("Enter your second exam score: "))

        average_score = (exam1 + exam2) / 2

        print(f"Last Name: {last_name}, Average Score: {average_score}")

        student_count += 1

        again = input("enter data for another student? (Enter 'Yes' to continue): ")
        if again.lower() != "yes":
            break
    else:
        break

print(f"Number of students who entered data: {student_count}")
