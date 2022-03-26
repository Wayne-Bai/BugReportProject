import json

num_2017 = 0
num_2018 = 0
num_2019 = 0
num_2020 = 0
num_2021 = 0
num_2022 = 0

with open('commit_git.json','r') as f:
    for line in f.readlines():
        data = json.loads(line)

        no_date = 0

        try:
            date = data["AUTHORED_DATE"]
        except:
            # print(data['date'])
            no_date += 1

        if '2017' in date:
            with open('2017_commit.json', 'a') as w1:
                num_2017 += 1
                w1.write(json.dumps(data))
                w1.write('\n')

        elif '2018' in date:
            with open('2018_commit.json', 'a') as w2:
                num_2018 += 1
                w2.write(json.dumps(data))
                w2.write('\n')

        elif '2019' in date:
            with open('2019_commit.json', 'a') as w3:
                num_2019 += 1
                w3.write(json.dumps(data))
                w3.write('\n')

        elif '2020' in date:
            with open('2020_commit.json', 'a') as w4:
                num_2020 += 1
                w4.write(json.dumps(data))
                w4.write('\n')

        elif '2021' in date:
            with open('2021_commit.json', 'a') as w5:
                num_2021 += 1
                w5.write(json.dumps(data))
                w5.write('\n')

        elif '2022' in date:
            with open('2022_commit.json', 'a') as w6:
                num_2022 += 1
                w6.write(json.dumps(data))
                w6.write('\n')

print(no_date)

print('2017: {}'.format(num_2017))
print('2018: {}'.format(num_2018))
print('2019: {}'.format(num_2019))
print('2020: {}'.format(num_2020))
print('2021: {}'.format(num_2021))
print('2022: {}'.format(num_2022))

f.close()
w1.close()
w2.close()
w3.close()
w4.close()
w5.close()
w6.close()
