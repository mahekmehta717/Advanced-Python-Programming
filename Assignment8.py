file = open("input.txt", "r")

lines = file.readlines()

file.close()

print("Total number of lines:", len(lines))

first_two_lines = lines[:2]

output_file = open("output.txt", "w")

output_file.writelines(first_two_lines)

output_file.close()

print("First two lines have been written to output.txt")
