import pandas

#recognizes first line of CSV as column names
#uses zero-based indices by default
#converts data-types

box_office = pandas.read_csv('box-office.csv')

print(box_office)

#specify index
box_office = pandas.read_csv('box-office.csv', index_col='Title')

print(box_office)

#forcing dates to be parsed
box_office = pandas.read_csv('box-office.csv', index_col='Title',
                             parse_dates=['Release Date'])

print(box_office)

#specifying column names
box_office = pandas.read_csv('box-office.csv', parse_dates=['Open Date'],
                             header = 0,
                             names = ['Rank', 'Title', 'Open Date', 'Box Office'])

print(box_office)
print(box_office['Title'][0])

#write csv files with pandas
box_office = pandas.read_csv('box-office.csv', parse_dates=['Open Date'],
                             index_col= 'Title',
                             header = 0,
                             names = ['Rank', 'Title', 'Open Date', 'Box Office'])

box_office.to_csv("box-office2.csv")
