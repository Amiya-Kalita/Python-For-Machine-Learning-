# Ask for user data in a specific format
user_info = input("Enter your Name, Age, and City (separated by commas): ")

# Split the string by the comma and a space to get individual parts
name, age, city = user_info.split(", ")

# Display the separated data
print("\n--- User Data Parsed ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")