import pandas as pd

file_path = "csv.csv"
df = pd.read_csv(file_path)

supervisor_dict = {}

for _, row in df.iterrows():
    supervisor = row["Supervisor"]
    employee = row["Employee"]
    
    if supervisor in supervisor_dict:
        supervisor_dict[supervisor].append(employee)
    else:
        supervisor_dict[supervisor] = [employee]

grouped_data = [{"Supervisor": sup, "Employee": ", ".join(emp)} for sup, emp in supervisor_dict.items()]

grouped_df = pd.DataFrame(grouped_data)

print(grouped_df)

output_file = "transformed_supervisor_employee.csv"
grouped_df.to_csv(output_file, index=False)

print(f"Transformed data saved to {output_file}")