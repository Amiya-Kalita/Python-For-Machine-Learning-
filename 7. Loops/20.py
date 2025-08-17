# Simulate a robot's battery draining while it performs a task
battery_level = 95.0 # Starting battery percentage
tasks_completed = 0

# The robot works as long as its battery is above 20%
while battery_level > 20.0:
    print(f"Battery: {battery_level:.1f}% - Robot is working...")
    
    # Each task consumes a bit of battery
    tasks_completed += 1
    battery_level -= 4.5 # Decrease battery by 4.5% per task
    
print("\nBattery below 20%. Robot is returning to charging station.")
print(f"Total tasks completed: {tasks_completed}")