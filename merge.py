import csv

dataset1 = []
dataset2 = []

f = open("iq_9000.csv", "r")
csvreader = csv.reader(f)
for row in csvreader:
    dataset1.append(row)

f = open("data_sorted.csv", "r")
csvreader = csv.reader(f)
for row in csvreader:
    dataset2.append(row)

header1 = dataset1[0]
header2 = dataset2[0]
headers = header1 + header2

merge_data1 = dataset1[1:]
merge_data2 = dataset2[1:]
merge_data = []

for index, datarow in enumerate(merge_data1):
    merge_data.append(merge_data1[index] + merge_data2[index])

f = open("merged.csv", "a+")
csvwriter = csv.writer(f)
csvwriter.writerow(headers)
csvwriter.writerows(merge_data)

#its messed up...but i tried

