import json
import datetime
import math
# from iteration_utils import duplicates
# from iteration_utils import unique_everseen
from collections import Counter

conversation = []

with open("2022_conversation.json", "r") as f1:
    for line in f1.readlines():
        data = json.loads(line)
        conversation.append(data)
f1.close()

mapping = []
count = 0

direct_reject = 0
discussion_reject = 0

accept_conversation = []

with open("2022_commit.json", 'r') as f2:
    for commit_data in f2.readlines():
        fix_commit = json.loads(commit_data)
        # summary = fix_commit["SUMMARY"].lower().split()
        summary = fix_commit["SUMMARY"].lower().split()

        temp = {}
        temp['COMMIT'] = commit_data
        temp['CONVERSATION'] = []

        for i in conversation:

            title = i[0]["subject"][0].lower().split()

            # if summary in title:

            # for email in i:
            #     if fix_commit["ID"] in email['content'][0]:
            #         temp['CONVERSATION'].append(i)
            #         if i not in accept_conversation:
            #             accept_conversation.append(i)
            #             break

            if fix_commit["ID"] in i[0]['content'][0]:
                temp['CONVERSATION'].append(i)
                if i not in accept_conversation:
                    accept_conversation.append(i)


            else:
                rate = len([k for k in summary if k in title]) / len(summary)

                author_date = fix_commit["AUTHORED_DATE"].split()[0]
                author_year = author_date.split('-')[0]
                author_month = author_date.split('-')[1]
                author_day = author_date.split('-')[2]

                email_date = i[0]['date'][0].split()
                email_year = email_date[3]
                email_month = email_date[2]
                email_day = email_date[1]

                if email_month == 'Jan':
                    int_email_month = 1
                elif email_month == 'Feb':
                    int_email_month = 2
                elif email_month == 'Mar':
                    int_email_month = 3
                elif email_month == 'Apr':
                    int_email_month = 4
                elif email_month == 'May':
                    int_email_month = 5
                elif email_month == 'Jun':
                    int_email_month = 6
                elif email_month == 'Jul':
                    int_email_month = 7
                elif email_month == 'Aug':
                    int_email_month = 8
                elif email_month == 'Sep':
                    int_email_month = 9
                elif email_month == 'Oct':
                    int_email_month = 10
                elif email_month == 'Nov':
                    int_email_month = 11
                elif email_month == 'Dec':
                    int_email_month = 12

                date_duration_days = datetime.datetime(int(email_year), int_email_month, int(email_day)) - datetime.datetime(int(author_year), int(author_month), int(author_day))
                date_duration = math.fabs(date_duration_days.days)

                if rate > 0.5:
                    temp['CONVERSATION'].append(i)
                    if i not in accept_conversation:
                        accept_conversation.append(i)
                # elif fix_commit['AUTHOR'] in i[0]['content'][0] and date_duration < 10 and rate >= 0.8:
                #     temp['CONVERSATION'].append(i)
                #     accept_conversation.append(i)

        mapping.append(temp)

# accept_conversation = list(set(accept_conversation))


f2.close()
print('mapping result: {}'.format(len(mapping)))
print('Total conversation: {}'.format(len(conversation)))
print('Accept conversation: {}'.format(len(accept_conversation)))

reject_conversation = []

for conv in conversation:
    if conv not in accept_conversation:
        reject_conversation.append(conv)

print('Reject conversation: {}'.format(len(reject_conversation)))

for reject_conv in reject_conversation:
    if len(reject_conv) < 3:
        direct_reject += 1
    else:
        discussion_reject += 1


direct_accept = 0
discussion_accept = 0

print('direct_reject: {}'.format(direct_reject))
print('discussion_reject: {}'.format(discussion_reject))

for j in mapping:
    if j['CONVERSATION']:

        length = 0

        for x in j['CONVERSATION']:
            length += len(x)

        # print(length)

        if length > 4:
            discussion_accept += 1
        else:
            direct_accept += 1
    else:
        print(j)

print('direct_accept: {}'.format(direct_accept))
print('discussion_accept: {}'.format(discussion_accept))


# NA_commit = 0
#
# for j in mapping:
#     for key,value in j.items():
#         if value == []:
#             NA_commit += 1
#             print(j['COMMIT'])
#         else:
#             with open('commit_email_map.json', 'a') as w:
#                 w.write(json.dumps(j))
#                 w.write('\n')
#
# print(NA_commit)
# w.close()


