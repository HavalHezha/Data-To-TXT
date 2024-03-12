# Variables
name = input("what is your name?")
age = input("how old are you?")
city = input("where are you?")

# File name
file_name = "Mydata.txt"

# Open file in write mode
with open(file_name, 'w') as file:
    # Write variables to the file
    file.write("Name: " + name + "\n")
    file.write("Age: " + str(age) + "\n")
    file.write("City: " + city + "\n")

print("Variables written to", file_name)
