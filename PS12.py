# Step 1: Prompt the user for a number to create a list of integers
num_items = int(input("Enter the number of items in the list: "))
integer_list = []

for _ in range(num_items):
    number = int(input("Enter an integer: "))
    integer_list.append(number)

print("Initial list:", integer_list)

# Step 2: Insert the score of 99 at position 1
integer_list.insert(1, 99)
print("List after inserting 99 at position 1:", integer_list)

# Step 3: Replace the value of 99 with 100
index_99 = integer_list.index(99)
integer_list[index_99] = 100
print("List after replacing 99 with 100:", integer_list)

# Step 4: Create a second list and extend the first list
second_list = [500, 600, 700, 800, 900]
print("Second list:", second_list)
integer_list.extend(second_list)
print("First list after extending with second list:", integer_list)

# Step 5: Remove the value 800 from the first list
integer_list.remove(800)
print("First list after removing 800:", integer_list)

# Step 6: Remove the third item from the first list
del integer_list[2]
print("First list after removing the third item:", integer_list)

# Step 7: Create a list of grades
grades = ["A", "B", "C", "A", "A", "C"]

# Step 8: Display a count of the number of A grades
count_A = grades.count("A")
print("Number of A grades:", count_A)

# Step 9: Display the index of the first B grade
index_B = grades.index("B")
print("Index of the first B grade:", index_B)

# Step 10: Check for grade F in the grades list
if "F" in grades:
    print("Grade F is in the list.")
else:
    print("Grade F is not in the list.")

# Step 11: Clear the second list of integers
second_list.clear()
print("Second list after clearing:", second_list)

# Step 12: Delete the second list and try to display it
del second_list
try:
    print(second_list)
except NameError:
    print("The second list no longer exists.")

# Step 13: Create a list of players
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

# Step 14: Sort the list of players
players.sort()
print("Sorted list of players:", players)

# Step 15: Make a copy of the list of players
players2 = players.copy()
print("Copy of the list of players (players2):", players2)

# Step 16: Reverse the order of players2
players2.reverse()
print("Original players list:", players)
print("Reversed players2 list:", players2)
