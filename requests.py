#-*- coding = utf-8 -*-
import requests
import threading
 
class myThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        print("Starting " + self.name)
        for i in range(1):
            try:
                crawler(self.name)
            except:
                break
        print("Exiting " + self.name)
 
# 定义功能函数，访问固定url地址
def crawler(threadName):
    urls = ["http://192.168.199.242/","http://192.168.199.242/1.html"]
    headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
                "Accept-Encoding":"gzip",
                "Accept-Language":"zh-CN,zh;q=0.8",
               "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/42.0.2311.90 Safari/537.36" }
    for url in urls:
        try:
            r = requests.get(url,headers=headers,timeout = 20)
            # 打印线程名和响应码
            print(threadName,r.status_code)
        except Exception as e:
            print(threadName,"Error: ",e)
 
# 创建线程列表
threads = []
 
# 开启10个线程
for i in range(10):
    # 给每个线程命名
    tName="url"+str(i)
    thread=myThread(tName)
    thread.start()
    # 将线程添加到线程列表
    threads.append(thread)
    
#等待所有线程完成
for t in threads:
	t.join()
