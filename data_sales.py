import csv

with open('data/daily_sales_data_comb.csv', 'r') as inp, open('data/output.csv', 'w') as out:
    writer = csv.writer(out)

    for row in csv.reader(inp):
        row[1] = row[1].replace('$','')
        sales = float(row[1]) * int(row[2])
        writer.writerow((sales, row[3], row[4]))