import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    # Write header row
    writer.writerow(["Name", "Age", "City"])
    
    # Write data rows
    writer.writerow(["Ali", 25, "Lahore"])
    writer.writerow(["Sara", 22, "Karachi"])
    writer.writerow(["Ahmed", 28, "Islamabad"])

print("CSV file created!")