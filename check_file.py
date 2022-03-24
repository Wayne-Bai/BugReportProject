import json

data_list = ['2017', '2018', '2019', '2021', '2022']

count = 0

for i in data_list:

    with open('dataset/' + i+'_email.json', 'r') as f:
        for line in f.readlines():
            count += 1

    print('{}: {}'.format(i,count))

    f.close()