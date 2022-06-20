import requests	    #请求模块
import re           #正则模块
import os	    #文件模块


if __name__ == "__main__":
    if not os.path.exists('./img'):
        os.mkdir('./img')

    headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }

    url = 'https://movie.douban.com/top250?start=%d&filter='    


    for pageNum in range(1,10):    #page是按什么方式递增要自己注意

        pageStart = (pageNum-1)*25

        new_url = format(url%pageStart)

        respone = requests.get(url=new_url,headers=headers).text

        ex = '<div class="pic">.*?<img width="100" alt=".*?" src="(.*?)" class.*?</div>'     #正则表达式，不难，为了找出括号里的所有链接

        img_list = re.findall(ex,respone,re.S)    #re.S是把整个数据看出一个字符串来处理，返回了一个符合条件的所有链接的列表
        for imgSrc in img_list:
            img = requests.get(url=imgSrc,headers=headers).content
            imgName=imgSrc.split('/')[-1]          #字符串的split方法可以以某个字符为界，取其之后或之前的所有内容         
            with open('./img/'+imgName,'wb') as fp:
                fp.write(img)
                print(imgName+"下载成功")

