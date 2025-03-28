import pandas as pd

def propagate_employee_data():
    input_csv = input("Enter the name of the input CSV file (including .csv): ")
    output_csv = input("Enter the name you'd like for the output CSV file (including .csv): ")

    try:
        df = pd.read_csv(input_csv, skiprows=5, skipfooter=2)
        df.dropna(how='all', inplace=True)
        df[['last', 'first', 'middle']] = df['Employee Name'].str.split(', ', expand=True)
        cols_to_fill = df.columns[:2]
        df[cols_to_fill] = df[cols_to_fill].fillna(method='ffill')
        df.to_csv(output_csv, index=False)
        print(f"\nProcessed file saved as: {output_csv}")
    except FileNotFoundError:
        print("\nFile not found. Please make sure the file name is correct and try again.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    propagate_employee_data()