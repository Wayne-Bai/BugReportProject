import json
import xlwt
import datetime
import numpy as np


workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('commit', cell_overwrite_ok=True)

whole_commits = []

with open("2022_commit.json",'r') as f:
    for line in f.readlines():
        data = json.loads(line)
        whole_commits.append(data)
f.close()

print(len(whole_commits))

commit_map = {}
sub_number = []
conv_number = []
whole_duration = []
whole_accept_line = []
whole_conversation_line = []
whole_reject_line = []

for commit in whole_commits:
    if commit['AUTHOR']:
        if commit['AUTHOR'] != 'Greg Kroah-Hartman' and commit['AUTHOR'] != 'kernel test robot':
            author = commit['AUTHOR']

            author_date = commit["AUTHORED_DATE"].split()[0]
            author_year = author_date.split('-')[0]
            author_month = author_date.split('-')[1]
            author_day = author_date.split('-')[2]

            # commit_date = data['COMMIT']["COMMITTED_DATE"].split()[0]
            commit_date = commit["COMMITTED_DATE"].split()[0]
            commit_year = commit_date.split('-')[0]
            commit_month = commit_date.split('-')[1]
            commit_day = commit_date.split('-')[2]

            duration = datetime.datetime(int(commit_year), int(commit_month), int(commit_day)) - \
                       datetime.datetime(int(author_year), int(author_month), int(author_day))

            author_email = commit["AUTHOR_EMAIL"]
            email_address = author_email.split('@')[1]
            author_belong = email_address.split('.')

            accept_content = commit['MESSAGE']
            if 'Fixes:' in accept_content:
                description = accept_content.split('Fixes:')[0]
                accept_line = len(description.split('\n\n'))
            else:
                accept_line = len(accept_content.split('\n\n'))




            if author not in commit_map.keys():
                commit_map[author] = {}

                commit_map[author]['submission'] = 1

                commit_map[author]['duration'] = [abs(duration.days)]

                commit_map[author]['accept line'] = [accept_line]

                if 'gmail' in author_belong or 'googlemail' in author_belong or 'outlook' in author_belong or 'hotmail' in author_belong \
                        or 'yahoo' in author_belong or 'foxmail' in author_belong or 'zoho' in author_belong:
                    commit_map[author]['belong'] = 'personal'
                elif 'edu' in author_belong:
                    commit_map[author]['belong'] = 'Education'
                elif 'net' in author_belong:
                    commit_map[author]['belong'] = 'network service company'
                elif 'org' in author_belong:
                    commit_map[author]['belong'] = 'non-profit organization'
                elif 'com' in author_belong:
                    if 'linux' in email_address:
                        commit_map[author]['belong'] = 'company: linux department'
                    else:
                        commit_map[author]['belong'] = 'company'
                else:
                    commit_map[author]['belong'] = 'other'

                commit_map[author]['conversation'] = 0

                commit_map[author]['conversation line'] = []

            else:
                commit_map[author]['accept line'].append(accept_line)

                commit_map[author]['submission'] += 1

with open('2022_conversation.json', 'r') as f1:
    for line in f1.readlines():
        conversation = json.loads(line)
        if conversation[0]['author']:
            conversation_author = conversation[0]['author'][0]
            if conversation_author in commit_map.keys():
                commit_map[conversation_author]['conversation'] += 1
                conversation_content = conversation[0]['content'][0]
                if 'Fixes:' in conversation_content:
                    conv_description_1 = conversation_content.split('Fixes')[0]
                    if 'Signed-off-by' in conv_description_1:
                        conv_description_2 = conv_description_1.split('Signed-off-by')[0]
                        content_line_temp = [x.strip() for x in conv_description_2.split('<br />') if x.strip()!='']
                        content_line = []
                        for i in content_line_temp:
                            if 'Link:' not in i and 'http' not in i:
                                content_line.append(i)
                        commit_map[conversation_author]['conversation line'].append(len(content_line_temp))
                    else:
                        content_line_temp = [x.strip() for x in conv_description_1.split('<br />') if x.strip() != '']
                        content_line = []
                        for i in content_line_temp:
                            if 'Link:' not in i and 'http' not in i:
                                content_line.append(i)
                        commit_map[conversation_author]['conversation line'].append(len(content_line))

                else:
                    if 'Signed-off-by' in conversation_content:
                        conv_description = conversation_content.split('Signed-off-by')[0]
                        content_line_temp = [x.strip() for x in conv_description.split('<br />') if x.strip() != '']
                        content_line = []
                        for i in content_line_temp:
                            if 'Link:' not in i and 'http' not in i:
                                content_line.append(i)
                        commit_map[conversation_author]['conversation line'].append(len(content_line))
                    else:
                        content_line_temp = [x.strip() for x in conv_description.split('<br />') if x.strip() != '']
                        content_line = []
                        for i in content_line_temp:
                            if 'Link:' not in i and 'http' not in i:
                                content_line.append(i)
                        commit_map[conversation_author]['conversation line'].append(len(content_line))
print(len(commit_map.keys()))

filter_commit_map = {}
for key,value in commit_map.items():
    if value['conversation'] != 0:
        filter_commit_map[key] = value

company_dict = {}
company_dict['personal'] = {"number of author": 0, "number of submission": 0, "duration": [], 'conversation': 0, 'accept line': [], 'conversation line': []}
company_dict['Education'] = {"number of author": 0, "number of submission": 0, "duration": [], 'conversation': 0, 'accept line': [], 'conversation line': []}
company_dict['company: linux department'] = {"number of author": 0, "number of submission": 0, "duration": [], 'conversation': 0, 'accept line': [], 'conversation line': []}
company_dict['company'] = {"number of author": 0, "number of submission": 0, "duration": [], 'conversation': 0, 'accept line': [], 'conversation line': []}
company_dict['non-profit organization'] = {"number of author": 0, "number of submission": 0, "duration": [], 'conversation': 0, 'accept line': [], 'conversation line': []}
company_dict['network service'] = {"number of author": 0, "number of submission": 0, "duration": [], 'conversation': 0, 'accept line': [], 'conversation line': []}
company_dict['other'] = {"number of author": 0, "number of submission": 0, "duration": [], 'conversation': 0, 'accept line': [], 'conversation line': []}

for key,value in filter_commit_map.items():
    if value['belong'] == 'personal':
        company_dict['personal']['number of author'] += 1
        company_dict['personal']['number of submission'] += value['submission']
        company_dict['personal']['duration'] = company_dict['personal']['duration'] + value['duration']
        company_dict['personal']['conversation'] += value['conversation']
        # company_dict['personal']['accept line'] = company_dict['personal']['accept line'] + value['accept line']
        # company_dict['personal']['conversation line'] = company_dict['personal']['conversation line'] + value['conversation line']
    elif value['belong'] == 'Education':
        company_dict['Education']['number of author'] += 1
        company_dict['Education']['number of submission'] += value['submission']
        company_dict['Education']['duration'] = company_dict['Education']['duration'] + value['duration']
        company_dict['Education']['conversation'] += value['conversation']
        # company_dict['Education']['accept line'] = company_dict['Education']['accept line'] + value['accept line']
        # company_dict['Education']['conversation line'] = company_dict['Education']['conversation line'] + value['conversation line']
    elif value['belong'] == 'company: linux department':
        company_dict['company: linux department']['number of author'] += 1
        company_dict['company: linux department']['number of submission'] += value['submission']
        company_dict['company: linux department']['duration'] = company_dict['company: linux department']['duration'] + value['duration']
        company_dict['company: linux department']['conversation'] += value['conversation']
        # company_dict['company: linux department']['accept line'] = company_dict['company: linux department']['accept line'] + value['accept line']
        # company_dict['company: linux department']['conversation line'] = company_dict['company: linux department']['conversation line'] + value['conversation line']
    elif value['belong'] == 'company':
        company_dict['company']['number of author'] += 1
        company_dict['company']['number of submission'] += value['submission']
        company_dict['company']['duration'] = company_dict['company']['duration'] + value['duration']
        company_dict['company']['conversation'] += value['conversation']
        # company_dict['company']['accept line'] = company_dict['company']['accept line'] + value['accept line']
        # company_dict['company']['conversation line'] = company_dict['company']['conversation line'] + value['conversation line']
    elif value['belong'] == 'non-profit organization':
        company_dict['non-profit organization']['number of author'] += 1
        company_dict['non-profit organization']['number of submission'] += value['submission']
        company_dict['non-profit organization']['duration'] = company_dict['non-profit organization']['duration'] + value['duration']
        company_dict['non-profit organization']['conversation'] += value['conversation']
        # company_dict['non-profit organization']['accept line'] = company_dict['non-profit organization']['accept line'] + value['accept line']
        # company_dict['non-profit organization']['conversation line'] = company_dict['non-profit organization']['conversation line'] + value['conversation line']
    elif value['belong'] == 'network service company':
        company_dict['network service']['number of author'] += 1
        company_dict['network service']['number of submission'] += value['submission']
        company_dict['network service']['duration'] = company_dict['network service']['duration'] + value['duration']
        company_dict['network service']['conversation'] += value['conversation']
        # company_dict['network service company']['accept line'] = company_dict['network service company']['accept line'] + value['accept line']
        # company_dict['network service company']['conversation line'] = company_dict['network service company']['conversation line'] + value['conversation line']
    elif value['belong'] == 'other':
        company_dict['other']['number of author'] += 1
        company_dict['other']['number of submission'] += value['submission']
        company_dict['other']['duration'] = company_dict['other']['duration'] + value['duration']
        company_dict['other']['conversation'] += value['conversation']
        # company_dict['other']['accept line'] = company_dict['other']['accept line'] + value['accept line']
        # company_dict['other']['conversation line'] = company_dict['other']['conversation line'] + value['conversation line']

    # print("Author: {}, Submit Number: {}, Duration_Average: {}, Duration_Median: {}".format(key, value['submission'], np.mean(value['duration']), np.median(value['duration'])))
    sub_number.append(value['submission'])
    conv_number.append(value['conversation'])
    whole_duration += value['duration']

    accept_temp = value['accept line'].copy()
    reject_temp = value['conversation line'].copy()

    if len(accept_temp) < len(reject_temp):
        for i in accept_temp:
            if i in reject_temp:
                reject_temp.remove(i)
            else:
                reject_temp.remove(max(reject_temp))

    whole_accept_line += accept_temp
    whole_reject_line += reject_temp

print(max(sub_number))
print(sum(sub_number))

whole_line = whole_accept_line + whole_reject_line

print(max(whole_line))
print(min(whole_line))

print('whole accept rate: {}'.format(sum(sub_number)/sum(conv_number)))
print('whole average duration: {}'.format(np.mean(whole_duration)))
print('whole median duration:{}'.format(np.median(whole_duration)))
print('whole average accept line: {}'.format(np.mean(whole_accept_line)))
print('whole average reject line: {}'.format(np.mean(whole_reject_line)))

number_dict = {}
for i in range(1,max(sub_number)+1):
    number_dict[str(i)] = {}
    number_dict[str(i)]['author number'] = 0
    number_dict[str(i)]['duration'] = []
    number_dict[str(i)]['conversation'] = 0
    # number_dict[str(i)]['accept line'] = []
    # number_dict[str(i)]['conversation line'] = []

for key1,value1 in filter_commit_map.items():
    number_dict[str(value1['submission'])]['author number'] += 1
    number_dict[str(value1['submission'])]['duration'] = number_dict[str(value1['submission'])]['duration'] + value1['duration']
    number_dict[str(value1['submission'])]['conversation'] += value1['conversation']
    # number_dict[str(value1['submission'])]['accept line'] = number_dict[str(value1['submission'])]['accept line'] + value1['accept line']
    # number_dict[str(value1['submission'])]['conversation line'] = number_dict[str(value1['submission'])]['conversation line'] + value1['conversation line']
# for k,v in number_dict.items():
#     print("#submission: {}, total number: {}, duration:{}".format(k,v['author number'], v['duration']))

line_dict = {}
for i in range(min(whole_line), max(whole_line)+1):
    line_dict[str(i)] = {}
    line_dict[str(i)]['accept'] = 0
    line_dict[str(i)]['reject'] = 0

for i in whole_accept_line:
    line_dict[str(i)]['accept'] += 1
for j in whole_reject_line:
    line_dict[str(j)]['reject'] += 1



workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('author duration', cell_overwrite_ok=True)
worksheet1 = workbook.add_sheet('company duration', cell_overwrite_ok=True)
worksheet2 = workbook.add_sheet('line accept reject', cell_overwrite_ok=True)

# Set up the HEAD
worksheet.write(0, 0, label='Number of Submission')
worksheet.write(0, 1, label='Number of Conversation')
worksheet.write(0, 2, label='Number of Author')
worksheet.write(0, 3, label='Duration Average')
worksheet.write(0, 4, label='Duration Median')
worksheet.write(0, 5, label='Accept Rate')


worksheet1.write(0, 0, label='category of belong')
worksheet1.write(0, 1, label="number of author")
worksheet1.write(0, 2, label="number of submission")
worksheet1.write(0, 3, label="number of conversation")
worksheet1.write(0, 4, label="Duration Average")
worksheet1.write(0, 5, label='Duration Median')
worksheet1.write(0, 6, label='Accept Rate')

worksheet2.write(0, 0, label='Number of lines')
worksheet2.write(0, 1, label='Accept')
worksheet2.write(0, 2, label='Reject')

val = 1


for key, value in number_dict.items():
    worksheet.write(val, 0, key)
    worksheet.write(val, 1, value['conversation'])
    worksheet.write(val, 2, value['author number'])

    if value['duration']:
        worksheet.write(val, 3, np.mean(value['duration']))
        worksheet.write(val, 4, np.median(value['duration']))
    else:
        worksheet.write(val, 3, 0)
        worksheet.write(val, 4, 0)

    if value['author number'] == 0:
        worksheet.write(val, 5, 0)
    else:
        worksheet.write(val, 5, int(key) * value['author number'] / value['conversation'])
    val += 1

val1 = 1
for key,value in company_dict.items():
    worksheet1.write(val1, 0, key)
    worksheet1.write(val1, 1, value['number of author'])
    worksheet1.write(val1, 2, value['number of submission'])
    worksheet1.write(val1, 3, value['conversation'])
    if value['duration']:
        worksheet1.write(val1, 4, np.mean(value['duration']))
        worksheet1.write(val1, 5, np.median(value['duration']))
    else:
        worksheet.write(val1, 4, 0)
        worksheet.write(val1, 5, 0)
    worksheet1.write(val1, 6, value['number of submission']/value['conversation'])
    val1 += 1

val2 = 1
for key,value in line_dict.items():
    worksheet2.write(val2, 0, key)
    worksheet2.write(val2, 1, value['accept'])
    worksheet2.write(val2, 2, value['reject'])
    val2 += 1

# SAVE the file

workbook.save('final version.xls')
