in_string = input("Please enter a string: ")
print((in_string[-2:] * 3).capitalize() if len(in_string) > 1 else "The string you entered must be > 1 character long.")