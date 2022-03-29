import json
import xlwt
import datetime

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('memory report duration', cell_overwrite_ok=True)
worksheet.write(0, 0, label='ID')
worksheet.write(0, 1, label='SUMMARY')
worksheet.write(0, 2, label='Authorized Date' )
worksheet.write(0, 3, label='Committed Date')
worksheet.write(0, 4, label='Public Date')
worksheet.write(0, 5, label='Duration')

number = 1

with open("commit_git.json",'r') as f:
    for line in f.readlines():
        data = json.loads(line)
        commit = json.loads(data['COMMIT'])
        if 'memory' in commit['SUMMARY'].lower():
            print(number)
            worksheet.write(number, 0, commit['ID'])
            worksheet.write(number, 1, commit['SUMMARY'])
            worksheet.write(number, 2, commit['AUTHORED_DATE'])
            worksheet.write(number, 3, commit['COMMITTED_DATE'])

            commit_date = commit["COMMITTED_DATE"].split()[0]
            commit_year = commit_date.split('-')[0]
            commit_month = commit_date.split('-')[1]
            commit_day = commit_date.split('-')[2]

            author_date = commit["AUTHORED_DATE"].split()[0]
            author_year = author_date.split('-')[0]
            author_month = author_date.split('-')[1]
            author_day = author_date.split('-')[2]
            # conversation = data['CONVERSATION']
            #
            # duration = []
            # duration_date = {}
            #
            # for i in conversation:
            #
            #     email_date = i[0]['date'][0].split()
            #     email_year = email_date[3]
            #     email_month = email_date[2]
            #     email_day = email_date[1]
            #
            #     if email_month == 'Jan':
            #         int_email_month = 1
            #     elif email_month == 'Feb':
            #         int_email_month = 2
            #     elif email_month == 'Mar':
            #         int_email_month = 3
            #     elif email_month == 'Apr':
            #         int_email_month = 4
            #     elif email_month == 'May':
            #         int_email_month = 5
            #     elif email_month == 'Jun':
            #         int_email_month = 6
            #     elif email_month == 'Jul':
            #         int_email_month = 7
            #     elif email_month == 'Aug':
            #         int_email_month = 8
            #     elif email_month == 'Sep':
            #         int_email_month = 9
            #     elif email_month == 'Oct':
            #         int_email_month = 10
            #     elif email_month == 'Nov':
            #         int_email_month = 11
            #     elif email_month == 'Dec':
            #         int_email_month = 12

            date_duration_days = datetime.datetime(int(commit_year), int(commit_month), int(commit_day)) - \
                                 datetime.datetime(int(author_year), int(author_month), int(author_day))



            worksheet.write(number, 4, date_duration_days.days)


            number += 1
workbook.save('memory_related_commit.xls')