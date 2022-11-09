# with open('test.csv', 'a', encoding='utf-8') as f:
    # f.write('1')
    # f.write(',')
    # f.write('hkw')
    # f.write(',')
    # f.write('0109')
    # f.write(',')

    # f.write('2')
    # f.write(',')
    # f.write('jon')
    # f.write(',')
    # f.write('0110')
    # f.write(',')

# with open('test.csv', 'r', encoding='utf-8') as f:
#     print(f.read())

import pandas as pd

csv_file = pd.read_csv('test.csv')
csv_file.to_excel('test.xlsx', header=True, index=None)



