nmbr = input("Enter a number: ")

# Validate input
try:
    nmbr = int(nmbr)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# Check if the number is even or odd
if nmbr % 2 == 0:
    print(f"{nmbr} is even.")
else:
    print(f"{nmbr} is odd.")

# Initialize counters
counter1, counter2 = 0, 0

# Increment counters in a loop
for _ in range(5):
    counter1 += 1
    counter2 += 2

print(f"counter1: {counter1}, counter2: {counter2}")