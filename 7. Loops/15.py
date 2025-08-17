# A dictionary mapping students to their test scores
student_scores = {
    "Alice": 91,
    "Bob": 78,
    "Charlie": 85,
    "Diana": 55,
    "Eve": 99
}

print("--- Student Status Report ---")
# .items() lets you loop over key-value pairs simultaneously
for student, score in student_scores.items():
    if score > 80:
        status = "Passed with Merit"
    elif score > 60:
        status = "Passed"
    else:
        status = "Needs Improvement"
    print(f"{student}: Score {score} -> {status}")