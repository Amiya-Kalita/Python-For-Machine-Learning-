score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B" # This block runs since 85 >= 80
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")