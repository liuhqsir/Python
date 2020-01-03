import csv

with open('example.csv','r') as rf:
    reader = csv.reader(rf)
    with open('new.csv','w') as wf:
        writer = csv.writer(wf)
        headers = next(reader)
        writer.writerow(headers)
        for row in reader:
            if row[0] < '2016-01-01':
                continue
            if int(row[5]) >= 50:
                writer.writerow(row)


print('end')
