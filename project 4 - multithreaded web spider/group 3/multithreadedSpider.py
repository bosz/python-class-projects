import urllib
import http.cookiejar
import re
import sys
from time import sleep
import threading
import collections

QUEUE=collections.deque()#to realize simple BFS algorithm
DATA={}#completed results
COUNTER=0#the number of urls added to DATA
VISITED=set()#visited urls
L=threading.Lock()

def fetch_html(url,opener):
    try:
        raw_html=opener.open(url,timeout=5).read()
        try:#try two different encodings
            txt=raw_html.decode('UTF-8')
        except:
            txt=raw_html.decode('gbk')
        return txt
    except:
        return None

#multithreading unit function
def unit(max_pages,title_model,link_model,opener):
    global QUEUE,DATA,COUNTER,VISITED,L
    sleep_times=0
    while True:
    
        L.acquire()#acquire the lock
        
        if COUNTER==max_pages:
            L.release()#must release the lock before the termination of this thread
            break
        
        if not QUEUE:#if one thread can not pop url from the QUEUE, wait a while
            L.release()
            sleep(1)
            sleep_times+=1
            if sleep_times==10:#If this thread has waited too much time, it will die.
                break
            continue
        sleep_times=0
        
        current_url=QUEUE.popleft()
        
        L.release()
        
        current_html=fetch_html(current_url,opener)#only this part uses multithreading
        
        L.acquire()
        
        if COUNTER==max_pages:
            L.release()
            break
        
        try:
            title=title_model.search(current_html).group(1)
            links=link_model.findall(current_html)
        except:
            L.release()
            continue
        
        COUNTER += 1
        title='*'+str(COUNTER)+'*'+title
        DATA[title]=current_url#save to DATA
        print(threading.current_thread().getName()+' obtained '+title+' '+current_url)
        
        for x in links:
            if x[-1]=='/':#"http://..."<=>"http://.../"
                x=x[0:-1]
            if x not in VISITED:
                QUEUE.append(x)
                VISITED |= {x}
        
        L.release()
    print(threading.current_thread().getName()+" has terminated.")

def main(entrance_url,max_pages,threads_count):
    global QUEUE,DATA,VISITED
    
    QUEUE.append(entrance_url)
    VISITED |= {entrance_url}
    
    opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    opener.addheaders=[('Connection','Keep-Alive'),('Accept','text/html'),('Accept-Language','en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3'),('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0')]
    
    #analyze the html by regular expressions
    title_model=re.compile(r"<title>(.*?)</title>",re.DOTALL)
    link_model=re.compile('href=\"(.+?)\"',re.DOTALL)
    
    for i in range(0,threads_count):
        threading.Thread(target=unit,args=(max_pages,title_model,link_model,opener)).start()
    
    while threading.active_count()>1:
        sleep(2)
    
    try:
        fileObj=open("results.txt",'w',encoding="utf-8")
        fileObj.write(str(DATA))
        fileObj.close()
        print("These data have been saved to the current path.")
    except:
        print("[Error]Save failed.")

main(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))