import csv
with open('data/daily_sales_data_0.csv', 'r') as inp, open('data/daily_sales_data_comb.csv', 'w') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[0] == "pink morsel":
            writer.writerow(row)

with open('data/daily_sales_data_1.csv', 'r') as inp, open('data/daily_sales_data_comb.csv', 'a') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[0] == "pink morsel":
            writer.writerow(row)

with open('data/daily_sales_data_2.csv', 'r') as inp, open('data/daily_sales_data_comb.csv', 'a') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[0] == "pink morsel":
            writer.writerow(row)


