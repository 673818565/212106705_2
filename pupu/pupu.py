"""
监控朴朴上某产品的详细价格信息
"""
import requests
import time


# 获得商品详情json
def getProduct():
    url = "https://j1.pupuapi.com/client/product/storeproduct/detail/7c1208da-907a-4391-9901-35a60096a3f9/97721095-5c55-4746-bd9e-8c98ef2946a3"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    result = requests.get(url=url, headers=headers)
    data = result.json()['data']
    return data


# 获得商品名
def getName(result):
    return result['name']


# 获得产品规格
def getSpec(result):
    return result['spec']


# 获得现价
def getPrice(result):
    return float(result['price']) / 100


# 获得原价
def getMarketPrice(result):
    return float(result['market_price']) / 100


# 获得详细内容
def getShareContent(result):
    return result['share_content']


# 获得实时价格
def nowPrice():
    return float(getProduct()['price']) / 100


if __name__ == '__main__':
    # 调用接口，获得商品数据
    proData = getProduct()
    # 获得商品名称
    proName = getName(proData)
    # 获得产品规格
    proSpec = getSpec(proData)
    # 获得产品现价
    proPrice = getPrice(proData)
    # 获取产品原价
    proMarketPrice = getMarketPrice(proData)
    # 获取产品详细内容
    proContent = getShareContent(proData)
    print('-------------商品:%s-------------' % proName)
    print('规格：%s' % proSpec)
    print('价格：%.1f' % proPrice)
    print('折扣价/原价：%.1f/%.1f' % (proPrice, proMarketPrice))
    print('详细内容：%s\n' % proContent)
    print('-------------"%s"的价格波动-------------' % proName)
    # 循环获取目前价格
    for i in range(5):
        # 获得当前时间
        dateTime = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        print('当前时间为%s，价格为%.1f' % (dateTime, nowPrice()))
        time.sleep(1)