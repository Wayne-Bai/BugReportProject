import json


pair_commit = []
with open('commit_email_mapping.json') as f1:
    for line in f1.readlines():
        data = json.loads(line)
        commit = json.loads(data['COMMIT'])
        pair_commit.append(commit['ID'])
f1.close()

print(len(pair_commit))

flag = 0

with open('commit_git.json','r') as f:
    with open('unmap_commit.json','a') as w:
        for line1 in f.readlines():
            whole_commit = json.loads(line1)
            if whole_commit['ID'] not in pair_commit:
                flag += 1
                print(flag)
                w.write(line1)

f.close()
w.close()
