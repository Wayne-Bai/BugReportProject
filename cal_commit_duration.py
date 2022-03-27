import datetime
import json

with open('commit_email_mapping.json','r') as f:
    with open('commit_email_mapping_duration.json', 'a') as w:
        for line in f.readlines():
            data = json.loads(line)

            # author_date = data['COMMIT']["AUTHORED_DATE"].split()[0]
            commit = json.loads(data['COMMIT'])


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

            data['DURATION'] = duration.days
            w.write(json.dumps(data))
            w.write('\n')
            print(duration.days)
            # exit()
w.close()
f.close()

