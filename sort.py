import csv

data = []

f = open("drawf_2.csv", "r")
csvreader = csv.reader(f)
for row in csvreader:
    data.append(row)

headers = data[0]
drawf_data = data[1:]
for x in drawf_data:
    x[2] = x[2].lower()

drawf_data.sort(key = lambda drawf_data:drawf_data[2])

f = open("data_sorted.csv", "a+")
csvwriter = csv.writer(f)
csvwriter.writerow(headers)
csvwriter.writerows(drawf_data)

with open("data_sorted.csv") as input, open("sorted.csv", "w", newline="") as output:
     writer = csv.writer(output)
     for row in csv.reader(input):
         if any(field.strip()for field in row):
            writer.writerow(row)