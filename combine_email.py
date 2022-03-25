import json


with open('whole_email.json', 'a') as w:
    for i in range(2017,2023):

        count = 0
        file_name = 'dataset/' + str(i) + '_email.json'
        with open(file_name,'r') as f:
            for line in f.readlines():
                w.write(line)
                count += 1

        f.close()
        print('{}: {}'.format(i,count))

flag = 0
with open('whole_email.json', 'r') as f2:
    for line in f2.readlines():
        flag += 1
    print('total email: {}'.format(flag))

f2.close()