import csv

# Read CSV file
csv_data = []
with open(r'C:\Users\lizes\Documents\FNB dataquest\Code\fnb_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        csv_data.append(row)

# Access data
for row in csv_data[:5]:  # Assuming you want to print first five rows
    print(row)