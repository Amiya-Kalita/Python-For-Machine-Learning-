user_role = "editor" # Try changing this to "admin", "viewer", or "guest"

if user_role == "admin":
    print("Welcome, Admin! You have full access to all settings.")
elif user_role == "editor":
    print("Welcome, Editor! You can create and edit content.")
elif user_role == "viewer":
    print("Welcome, Viewer! You can view content but cannot make changes.")
else:
    print("Welcome, Guest! Your access is limited. Please log in or sign up.")