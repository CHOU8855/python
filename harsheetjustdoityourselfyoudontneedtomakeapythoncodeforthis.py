
num_input = input("Enter a number: ")


num_str = num_input.lstrip("+-")


if num_str.isdigit():
    
    num_digits = len(num_str)
    print(f"The total number of digits in {num_input} is: {num_digits}")
else:
    print("Invalid input! Please enter a valid integer number.")
