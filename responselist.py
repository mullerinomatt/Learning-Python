import csv

file_path = "responselist2.csv"
output_file = "transformed_supervisor_employee.csv"

supervisor_dict = {}

with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    for row in reader:
        employee, supervisor = row
        if supervisor in supervisor_dict:
            supervisor_dict[supervisor].append(employee)
        else:
            supervisor_dict[supervisor] = [employee]

with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Supervisor", "Employee"])
    for supervisor, employees in supervisor_dict.items():
        writer.writerow([supervisor, ", ".join(employees)])

print(f"Transformed data saved to {output_file}")