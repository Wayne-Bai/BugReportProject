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

author_map = {}
value_list = []
for key,value in email_map.items():
    # print("Author: {}, Submit Number: {}".format(key, len(value)))
    author_map[key] = len(value)
    value_list.append(len(value))

print(min(value_list))
print(max(value_list))

number_map = {}
for i in range(min(value_list), max(value_list)+1):
    number_map[str(i)] = 0

for _, submit_value in author_map.items():
    number_map[str(submit_value)] += 1

print(number_map)


# print(email_map.keys())
