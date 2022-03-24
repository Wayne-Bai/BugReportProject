import json

with open('whole_email.json','r') as f:
    for line in f.readlines():
        data = json.loads(line)

        no_date = 0

        try:
            date = data['date'][0].split()
        except:
            # print(data['date'])
            no_date += 1

        if '2017' in date:
            with open('2017_email.json', 'a') as w1:
                w1.write(json.dumps(data))
                w1.write('\n')

        elif '2018' in date:
            with open('2018_email.json', 'a') as w2:
                w2.write(json.dumps(data))
                w2.write('\n')

        elif '2019' in date:
            with open('2019_email_v1.json', 'a') as w3:
                w3.write(json.dumps(data))
                w3.write('\n')

print(no_date)

f.close()
w1.close()
w2.close()
w3.close()
