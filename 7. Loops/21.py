import time

attempts = 0
max_attempts = 4
connection_successful = False

# Keep trying as long as we have attempts left AND we haven't connected
while attempts < max_attempts and not connection_successful:
    print(f"Attempt {attempts + 1}: Trying to connect to the server...")
    attempts += 1
    
    # In a real app, this is where you'd make a network request.
    # We will simulate a failure on the first two attempts.
    if attempts <= 2:
        print("Connection failed. Retrying in 2 seconds...")
        time.sleep(2) # Wait for 2 seconds before retrying
    else:
        connection_successful = True # Simulate a successful connection

# After the loop, check why it ended
if connection_successful:
    print("\n✅ Successfully connected to the server!")
else:
    print("\n❌ Failed to connect after several attempts.")