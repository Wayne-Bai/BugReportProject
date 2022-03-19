import xlwt
import json

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)

# 设置表头
worksheet.write(0, 0, label='ID')
worksheet.write(0, 1, label='DATE')
worksheet.write(0, 2, label='AUTHOR')
worksheet.write(0, 3, label='SUMMARY')
worksheet.write(0, 4, label='MESSAGE')


# 读取json文件
with open('commit_git.json', 'r') as f:

    val = 1

    for line in f.readlines():
        data = json.loads(line)

        for key, value in data.items():
            if key == "ID":
                worksheet.write(val, 0, value)
            elif key == "DATE":
                worksheet.write(val, 1, value)
            elif key == "AUTHOR":
                worksheet.write(val, 2, value)
            elif key == "SUMMARY":
                worksheet.write(val, 3, value)
            elif key == "MESSAGE":
                worksheet.write(val, 4, value)
        val += 1


# 保存
workbook.save('OK.xls')
