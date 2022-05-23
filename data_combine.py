import csv


with open('data/daily_sales_data_0.csv', 'r') as inp, open('data/daily_sales_data_comb.csv', 'w') as out: #'w' to create daily_sales_data_comb
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[0] == "pink morsel": #only find pink morsel sales
            writer.writerow(row) #write row if a pink morsel sale

with open('data/daily_sales_data_1.csv', 'r') as inp, open('data/daily_sales_data_comb.csv', 'a') as out: #'a' to append to daily_sales_data_comb
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[0] == "pink morsel": #only find pink morsel sales
            writer.writerow(row) #write row if a pink morsel sale

with open('data/daily_sales_data_2.csv', 'r') as inp, open('data/daily_sales_data_comb.csv', 'a') as out: #'a' to append to daily_sales_data_comb
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[0] == "pink morsel":#only find pink morsel sales
            writer.writerow(row) #write row if a pink morsel sale


