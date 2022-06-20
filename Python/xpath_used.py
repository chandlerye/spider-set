import requests
from lxml import etree


if __name__ == "__main__":


    headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }

    url = "https://bj.58.com/ershoufang/"

    page_text = requests.get(url=url,headers=headers).text

    #将page_text转成etree对象
    tree = etree.HTML(page_text) 

    #xpath的格式,属性用@class来获取
    li_list = tree.xpath('//section[@class="list"]/div')  

    for li in li_list:
	#以当前li为开端获取下层标签
        title = li.xpath('./a/div[2]/div/div/h3/@title') 
        with open('./info.txt','a',encoding='utf-8') as fp:
            fp.write("\n")
            fp.write(title[0])
