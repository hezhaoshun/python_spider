import requests
from lxml import etree
def getOnePage(n):
#字符串前的格式化
  url=f'http://maoyan.com/board/4?offset={(n-1)*10}'
#告诉服务器 我们是浏览器 字典
  header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#调用
  r=requests.get(url,headers=header)
#返回文本
  return r.text
def parse(text):
#初始化 标准化
  html=etree.HTML(text)
#提取我们想要的信息 需要写xpath语法
#names是列表 xpath返回一定是列表
  names=html.xpath('//div[@class="movie-item-info"]/p[@class="name"]/a/@title')
  print(names)
text=getOnePage(1)
parse(text)
