import json

with open('total_conversation.json', 'r') as f:
    num_2017 = 0
    num_2018 = 0
    num_2019 = 0
    num_2020 = 0
    num_2021 = 0
    num_2022 = 0
    num_undefine = 0
    for line in f.readlines():
        data = json.loads(line)
        if data['date'][0]:
            if data['date'][0][0].split()[3] == '2017':
                num_2017 += 1
            elif data['date'][0][0].split()[3] == '2018':
                num_2018 += 1
            elif data['date'][0][0].split()[3] == '2019':
                num_2019 += 1
            elif data['date'][0][0].split()[3] == '2020':
                num_2020 += 1
            elif data['date'][0][0].split()[3] == '2021':
                num_2021 += 1
            elif data['date'][0][0].split()[3] == '2022':
                num_2022 += 1
        else:
            num_undefine += 1
    print('2017: {}'.format(num_2017))
    print('2018: {}'.format(num_2018))
    print('2019: {}'.format(num_2019))
    print('2020: {}'.format(num_2020))
    print('2021: {}'.format(num_2021))
    print('2022: {}'.format(num_2022))
    print('undefine: {}'.format(num_undefine))
f.close()