import csv

def add_column_to_csv(input_filename, output_filename, column_name, default_value=''):
    """Adds a new column to a CSV file.

    Args:
        input_filename (str): Path to the input CSV file.
        output_filename (str): Path to the output CSV file.
        column_name (str): Name of the new column.
        default_value (str, optional): Default value for the new column. Defaults to ''.
    """
    with open(input_filename, 'r') as infile, open(output_filename, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Read the header row
        header = next(reader)

        # Write the new header with the added column
        writer.writerow(header + [column_name])

        # Iterate through the rows, add the default value, and write to the new file
        for row in reader:
            writer.writerow(row + [default_value])