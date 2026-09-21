import csv
import json

print("---------------------------------------------")
print("          CSV TO JSON CONVERSION")
print("---------------------------------------------")
 
csv_file = "input.csv"
json_file = "output.json"

try: 
    with open(csv_file, "r") as file:
        csv_reader = csv.DictReader(file) 
        data = list(csv_reader) 
        
    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)

    print("---------------------------------------------")
    print("CSV file read successfully.")
    print("Data converted to JSON successfully.")
    print("JSON file created:", json_file)
    print("---------------------------------------------") 

except FileNotFoundError:
    print("---------------------------------------------")
    print("Input CSV file not found!")
    print("---------------------------------------------")
