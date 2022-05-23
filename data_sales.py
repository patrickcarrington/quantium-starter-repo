import csv

with open('data/daily_sales_data_comb.csv', 'r') as inp, open('data/output.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(("sales","date","region"))


with open('data/daily_sales_data_comb.csv', 'r') as inp, open('data/output.csv', 'a') as out:
    writer = csv.writer(out)

    for row in csv.reader(inp):
        row[1] = row[1].replace('$','') #remove dollar sign
        sales = float(row[1]) * int(row[2]) #multiply sales and quantity
        writer.writerow((sales, row[3], row[4])) #write
