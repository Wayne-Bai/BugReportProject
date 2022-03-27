from git import Repo, diff
import json

repo = Repo('linux')

# print(repo.head.commit)

content = 'whole_commit'

count1 = 0
count2 = 0

count_2017 = 0
count_2018 = 0
count_2019 = 0
count_2020 = 0
count_2021 = 0
count_2022 = 0

if content == 'fix_commit':

    with open('commit_git.json','a') as f:

        # for i, commit in enumerate(repo.iter_commits('master', max_count=2500000)):    # 2500000
        for i, commit in enumerate(repo.iter_commits(max_count=2500000)):

            temp = {}

            date = int(str(commit.authored_datetime)[:4])
            if 'fix' in str(commit.summary).lower().split() and 'merge' not in str(commit.summary).lower() \
                    and 'performance' not in str(commit.summary).lower() and 'perform ' not in str(commit.summary).lower() \
                    and 'performing' not in str(commit.summary).lower() and 'typo' not in str(commit.summary).lower() \
                    and 'revert' not in str(commit.summary).lower() and 'spelling' not in str(commit.summary).lower() \
                    and 'readability' not in str(commit.summary).lower() and 'documentation' not in str(commit.summary).lower() \
                    and 'comment' not in str(commit.summary).lower()  \
                    and 'grammar' not in str(commit.summary).lower() and date-2017 >= 0:
                # and str(commit.author) != str(commit.committer)

            # if 'fix' in str(commit.summary).lower() and 'merge' not in str(commit.summary).lower():
                temp['ID'] = commit.hexsha
                temp['AUTHORED_DATE'] = str(commit.authored_datetime)
                temp['AUTHOR'] = str(commit.author)
                temp['AUTHOR_EMAIL'] = str(commit.author.email)
                temp['COMMITTED_DATE'] = str(commit.committed_datetime)
                # print(str(commit.authored_datetime))
                temp['COMMITTER'] = str(commit.committer)
                temp['COMMITTER_EMAIL'] = str(commit.committer.email)
                temp['SUMMARY'] = str(commit.summary)
                temp['SIZE'] = commit.size
                # print(commit.summary)
                temp['MESSAGE'] = str(commit.message)

                count1 += 1

                f.write(json.dumps(temp))
                f.write('\n')
            count2 += 1
    f.close()

    print('fix commit number: {}'.format(count1))
    print('whole commit number: {}'.format(count2))

elif content == 'whole_commit':

    for i, commit in enumerate(repo.iter_commits('master', max_count=2500000)):
        date = int(str(commit.authored_datetime)[:4])
        if date-2017 >= 0 and '2017' in str(commit.authored_datetime):
            count_2017 += 1
        elif date-2017 >= 0 and '2018' in str(commit.authored_datetime):
            count_2018 += 1
        elif date-2017 >= 0 and '2019' in str(commit.authored_datetime):
            count_2019 += 1
        elif date-2017 >= 0 and '2020' in str(commit.authored_datetime):
            count_2020 += 1
        elif date - 2017 >= 0 and '2021' in str(commit.authored_datetime):
            count_2021 += 1
        elif date-2017 >= 0 and '2022' in str(commit.authored_datetime):
            count_2022 += 1

    print('2017: {}'.format(count_2017))
    print('2018: {}'.format(count_2018))
    print('2019: {}'.format(count_2019))
    print('2020: {}'.format(count_2020))
    print('2021: {}'.format(count_2021))
    print('2022: {}'.format(count_2022))