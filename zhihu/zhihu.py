import requests


# 获得用户数据
def getUserDate():
    url = 'https://www.zhihu.com/api/v4/people/mu-shang-zhu-42/collections'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        # 如果要获取自己私有的收藏夹，需要添加cookie
        # 'cookie':''
    }
    res = requests.get(url=url, headers=headers)
    return res.json()


if __name__ == '__main__':
    userDate=getUserDate()
    for colData in userDate['data']:
        print('------------收藏夹标题：【%s】------------'%colData['title'])
        url = "https://www.zhihu.com/api/v4/collections/%s/items" % colData['id']
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers).json()
        i=1
        for article in res['data']:
            articleTitle = article['content']['title']
            if articleTitle=='':
                articleTitle = article['content']['question']['title']
            articleLink = article['content']['url']
            print('--%s:%s\t%s' % (i,articleTitle, articleLink))
            i+=1
