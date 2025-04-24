# Get input from the user
num = input("Enter a number: ")

# Remove any negative sign or decimal point if present
cleaned_num = num.replace("-", "").replace(".", "")

# Count and display the number of digits
print("Total number of digits:", len(cleaned_num))
