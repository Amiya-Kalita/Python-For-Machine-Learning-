# --- GOOD variable names ---
first_name = "John"
user_email_address = "john.doe@email.com"
car_speed_kmh = 80
_temporary_variable = 100 # Starting with _ often implies a private or temporary variable

# --- BAD variable names (these will cause errors) ---
# 2_cars = 2           # Error! Cannot start with a number.
# my-variable = "Hi"   # Error! Cannot use hyphens.
# user name = "Jane"   # Error! Cannot have spaces.

# --- BAD but functional names (avoid these) ---
x = "Jane"            # Not descriptive
fn = "Jane"           # Too abbreviated
FirstName = "Jane"    # Not snake_case (this is often called PascalCase)
FIRSTNAME = "Jane"    # Not snake_case (this is often called UPPERCASE)