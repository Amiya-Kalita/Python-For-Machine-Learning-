score = 85
is_b_grade = score >= 80 and score <= 89
print(f"Score is a B grade (old way): {is_b_grade}") # Output: True

score = 85
# Check if 80 is less than or equal to score, which is less than or equal to 89
is_b_grade_chained = 80 <= score <= 89
print(f"Score is a B grade (chained way): {is_b_grade_chained}") # Output: True

# Let's test with a failing score
score_fail = 75
is_b_grade_fail = 80 <= score_fail <= 89
print(f"Failing score is a B grade? {is_b_grade_fail}") # Output: False