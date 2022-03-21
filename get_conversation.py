import json

total_email = []

with open("temp_fix_total.json",'r') as f:
    for line in f.readlines():
        data = json.loads(line)
        total_email.append(data)
f.close()

total_conversation = []
for i in range(len(total_email)):
    if 'Re:' not in total_email[i]['subject'][0]:
        temp = []
        temp.append(total_email[i])
        for j in range(i+1, len(total_email)):
            if total_email[i]['subject'][0] in total_email[j]['subject'][0]:
                temp.append(total_email[j])
        total_conversation.append(temp)
print(len(total_conversation))
print(total_conversation[1])
