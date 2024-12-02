# Initialize an empty list to store the numbers
numbers = []

# Loop to get 5 numbers from the user
for i in range(1, 6):
    while True:  # Start an inner loop to handle invalid input
        try:
            # Prompt user for input
            num = float(input(f"Enter number {i}: "))  # Use float to allow decimal numbers
            
            # Append the valid number to the list
            numbers.append(num)
            break  # Exit the loop if input is valid
        except ValueError:
            # If input is not a valid number, display an error and prompt again
            print("Invalid input! Please enter a numeric value.")

# Find the maximum value using the max() function
max_value = max(numbers)

# Display the maximum value
print(f"The maximum value is: {max_value}")
