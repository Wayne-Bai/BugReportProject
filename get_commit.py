from git import Repo, diff
import json

repo = Repo('linux')

# print(repo.head.commit)

count1 = 0
count2 = 0

with open('commit_git.json','a') as f:

    for i, commit in enumerate(repo.iter_commits('master', max_count=2500000)):    # 2500000

        temp = {}

        date = int(str(commit.authored_datetime)[:4])
        if 'fix' in str(commit.summary).lower().split() and 'merge' not in str(commit.summary).lower() \
                and 'performance' not in str(commit.summary).lower() and 'perform ' not in str(commit.summary).lower() \
                and 'performing' not in str(commit.summary).lower() and 'typo' not in str(commit.summary).lower() \
                and 'revert' not in str(commit.summary).lower() and 'spelling' not in str(commit.summary).lower() \
                and 'readability' not in str(commit.summary).lower() and 'documentation' not in str(commit.summary).lower() \
                and 'comment' not in str(commit.summary).lower() and date-2017 >= 0:
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

print(count1)
print(count2)