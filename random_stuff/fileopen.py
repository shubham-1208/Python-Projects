with open("file.py") as f:
    for line in f:
        print(line, end="")



with open("2.txt") as f:
    for line in f:
        number = int(line)  # Here we do the type conversion
        new_number = number + 17  # Here is where we do our "data analysis"
        print(new_number)