try:
    age = int(input("Please enter your age: "))

    # Check if the age is between 10 and 20 (inclusive)
    if 10 <= age <= 20:
        print(f"Your age ({age}) is between 10 and 20 years.")
    else:
        print(f"Your age ({age}) is NOT between 10 and 20 years.")

except ValueError:
    print("Invalid input! Please enter a valid integer for your age.")