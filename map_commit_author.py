import json
import xlwt
import datetime
import numpy as np


workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('commit', cell_overwrite_ok=True)

whole_commits = []

with open("commit_git.json",'r') as f:
    for line in f.readlines():
        data = json.loads(line)
        whole_commits.append(data)
f.close()

print(len(whole_commits))

commit_map = {}
sub_number = []

for commit in whole_commits:
    if commit['AUTHOR']:
        author = commit['AUTHOR']
    else:
        author = 'N/A'

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



    if author not in commit_map.keys():
        # if duration.days > 0:
        #     commit_map[author] = {}
        #     commit_map[author]['submission'] = 1
        #     commit_map[author]['duration'] = [duration.days]
        commit_map[author] = {}
        commit_map[author]['submission'] = 1
        commit_map[author]['duration'] = [abs(duration.days)]
        if 'gmail' in author_belong or 'googlemail' in author_belong or 'outlook' in author_belong or 'hotmail' in author_belong \
                or'yahoo' in author_belong or 'foxmail' in author_belong or 'zoho' in author_belong:
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
    else:
        # if duration.days > 0:
        #     commit_map[author]['submission'] += 1
        #     commit_map[author]['duration'].append(duration.days)

        commit_map[author]['submission'] += 1
        commit_map[author]['duration'].append(abs(duration.days))

print(len(commit_map.keys()))

company_dict = {}
company_dict['personal'] = {"number of author": 0, "number of submission": 0, "duration": []}
company_dict['Education'] = {"number of author": 0, "number of submission": 0, "duration": []}
company_dict['company: linux department'] = {"number of author": 0, "number of submission": 0, "duration": []}
company_dict['company'] = {"number of author": 0, "number of submission": 0, "duration": []}
company_dict['non-profit organization'] = {"number of author": 0, "number of submission": 0, "duration": []}
company_dict['network service'] = {"number of author": 0, "number of submission": 0, "duration": []}
company_dict['other'] = {"number of author": 0, "number of submission": 0, "duration": []}

for key,value in commit_map.items():
    if value['belong'] == 'personal':
        company_dict['personal']['number of author'] += 1
        company_dict['personal']['number of submission'] += value['submission']
        company_dict['personal']['duration'] = company_dict['personal']['duration'] + value['duration']
    elif value['belong'] == 'Education':
        company_dict['Education']['number of author'] += 1
        company_dict['Education']['number of submission'] += value['submission']
        company_dict['Education']['duration'] = company_dict['Education']['duration'] + value['duration']
    elif value['belong'] == 'company: linux department':
        company_dict['company: linux department']['number of author'] += 1
        company_dict['company: linux department']['number of submission'] += value['submission']
        company_dict['company: linux department']['duration'] = company_dict['company: linux department']['duration'] + value['duration']
    elif value['belong'] == 'company':
        company_dict['company']['number of author'] += 1
        company_dict['company']['number of submission'] += value['submission']
        company_dict['company']['duration'] = company_dict['company']['duration'] + value['duration']
    elif value['belong'] == 'non-profit organization':
        company_dict['non-profit organization']['number of author'] += 1
        company_dict['non-profit organization']['number of submission'] += value['submission']
        company_dict['non-profit organization']['duration'] = company_dict['non-profit organization']['duration'] + value['duration']
    elif value['belong'] == 'network service company':
        company_dict['network service']['number of author'] += 1
        company_dict['network service']['number of submission'] += value['submission']
        company_dict['network service']['duration'] = company_dict['network service']['duration'] + value['duration']
    elif value['belong'] == 'other':
        company_dict['other']['number of author'] += 1
        company_dict['other']['number of submission'] += value['submission']
        company_dict['other']['duration'] = company_dict['other']['duration'] + value['duration']

    # print("Author: {}, Submit Number: {}, Duration_Average: {}, Duration_Median: {}".format(key, value['submission'], np.mean(value['duration']), np.median(value['duration'])))
    sub_number.append(value['submission'])

print(max(sub_number))
print(sum(sub_number))

number_dict = {}
for i in range(1,max(sub_number)+1):
    number_dict[str(i)] = {}
    number_dict[str(i)]['author number'] = 0
    number_dict[str(i)]['duration'] = []

for key1,value1 in commit_map.items():
    number_dict[str(value1['submission'])]['author number'] += 1
    number_dict[str(value1['submission'])]['duration'] = number_dict[str(value1['submission'])]['duration'] + value1['duration']

# for k,v in number_dict.items():
#     print("#submission: {}, total number: {}, duration:{}".format(k,v['author number'], v['duration']))



workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('author duration', cell_overwrite_ok=True)
worksheet1 = workbook.add_sheet('company duration', cell_overwrite_ok=True)

# Set up the HEAD
worksheet.write(0, 0, label='Number of Submission')
worksheet.write(0, 1, label='Number of Author')
worksheet.write(0, 2, label='Duration Average')
worksheet.write(0, 3, label='Duration Median')

worksheet1.write(0, 0, label='category of belong')
worksheet1.write(0, 1, label="number of author")
worksheet1.write(0, 2, label="number of submission")
worksheet1.write(0, 3, label="Duration Average")
worksheet1.write(0, 4, label='Duration Median')


val = 1


for key, value in number_dict.items():
    worksheet.write(val, 0, key)
    worksheet.write(val, 1, value['author number'])
    if value['duration']:
        worksheet.write(val, 2, np.mean(value['duration']))
        worksheet.write(val, 3, np.median(value['duration']))
    else:
        worksheet.write(val, 2, 0)
        worksheet.write(val, 3, 0)


    val += 1

val1 = 1
for key,value in company_dict.items():
    worksheet1.write(val1, 0, key)
    worksheet1.write(val1, 1, value['number of author'])
    worksheet1.write(val1, 2, value['number of submission'])
    if value['duration']:
        worksheet1.write(val1, 3, np.mean(value['duration']))
        worksheet1.write(val1, 4, np.median(value['duration']))
    else:
        worksheet.write(val1, 2, 0)
        worksheet.write(val1, 3, 0)
    val1 += 1

# SAVE the file

workbook.save('commit_number.xls')
