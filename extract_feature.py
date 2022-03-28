import json
import xlwt
import numpy as np

conversation = []
maintainer_email = 0

with open("total_conversation.json", "r") as f1:
    for line in f1.readlines():
        data = json.loads(line)
        # if data[0]['author'] != ['Greg Kroah-Hartman'] and data[0]['author'] != ['kernel test robot']:
        #     conversation.append(data)
        # else:
        #     maintainer_email += 1
        conversation.append(data)
f1.close()

direct_accept = []

direct_accept_feature = []

discussion_accept = []

discussion_accept_feature = []

total_accept = []

with open("commit_email_mapping.json", 'r') as f2:
    for lines in f2.readlines():
        accept_data = json.loads(lines)
        if accept_data['CONVERSATION']:

            # length = 0
            length = max(len(k) for k in accept_data["CONVERSATION"])
            print(length)

            if length > 2:
                for i in accept_data['CONVERSATION']:
                    # if i not in total_accept and i[0]['author'] != ['Greg Kroah-Hartman'] and i[0]['author'] != ['kernel test robot']:
                    if i not in total_accept and len(i) == length:
                        total_accept.append(i)
                        discussion_accept.append(i)
                    # if len(i) > 1 and i not in discussion_accept:
                    #     discussion_accept.append(i)
                    # if i not in discussion_accept and i[0]['author'] != ['Greg Kroah-Hartman'] and i[0]['author'] != ['kernel test robot']:


            else:
                for j in accept_data['CONVERSATION']:
                    # if j not in total_accept and j[0]['author'] != ['Greg Kroah-Hartman'] and j[0]['author'] != ['kernel test robot']:
                    if j not in total_accept:
                        total_accept.append(j)
                    # if j not in direct_accept and j[0]['author'] != ['Greg Kroah-Hartman'] and j[0]['author'] != ['kernel test robot']:
                    if j not in direct_accept:
                        direct_accept.append(j)

f2.close()

direct_reject = []

direct_reject_feature = []

discussion_reject = []

discussion_reject_feature = []

for conv in conversation:
    if conv not in total_accept:
        if len(conv) == 1:
            direct_reject.append(conv)
        else:
            discussion_reject.append(conv)


# print('maintainer email: {}'.format(maintainer_email))
# print('total conversation: {}'.format((len(conversation))))
# print('directed accept: {}'.format(len(direct_accept)))
# print('discussion accept: {}'.format(len(discussion_accept)))
# print('discussion refuse: {}'.format(len(discussion_reject)))
# print('directed refuse: {}'.format(len(direct_reject)))

for i in direct_accept:

    if i[0]['author'] != ['Greg Kroah-Hartman'] and i[0]['author'] != ['kernel test robot']:
        temp = {}
        temp['#CONV'] = len(i)
        temp['SIZE'] = []
        for j in i:
            temp['SIZE'].append(len(j['content'][0]))
        direct_accept_feature.append(temp)
    else:
        maintainer_email += 1

for i in discussion_accept:

    if i[0]['author'] != ['Greg Kroah-Hartman'] and i[0]['author'] != ['kernel test robot']:
        temp = {}
        temp['#CONV'] = len(i)
        temp['SIZE'] = []
        for j in i:
            temp['SIZE'].append(len(j['content'][0]))
        discussion_accept_feature.append(temp)
    else:
        maintainer_email += 1

for i in discussion_reject:

    if i[0]['author'] != ['Greg Kroah-Hartman'] and i[0]['author'] != ['kernel test robot']:
        temp = {}
        temp['#CONV'] = len(i)
        temp['SIZE'] = []
        for j in i:
            temp['SIZE'].append(len(j['content'][0]))
        discussion_reject_feature.append(temp)
    else:
        maintainer_email += 1

for i in direct_reject:

    if i[0]['author'] != ['Greg Kroah-Hartman'] and i[0]['author'] != ['kernel test robot']:
        temp = {}
        temp['#CONV'] = len(i)
        temp['SIZE'] = []
        for j in i:
            temp['SIZE'].append(len(j['content'][0]))
        direct_reject_feature.append(temp)
    else:
        maintainer_email += 1

print('maintainer email: {}'.format(maintainer_email))
# print('total conversation: {}'.format((len(conversation))))
print('directed accept: {}'.format(len(direct_accept_feature)))
print('discussion accept: {}'.format(len(discussion_accept_feature)))
print('discussion refuse: {}'.format(len(discussion_reject_feature)))
print('directed refuse: {}'.format(len(direct_reject_feature)))



# print(len(direct_accept_feature))
# print(len(discussion_accept_feature))
# print(len(discussion_reject_feature))
# print(len(direct_reject_feature))
# print(maintainer_email)



workbook = xlwt.Workbook(encoding='utf-8')
worksheet1 = workbook.add_sheet('direct accept', cell_overwrite_ok=True)
worksheet2 = workbook.add_sheet('discussion accept', cell_overwrite_ok=True)
worksheet3 = workbook.add_sheet('discussion reject', cell_overwrite_ok=True)
worksheet4 = workbook.add_sheet('direct reject', cell_overwrite_ok=True)

# Set up the HEAD
worksheet1.write(0, 0, label='#conv')
worksheet1.write(0, 1, label='Average')
worksheet1.write(0, 2, label='Total')

worksheet2.write(0, 0, label='#conv')
worksheet2.write(0, 1, label='Average')
worksheet2.write(0, 2, label='Total')

worksheet3.write(0, 0, label='#conv')
worksheet3.write(0, 1, label='Average')
worksheet3.write(0, 2, label='Total')

worksheet4.write(0, 0, label='#conv')
worksheet4.write(0, 1, label='Average')
worksheet4.write(0, 2, label='Total')

v1 = 1
v2 = 1
v3 = 1
v4 = 1

for i in direct_accept_feature:
    worksheet1.write(v1, 0, i['#CONV'])
    worksheet1.write(v1, 1, np.mean(i['SIZE']))
    worksheet1.write(v1, 2, sum(i['SIZE']))
    v1 += 1

for i in discussion_accept_feature:
    worksheet2.write(v2, 0, i['#CONV'])
    worksheet2.write(v2, 1, np.mean(i['SIZE']))
    worksheet2.write(v2, 2, sum(i['SIZE']))
    v2 += 1

for i in discussion_reject_feature:
    worksheet3.write(v3, 0, i['#CONV'])
    worksheet3.write(v3, 1, np.mean(i['SIZE']))
    worksheet3.write(v3, 2, sum(i['SIZE']))
    v3 += 1

for i in direct_reject_feature:
    worksheet4.write(v4, 0, i['#CONV'])
    worksheet4.write(v4, 1, np.mean(i['SIZE']))
    worksheet4.write(v4, 2, sum(i['SIZE']))
    v4 += 1



# SAVE the file

workbook.save('email_size_feature.xls')


