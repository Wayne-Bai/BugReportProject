import xlwt
import json

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('commit', cell_overwrite_ok=True)

# Set up the HEAD
worksheet.write(0, 0, label='ID')
worksheet.write(0, 1, label='AUTHORED_DATE')
worksheet.write(0, 2, label='AUTHOR')
worksheet.write(0, 3, label='AUTHOR_EMAIL')
worksheet.write(0, 4, label='COMMITTED_DATE')
worksheet.write(0, 5, label='COMMITTER')
worksheet.write(0, 6, label='COMMITTER_EMAIL')
worksheet.write(0, 7, label='SUMMARY')
worksheet.write(0, 8, label='SIZE')
worksheet.write(0, 9, label='MESSAGE')


# Read JSON File
with open('commit_git.json', 'r') as f:

    val = 1

    for line in f.readlines():
        data = json.loads(line)

        for key, value in data.items():
            if key == "ID":
                worksheet.write(val, 0, value)
            elif key == "AUTHORED_DATE":
                worksheet.write(val, 1, value)
            elif key == "AUTHOR":
                worksheet.write(val, 2, value)
            elif key == "AUTHOR_EMAIL":
                worksheet.write(val, 3, value)
            elif key == "COMMITTED_DATE":
                worksheet.write(val, 4, value)
            elif key == "COMMITTER":
                worksheet.write(val, 5, value)
            elif key == "COMMITTER_EMAIL":
                worksheet.write(val, 6, value)
            elif key == "SUMMARY":
                worksheet.write(val, 7, value)
            elif key == "SIZE":
                worksheet.write(val, 8, value)
            elif key == "MESSAGE":
                worksheet.write(val, 9, value)

        val += 1


# SAVE the file

workbook.save('commit_content.xls')
f.close()
