import json

id = []
with open('id.txt') as f1:
    for line in f1.readlines():
        id.append(line)


commit_list = []

with open("commit_email_mapping.json",'r') as f:
    for line in f.readlines():
        data = json.loads(line)
        if int(json.loads(data['COMMIT'])['DATE'].split('-')[0]) -2021 >= 0:
            commit_list.append(data)

f.close()
f1.close()

number = 0
whole = len(id)

for i in id:
    for j in commit_list:
        commit = json.loads(data['COMMIT'])
        conversation = data['CONVERSATION']
        if i == commit['DATE']:
            number += 1
            for k in conversation:
                print('ID: {}, Public Date: {}'.format(i,k['date']))

print(number)
print(whole)