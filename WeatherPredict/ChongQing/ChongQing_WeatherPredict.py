from weather import Weather
from bs4 import BeautifulSoup
import time
from tqdm import tqdm


def main(url,i):
    #创建城市的天气实例
    w = Weather(url)

    #请求url
    html = w.get_html()

    #构建美味的汤的实例
    bs = BeautifulSoup(html,'lxml')

    #解析url
    w.parse_html(bs,html)

    #将数据添加至列表
    dates = w.dates
    maxs = w.Maximum_temperature
    mins = w.Minimum_temperature

    #写入文件
    w.write_to_file(dates,maxs,mins,i)

def main_and_print_Progress_bar(i,pbar):
    '''运行main函数并打印进度条'''
    url = 'http://www.tianqihoubao.com/lishi/chongqing/month/20220'+str(i)+'.html'
    main(url,i)
    # 延时2秒
    time.sleep(2)
    # 进度条更新
    pbar.update(1)


if __name__ == '__main__':
    year_number = 1
    start_month = 1
    end_month = 7

    #打印进度条
    pbar = tqdm(total=end_month, desc="Count", unit="times")

    for i in range(start_month,end_month+1):
        main_and_print_Progress_bar(i,pbar)

    pbar.close()



