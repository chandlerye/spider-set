import requests                                        #请求库
from bs4 import BeautifulSoup		               #标签处理库

if __name__=="__main__":
    url = 'https://www.sogotxt.com/book/0/67/'          #有目录的那个网页
    headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }

    respone = requests.get(url=url,headers=headers).content
    soup = BeautifulSoup(respone,'lxml')                #将网页信息转成soup对象
 
    page_list =  soup.select('#list > dl > dd >a')      #select方法用来选择层叠样式，这里选择所有a标签
 
    fp = open('./xiaoshuo.txt','w',encoding='utf-8')    #储存

    for a in page_list:
        title=a.string    				#获取a标签的内容
        a_url = "https://www.sogotxt.com/" + a['href']  #获得目录条目指向页面的链接
        page_content = requests.get(url=a_url,headers=headers).content        #请求单个页面
        page_soup = BeautifulSoup(page_content)
        div_tag = page_soup.find('div',id='content')    #获取文本内容
        content = div_tag.text    			#转成文本，可以将标签中的br标签去掉
        fp.write(title+":"+content)  			#写入标题和内容
        print(title +"下载成功")









