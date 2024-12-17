def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f"{prompt}: Invalid input. Sorry error.")  # Using f-string for variable substitution.

# Test the function

print(get_integer_input("HI"))