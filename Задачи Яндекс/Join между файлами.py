import csv

list_file = input().split()
with open(list_file[0], 'r') as market, open(list_file[1], 'r') as billing:
    list_market = dict(csv.reader(market))
    list_billing = csv.reader(billing)
    for line in list_billing:
        if line[1] in list_market.keys():
            shop = list_market[line[1]]
            print(line[0], shop, line[1], line[2], sep=',')