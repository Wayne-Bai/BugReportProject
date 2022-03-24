import json
import xlwt


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
for commit in whole_commits:
    if commit['AUTHOR']:
        author = commit['AUTHOR']
    else:
        author = 'N/A'
    if author not in commit_map.keys():
        commit_map[author] = []
        commit_map[author].append(commit)
    else:
        commit_map[author].append(commit)

print(len(commit_map.keys()))

for key,value in commit_map.items():
    print("Author: {}, Submit Number: {}".format(key, len(value)))

