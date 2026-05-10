n = int(input("Enter number of subjects: "))
total = 0

for i in range(n):
    grade = float(input(f"Enter grade point for subject {i+1}: "))
    total += grade

cgpa = total / n

print("Your CGPA is:", round(cgpa, 2))
