import requests
from pyecharts.charts import Bar
import pyecharts.options as opts
import re

class CityData(object):
    def __init__(self,salary):
        self.__salary=salary
        self.__count=0
    def addCount(self):
        self.__count+=1
    def getSalary(self):
        return self.__salary
    def getCount(self):
        return self.__count

list=[]

def getData(page,city):
    url = "https://www.lagou.com/jobs/positionAjax.json?gj=在校/应届&px=default&gm=50-150人&city=%s&needAddtionalResult=false"%city
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '25',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_java/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput=',
        'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':'"Windows"',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'traceparent':'00-06bc3b8a19f3c6e98fe7c56d9adcae1d-4ba823c5c818d9e9-01',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'x-anit-forge-code': '0',
        'x-anit-forge-token': 'None',
        'x-requested-with': 'XMLHttpRequest',
        'cookie':'RECOMMEND_TIP=true; privacyPolicyPopup=false; _ga=GA1.2.1516507538.1647096956; user_trace_token=20220312225557-abb182ce-3f92-4651-9c39-31ebb4c7bdfe; LGUID=20220312225557-bfa9a12c-1d6b-4ade-b9e6-dc95c59fde8b; index_location_city=%E5%85%A8%E5%9B%BD; LG_HAS_LOGIN=1; hasDeliver=0; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; _gid=GA1.2.2010130206.1647242956; __lg_stoken__=18ffbcf2b7cde16a48df0c80069759da64ed5d3427729eae87b1361b2b93ca241428d2ab358fc4b718c2b81d7decdd559a6de084027f5186c937c0190a93eda797ccccb64bc2; JSESSIONID=ABAAABAABAGABFA2095E281A00B43C351EE0D9C94CFC176; WEBTJ-ID=20220315163755-17f8cba0528482-0092a2ae47748d-977173c-2073600-17f8cba0529ca8; LGSID=20220315163755-9896ef8f-e708-40b9-bf90-ecce6c733ae5; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist%5Fjava%2Fp-city%5F0%3F%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1647096956,1647242956,1647333476; gate_login_token=71c896588f9d88913074ddb57f208ae34641bab2fbec2a76d1a12fb63ec712ba; LG_LOGIN_USER_ID=2234f9799e36703943b23a21a509e8f4687aa0619f3e24f8880f5ebf36b5544f; _putrc=D8327F539A6189C2123F89F2B170EADC; login=true; unick=%E7%94%A8%E6%88%B73109; __SAFETY_CLOSE_TIME__24047327=1; sensorsdata2015session=%7B%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2224047327%22%2C%22first_id%22%3A%2217f7ea105d34c1-087ef7f3a3bbec-977173c-2073600-17f7ea105d4d5b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2299.0.4844.51%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217f7ea105d34c1-087ef7f3a3bbec-977173c-2073600-17f7ea105d4d5b%22%7D; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1647333501; SEARCH_ID=05344f68061c476ea546377ac0563232; LGRID=20220315164348-7553573f-0e4d-4a0e-a1cc-d63cbd50d2f7; X_HTTP_TOKEN=dbf713b0116db3ca8283337461a6ef4a1a8eafd163'
        }
    datas = {
        'first':  'true',
        'pn': page,
        'kd': 'java工程师'
    }
    res=requests.post(url=url,headers=headers,data=datas,timeout=4)
    return res.json()['content']['positionResult']['result']

def yanzheng(salary,list):
    flag=True
    for item in list:
        if salary==item.getSalary():
            flag=False
            break
    if flag:
        list.append(CityData(salary))

def addCount(salary,list):
    for item in list:
        if salary==item.getSalary():
            item.addCount()
            break


if __name__ == '__main__':

    try:
        i=1
        while True:
            data=getData(i,'北京')
            for item in data:
                yanzheng(item['salary'],list)
                addCount(item['salary'],list)
                print(item['positionName'],item['workYear'], item['salary'], item['companySize'], item['city'],item['companyFullName'])
            i+=1
    except:
        print('结束')


    for x in range(len(list)):
        for y in range(x+1,len(list)):
            tempx = int(re.search('(\d+).*?(\d+).', list[x].getSalary()).group(1))+int(re.search('(\d+).*?(\d+).', list[x].getSalary()).group(2))
            tempy = int(re.search('(\d+).*?(\d+).', list[y].getSalary()).group(1))+int(re.search('(\d+).*?(\d+).', list[y].getSalary()).group(2))
            if tempx/2>tempy/2:
                temp=list[x]
                list[x]=list[y]
                list[y]=temp

    # for item in list:
    #     print(item.getSalary(),item.getCount())

    salaryList=[]
    countList=[]
    for item in list:
        salaryList.append(item.getSalary())
        countList.append(item.getCount())



    bar = Bar()
    bar.add_xaxis(salaryList)
    bar.add_yaxis('北京',countList)
    bar.set_global_opts(xaxis_opts=opts.AxisOpts(name='薪资'),
                        yaxis_opts = opts.AxisOpts(name='招聘公司数量'))
    bar.render("北京.html")
