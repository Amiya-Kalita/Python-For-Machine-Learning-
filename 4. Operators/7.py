# --- Test Scenario 1: Danger! ---
is_armed = True
motion_detected = True
is_maintenance_mode = False

# We check for the danger condition first: is_armed AND motion_detected
danger_condition = is_armed and motion_detected

# The final decision: Is there a danger condition AND we are NOT in maintenance mode?
should_sound_alarm = danger_condition and not is_maintenance_mode

print(f"--- Scenario 1 ---")
print(f"Alarm should sound: {should_sound_alarm}") # Output: True

# --- Test Scenario 2: Safe (Maintenance) ---
is_armed = True
motion_detected = True
is_maintenance_mode = True # The only change

danger_condition = is_armed and motion_detected
should_sound_alarm = danger_condition and not is_maintenance_mode # not True is False

print(f"\n--- Scenario 2 ---")
print(f"Alarm should sound: {should_sound_alarm}") # Output: False