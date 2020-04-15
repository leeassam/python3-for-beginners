#Working with CSV files
import csv

with open ("contacts.csv") as contacts:
    csv_reader = csv.reader(contacts, delimiter = ",")
    for row in csv_reader:
        print(f'{row[0]} {row[1]} {row[2]} {row[3]}' )

print("\n\n")

#reading CSV into a dictionary
with open ("contacts.csv") as contacts:
    csv_reader = csv.DictReader(contacts)
    for row in csv_reader:
        print(row.keys())
        print(f'{row["name"]} {row["address"]} {row["email"]} {row["phone"] }' )

'''
optional parameters
delimiter - character used to separate each field
quotechar - character used to surround fields
'''

with open ("contacts2.csv") as contacts:
    csv_reader = csv.reader(contacts, delimiter="|", quotechar="'", escapechar="\\")
    for row in csv_reader:
        print (f'{row[0]} {row[1]} {row[2]} {row[3]}')

#writing csv files
with open ("orders.csv", "w") as order_file:
    order_writer = csv.writer(order_file, delimiter=",")

    #Header columns
    order_writer.writerow(['OrderNo', 'ItemId', 'Description', 'Qty'])
    #Data
    order_writer.writerow(['100','34', 'AAA Batteries', 6])
    order_writer.writerow(['200', '43', 'Dish Soap', 1])
    order_writer.writerow(['300', '45', 'Apples', 5])

#writing csv files from a Dictionary with csv
with open ("movies.csv", "w") as csv_file:
    fields = ['title', 'rating', 'runtime']
    writer = csv.DictWriter(csv_file, fieldnames=fields)

    writer.writeheader() # write the header column names
    writer.writerow({'title' : 'Interstellar', 'rating' : 'PG-13', 'runtime' : 169})
    writer.writerow({'title': 'Memento', 'rating': 'R', 'runtime': 120})
    writer.writerow({'title': 'The Dark Knight', 'rating': 'PG-13', 'runtime': 152})

