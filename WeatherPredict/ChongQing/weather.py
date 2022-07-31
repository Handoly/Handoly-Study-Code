import requests

import re
import pandas as pd
import random

class Weather():
    '''创建一个关于爬取天气的类'''
    def __init__(self,url):
        '''初始化属性'''
        self.url = url
        self.name = None
        self.dates = []
        self.Maximum_temperature = []
        self.Minimum_temperature = []

    def get_html(self):
        '''获取网页html'''
        headers = {}
        try:
            #添加了请求头，防止反爬，注意复制粘贴后对headers的内容进行处理，否则会出问题，例如'User - Agent'多了两个空格
            user_agent_list = [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
                'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
            ]
            headers['User-Agent'] = random.choice(user_agent_list)

            response = requests.get(self.url,headers=headers)
        except Exception as e:
            print('获取html网页时遇到了问题，错误原因：',e)
        else:
            # 设置编码格式为gbk
            response.encoding = 'gbk'
            html = response.text
            response.close()
            return html


    def parse_html(self,bs,html):
        '''解析网页html'''

        #查找城市名称
        self.name = '重庆'

        '''查找日期、最高温度、最低温度'''
        try:
            table = bs.find(name='table',attrs={'width':'100%'})

            # 查找日期
            for a in table.find_all(name='a'):
                date = str(a.string).strip()
                self.dates.append(date)

            #利用正则表达式查找最高/最低温度
            pattern = re.compile('<td>.*?href.*?</a>.*?<td>.*?<td>(.*?)</td>',re.S)
            items = re.findall(pattern,html)
            for item in items:
                # 查找最高温度
                if (item.strip()[0:1] and item.strip()[1:2]) in [str(x) for x in range(0,10)]:
                    max = item.strip()[0:2]
                else:
                    max = item.strip()[0:1]
                self.Maximum_temperature.append(max)
                # 查找最低温度
                min = item.strip()[-3:-1]
                self.Minimum_temperature.append(min)
        except Exception as e:
            print('解析html时遇到了问题，错误原因：',e)


    def write_to_file(self,dates,maxs,mins,i):
        '''将数据写入csv文件'''
        #利用pandas，向csv逐列添加数据
        dataframe = pd.DataFrame({'日期':dates,'最高温度':maxs,'最低温度':mins})
        #设置后面添加的数据不添加列名
        if  i == 1:
            dataframe.to_csv(r'cq_weather_data.csv',sep=',',encoding='gbk',mode='a',index=False)
        else:
            dataframe.to_csv(r'cq_weather_data.csv',sep=',',encoding='gbk',mode='a',index=False,header=False)



