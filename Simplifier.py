import csv
from collections import defaultdict

# Create a dictionary to store the count of each (latitude, longitude) pair.
coord_counts = defaultdict(int)

# Read the input CSV file.
with open('input1.csv', 'r', newline='') as infile:
    reader = csv.reader(infile)
    # If your CSV file contains a header, uncomment the next line to skip it.
    next(reader)
    for row in reader:
        # Skip empty rows.
        if not row:
            continue
        # Assuming the CSV rows are formatted as: latitude,longitude
        latitude = row[0].strip()
        longitude = row[1].strip()
        coord_counts[(latitude, longitude)] += 1

# Write the results to the output CSV file.
with open('output1.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    for (lat, lon), count in coord_counts.items():
        writer.writerow([lat, lon, count])
