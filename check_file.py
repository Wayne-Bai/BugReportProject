import json

file_type = 'commit'

if file_type == 'email':

    data_list = ['2017', '2018', '2019', '2021', '2022']

    count = 0

    for i in data_list:

        with open('dataset/' + i+'_email.json', 'r') as f:
            for line in f.readlines():
                count += 1

        print('{}: {}'.format(i,count))

        f.close()

elif file_type == 'commit':

    data_list = ['2017', '2018', '2019', '2020', '2021', '2022']

    count = 0

    for i in data_list:

        with open(i + '_commit.json', 'r') as f:
            for line in f.readlines():
                count += 1

        print('{}: {}'.format(i, count))

        f.close()