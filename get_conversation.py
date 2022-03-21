import json

total_email = []

with open("2022_fix_total.json",'r') as f:
    for line in f.readlines():
        data = json.loads(line)
        total_email.append(data)
f.close()

print(len(total_email))

total_conversation = []
for i in range(len(total_email)):
    if 'Re:' not in total_email[i]['subject'][0]:
        temp = []
        temp.append(total_email[i])
        for j in range(i+1, len(total_email)):
            if total_email[i]['subject'][0] in total_email[j]['subject'][0]:
                temp.append(total_email[j])
        # print(temp)
        total_conversation.append(temp)

print(len(total_conversation))

# map to same author

email_map = {}
for email in total_conversation:
    first_email = email[0]
    if first_email['author']:
        author = first_email['author'][0]
    else:
        author = 'N/A'
    if author not in email_map.keys():
        email_map[author] = []
        email_map[author].append(email)
    else:
        email_map[author].append(email)

print(len(email_map.keys()))

for key,value in email_map.items():
    print("Author: {}, Submit Number: {}".format(key, len(value)))

# print(email_map.keys())
