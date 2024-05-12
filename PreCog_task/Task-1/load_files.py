import csv


def load_file(filename):
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        headers = next(reader)  # Read the first row as headers
        for row in reader:
            data_dict = dict(zip(headers, row))  # Create a dictionary from headers and row
            data.append(data_dict)
    return data
