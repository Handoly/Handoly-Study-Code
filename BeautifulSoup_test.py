import requests
from bs4 import BeautifulSoup

'''
def request_url():
    #请求url
    url = 'https://www.baidu.com/'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print('请求网页成功')
    except Exception as e:
        print('错误原因：',e)
    else:

        #指定编码格式为utf-8，防止出现中文乱码
        response.encoding='utf-8'

        result = response.text

        #创建BeautifulSoup对象
        bs = BeautifulSoup(result,'lxml')

        #美化html格式
        html = bs.prettify()

        #将html写入文件baidu.html
        with open('baidu.html','w',encoding='utf-8') as f:
            f.write(html)
            print('文件读写完毕')

request_url()
'''
with open('baidu.html','r',encoding='utf-8') as f:
    html = f.read()

bs = BeautifulSoup(html,'lxml')
print(bs.a)
print('========================================================================================')
print(bs.a.name)
print('========================================================================================')
print(bs.a.attrs)
print('========================================================================================')
print(bs.a.string)
print('========================================================================================')
print(len(bs.body.contents))
for child in bs.body.children:
    print(child)

print('========================================================================================')

for child in bs.body.descendants:
    print(child)
    print('---------------------------------------------------------------------------------')

print('========================================================================================')
print(bs.a.parent.name)
print('========================================================================================')
for parent in bs.a.parents:
    print(parent)
    print('---------------------------------------------------------------------------------')
print('========================================================================================')
for sibling in bs.a.next_siblings:
    print(sibling)
    print('---------------------------------------------------------------------------------')

print('========================================================================================')
for sibling in bs.a.previous_siblings:
    print(sibling)
    print('---------------------------------------------------------------------------------')
print('========================================================================================')
for string in bs.body.strings:
    print(string)
    print('---------------------------------------------------------------------------------')
print('========================================================================================')
for string in bs.body.stripped_strings:
    print(string)
    print('---------------------------------------------------------------------------------')
print('========================================================================================')
print(bs.a.has_attr)
print('========================================================================================')







