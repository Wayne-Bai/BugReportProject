import json

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
                w1.write(json.dumps(data))
                w1.write('\n')

        elif '2018' in date:
            with open('2018_commit.json', 'a') as w2:
                w2.write(json.dumps(data))
                w2.write('\n')

        elif '2019' in date:
            with open('2019_commit.json', 'a') as w3:
                w3.write(json.dumps(data))
                w3.write('\n')

        elif '2020' in date:
            with open('2020_commit.json', 'a') as w4:
                w4.write(json.dumps(data))
                w4.write('\n')

        elif '2021' in date:
            with open('2021_commit.json', 'a') as w5:
                w5.write(json.dumps(data))
                w5.write('\n')

        elif '2022' in date:
            with open('2022_commit.json', 'a') as w6:
                w6.write(json.dumps(data))
                w6.write('\n')

print(no_date)

f.close()
w1.close()
w2.close()
w3.close()
w4.close()
w5.close()
w6.close()
