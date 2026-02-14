# Input
name = input("Enter student name: ")
m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))

# Calculate
total = m1 + m2 + m3
percentage = (total / 300) * 100

# Grade Logic
if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

# Output
print("-" * 20)
print(name)
print(f"Total: {total}/300")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
