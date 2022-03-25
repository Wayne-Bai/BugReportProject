import json

# Delete 'no-fix' data

count = 0
fix_email = []

with open('../2022_email.json','r') as f:
    for line in f.readlines():
        data = json.loads(line)
        if 'fix' in str(data['subject']).lower().split() and 'merge' not in str(data['subject']).lower() \
                and 'performance' not in str(data['subject']).lower() and 'perform' not in str(data['subject']).lower() \
                and 'performing' not in str(data['subject']).lower() and 'typo' not in str(data['subject']).lower() \
                and 'revert' not in str(data['subject']).lower() and 'spelling' not in str(data['subject']).lower() \
                and 'readability' not in str(data['subject']).lower() and 'documentation' not in str(data['subject']).lower() \
                and 'comment' not in str(data['subject']).lower():
            fix_email.append(data)
            count += 1
f.close()

print(count)

with open('2022_fix_total.json','a') as w:
    for i in fix_email:
        w.write(json.dumps(i))
        w.write('\n')
w.close()

#Generate Conversation
# total_conversation = []
# for i in range(len(fix_email)):
#     if 'Re:' not in fix_email[i]['subject']:
#         temp = []
#         temp.append(fix_email[i])
#         for j in range(i+1, len(fix_email)):
#             if fix_email[i]['subject'] in fix_email[j]['subject']:
#                 temp.append(fix_email[j])
#         total_conversation.append(temp)
# print(len(total_conversation))

