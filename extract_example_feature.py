import json
import xlwt

conversation = []

with open("2022_conversation.json", "r") as f1:
    for line in f1.readlines():
        data = json.loads(line)
        conversation.append(data)
f1.close()

direct_accept = []

discussion_accept = []


with open("2022_commit_email_mapping.json", 'r') as f2:
    for lines in f2.readlines():
        accept_data = json.loads(lines)
        if accept_data['CONVERSATION']:

            # length = 0
            length = max(len(k) for k in accept_data["CONVERSATION"])
            print(length)

            if length > 2:
                discussion_accept.append(accept_data['CONVERSATION'])

            else:
                direct_accept.append(accept_data['CONVERSATION'])

f2.close()

direct_reject = []

discussion_reject = []

for conv in conversation:
    if conv not in direct_accept and conv not in discussion_accept:
        if len(conv) < 3:
            direct_reject.append(conv)
        else:
            discussion_reject.append(conv)


print('directed accept: {}'.format(len(direct_accept)))
print('discussion accept: {}'.format(len(discussion_accept)))
print('discussion refuse: {}'.format(len(discussion_reject)))
print('directed refuse: {}'.format(len(direct_reject)))



workbook = xlwt.Workbook(encoding='utf-8')
worksheet1 = workbook.add_sheet('direct accept', cell_overwrite_ok=True)
worksheet2 = workbook.add_sheet('discussion accept', cell_overwrite_ok=True)
worksheet3 = workbook.add_sheet('discussion reject', cell_overwrite_ok=True)
worksheet4 = workbook.add_sheet('direct reject', cell_overwrite_ok=True)

# Set up the HEAD
worksheet1.write(0, 0, label='DATE')
worksheet1.write(0, 1, label='EMAIL CONTENT')

worksheet2.write(0, 0, label='DATE')
worksheet2.write(0, 1, label='EMAIL CONTENT')

worksheet3.write(0, 0, label='DATE')
worksheet3.write(0, 1, label='EMAIL CONTENT')

worksheet4.write(0, 0, label='DATE')
worksheet4.write(0, 1, label='EMAIL CONTENT')

v1 = 1
v2 = 1
v3 = 1
v4 = 1
v5 = 1


for a in direct_accept:
    if v1 < 65:
        if len(a) == 1:
            if a[0][0]['author'] != ['Greg Kroah-Hartman']:
                worksheet1.write(v1, 0, a[0][0]['date'])
                worksheet1.write(v1, 1, str(a[0][0])[:4000])
                v1 += 1
        else:
            max_len1 = max(len(x) for x in a)
            for a1 in a:
                if len(a1) == max_len1 and a1[0]['author'] != ['Greg Kroah-Hartman']:
                    worksheet1.write(v1, 0, a1[0]['date'])
                    worksheet1.write(v1, 1, str(a1)[:4000])
                    v1 += 1

for b in discussion_accept:
    if v2 < 65:
        max_len2 = max(len(x) for x in b)
        for b1 in b:
            if len(b1) == max_len2 and b1[0]['author'] != ['Greg Kroah-Hartman']:
                worksheet2.write(v2, 0, b1[0]['date'])
                worksheet2.write(v2, 1, str(b1)[:4000])
                v2 += 1

for c in discussion_reject:
    if v3 < 65:
        max_len3 = max(len(x) for x in c)
        for c1 in c:
            if len(c1) == max_len3 and c1['author'] != ['Greg Kroah-Hartman']:
                worksheet3.write(v3, 0, c1['date'])
                worksheet3.write(v3, 1, str(c1)[:4000])
                v3 += 1

for d in direct_reject:
    if v4 < 65:
        if len(d) == 1 and d[0]['author'] != ['Greg Kroah-Hartman'] and d[0]['author'] != ['kernel test robot']:
            worksheet4.write(v4, 0, d[0]['date'])
            worksheet4.write(v4, 1, str(d)[:4000])
            v4 += 1
        else:
            max_len4 = max(len(x) for x in d)
            for d1 in d:
                if len(d1) == max_len4 and d1['author'] != ['Greg Kroah-Hartman'] and d1['author'] != ['kernel test robot']:
                    worksheet4.write(v4, 0, d1['date'])
                    worksheet4.write(v4, 1, str(d1)[:4000])
                    v4 += 1



# SAVE the file

workbook.save('4_categories_example.xls')


