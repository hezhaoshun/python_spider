import requests
from bs4 import BeautifulSoup as bs

#以豆瓣‘编程’分类的一个连接URL为例子开始爬数据ID
url = 'https://book.douban.com/tag/编程?start=20&type=T'
res = requests.get(url)  #发送请求
#print(res.encoding)    #这个是用来查看网页编码的
#res.encoding = 'utf-8'   #跟上一个结合来用，如果编码有乱码，则可以通过这个定义编码来改变
html = res.text     
#print(html)

IDs = []
soup  = bs(html,"html.parser")     #定义一个BeautifulSoup变量
items = soup.find_all('a',attrs={'class':'nbg'})
#print(items)

for i in items:
    idl = i.get('href')
    #print(idl)
    id = idl.split('/')[4]
    print(id)
    IDs.append(id)
print('这一页收集到书籍ID数：%d' % len(IDs))
