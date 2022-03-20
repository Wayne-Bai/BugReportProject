import requests
import re
import json

Specific_year = 2022
long_month = [1,3,5,7,8,10,12]

class LinuxSpider:

    def __init__(self):

        self.session = requests.Session()
        # self.total = []
        self.year_url = None
        self.date_url = []
        self.day_url = []

    def get_whole_emails(self,url):
        index_html = self.download(url, encoding='gdk')
        # print(index_html)
        self.year_url = self.get_year_url(index_html)
        # print(year_url)

        for i in self.year_url:
            year_url = 'https://lkml.org' +i
            year_html = self.download(year_url, encoding='gdk')
            data_url = self.get_date_url(year_html)
            self.date_url.append(data_url)

        for date in self.date_url:
            for j in date:
                date_url = 'https://lkml.org' + j
                date_html = self.download(date_url, encoding='gdk')
                day_url = self.get_day_url(date_html)
                self.day_url.append(day_url)

        return self.day_url



    def get_email(self,url):

        index_html = self.download(url, encoding='gdk')
        # print(index_html)
        Email_infos = self.get_email_info(index_html)

        if Specific_year == None:
            file_name = 'whole_email.json'
        else:
            file_name = str(Specific_year) + '_email.json'

        with open(file_name, 'a') as w:
            for email_info in Email_infos:
                email_url = 'https://lkml.org' + email_info[0][0]
                email_html = self.download(email_url, encoding='gdk')
                email_dic = self.get_email_content(email_html)
                # print(self.total)
                w.write(json.dumps(email_dic))
                w.write('\n')
        w.close()

    def download(self, url, encoding):

        response = self.session.get(url)
        response.encoding = encoding
        html = response.text
        return html

    def get_year_url(self,index_html):

        result = []

        whole_info = re.findall(r'<a class="nb" href="(.*?)">.*?</a>',index_html)
        for i in whole_info:
            try:
                if int(i[-4:]) - 2017 >= 0:
                    result.append(i)
            except:
                pass

        result = sorted(list(set(result)))

        return result

    def get_date_url(self,index_html):

        result = []

        whole_info = re.findall(r'<a class="nb" href="(.*?)">.*?</a>', index_html)
        for i in whole_info:
            if i.count('/') == 3:
                result.append(i)

        result = sorted(list(set(result)), key=lambda x:int(str(x).split('/')[-1]))
        # print(result)

        return result

    def get_day_url(self,index_html):

        result = []

        whole_info = re.findall(r'<a class="nb" href="(.*?)">.*?</a>', index_html)
        for i in whole_info:
            if i.count('/') == 4:
                result.append(i)

        result = sorted(list(set(result)), key=lambda x:int(str(x).split('/')[-1]))
        # print(result)

        return result

    def get_email_info(self, index_html):

        temp = []
        div = re.findall(r'<tr class=".*?">.*?</tr>', index_html, re.S)

        for i in div:
            # if '[New]' in i:
            #     info = re.findall(r'<a class="nb" href="(.*?)">(.*?)</a></td><td><a class="nb" href=".*?">(.*?)</a></td></tr>',i)
            #     temp.append(info)
            #     # print(info)
            info = re.findall(r'<a class="nb" href="(.*?)">(.*?)</a></td><td><a class="nb" href=".*?">(.*?)</a></td></tr>',i)
            temp.append(info)
                # print(info)
        # print(temp)
        return temp

    def get_email_content(self,email_html):

        email_dic = {}
        author = re.findall(r'<td class="rp" itemprop="author">(.*?) &lt;&gt;</td>',email_html)
        date = re.findall(r'<td class="rp" itemprop="datePublished">(.*?)</td>',email_html)
        subject =re.findall(r'<td class="rp" itemprop="name">(.*?)</td>',email_html)
        content = re.findall(r'<pre itemprop="articleBody">(.*?)</pre>',email_html)
        email_dic['author'] = author
        email_dic['date'] = date
        email_dic['subject'] = subject
        email_dic['content'] = content

        return email_dic

if __name__ == '__main__':
    # Linux_url = 'https://lkml.org/lkml/2020/1/1'
    # spider = LinuxSpider()
    # spider.get_email(Linux_url)

    if Specific_year == None:
        linux_url = 'https://lkml.org/lkml'
        spider = LinuxSpider()
        day_list = spider.get_whole_emails(linux_url)
        # print(len(day_list))
        for i in day_list:
            # print(len(i))
            for j in i:
                print(j)
                email_whole_email = 'https://lkml.org' + j
                spider.get_email(email_whole_email)
    else:
        spider = LinuxSpider()
        if Specific_year == 2022:
            for i in range(1,4):
                if i in long_month:
                    for j in range(1,32):
                        linux_url = 'https://lkml.org/lkml' + str(Specific_year) + '/' + str(i) + '/' + str(j)
                        spider.get_email(linux_url)
                elif i == 2:
                        for j in range(1, 30):
                            linux_url = 'https://lkml.org/lkml' + str(Specific_year) + '/' + str(i) + '/' + str(j)
                            spider.get_email(linux_url)
                else:
                    for j in range(1,31):
                        linux_url = 'https://lkml.org/lkml' + str(Specific_year) + '/' + str(i) + '/' + str(j)
                        spider.get_email(linux_url)
        else:
            for i in range(1,13):
                if i in long_month:
                    for j in range(1,32):
                        linux_url = 'https://lkml.org/lkml' + str(Specific_year) + '/' + str(i) + '/' + str(j)
                        spider.get_email(linux_url)
                elif i == 2:
                    if Specific_year % 4 == 0:
                        for j in range(1, 30):
                            linux_url = 'https://lkml.org/lkml' + str(Specific_year) + '/' + str(i) + '/' + str(j)
                            spider.get_email(linux_url)
                    else:
                        for j in range(1, 29):
                            linux_url = 'https://lkml.org/lkml' + str(Specific_year) + '/' + str(i) + '/' + str(j)
                            spider.get_email(linux_url)
                else:
                    for j in range(1,31):
                        linux_url = 'https://lkml.org/lkml' + str(Specific_year) + '/' + str(i) + '/' + str(j)
                        spider.get_email(linux_url)