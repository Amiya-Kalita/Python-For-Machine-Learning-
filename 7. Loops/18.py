# A list where each element is a list of participants for an event
weekly_participants = [
    ["Alice", "Bob"],
    ["Charlie", "Diana", "Eve"],
    ["Frank"]
]

all_participants = []

# Outer loop iterates through each week's list
for weekly_list in weekly_participants:
    # Inner loop iterates through each name in the current week's list
    for participant in weekly_list:
        all_participants.append(participant)

print(f"Original nested data: {weekly_participants}")
print(f"Flattened list of all participants: {all_participants}")