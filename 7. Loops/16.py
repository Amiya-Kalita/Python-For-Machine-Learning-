# Employees who worked on Project A
project_a_staff = ["Alice", "Bob", "Frank", "Grace"]
# Employees who worked on Project B
project_b_staff = ["Charlie", "Diana", "Frank", "Eve", "Alice"]

common_staff = []

print("Searching for staff who worked on both projects...")
# Outer loop: iterate through staff from Project A
for staff_a in project_a_staff:
    # Inner loop: iterate through staff from Project B
    for staff_b in project_b_staff:
        # Compare the staff member from A to the one from B
        if staff_a == staff_b:
            print(f"Match found: {staff_a}")
            common_staff.append(staff_a)
            break # Optimization: once a match is found, stop checking this staff_a against the rest of B

print(f"\nStaff on both projects: {common_staff}")