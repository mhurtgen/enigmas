# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 16:17:20 2016

@author: mhurtgen
"""
import json,urllib
import tkinter as tk


    
def geturl(which,data):
    """get the url of the desired newspaper"""
    url1="https://newsapi.org/v1/articles?source="
    
    if which=='Das Bild':
        url2="bild&sortBy=latest&apiKey="
        url=url1+url2+data
        #url="https://newsapi.org/v1/articles?source=bild&sortBy=latest&apiKey=1eed8bf5067c4989822bdf396b2e7b3b"
    elif which=='Die Zeit':
        url2="die-zeit&sortBy=latest&apiKey="
        #url="https://newsapi.org/v1/articles?source=die-zeit&sortBy=latest&apiKey=1eed8bf5067c4989822bdf396b2e7b3b"
        url=url1+url2+data        
    elif which=='BBC':
        url2="bbc-news&sortBy=top&apiKey="
        #url="https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=1eed8bf5067c4989822bdf396b2e7b3b"
        url=url1+url2+data                
    elif which=='Hacker':
        url2="hacker-news&sortBy=top&apiKey="
#        url="https://newsapi.org/v1/articles?source=hacker-news&sortBy=top&apiKey=1eed8bf5067c4989822bdf396b2e7b3b"
        url=url1+url2+data
    elif which=='Newsweek':
        url2="newsweek&sortBy=top&apiKey="
        #url="https://newsapi.org/v1/articles?source=newsweek&sortBy=top&apiKey=1eed8bf5067c4989822bdf396b2e7b3b"
        url=url1+url2+data
    elif which=='Time':
        url2="time&sortBy=top&apiKey="
        #url="https://newsapi.org/v1/articles?source=time&sortBy=top&apiKey=1eed8bf5067c4989822bdf396b2e7b3b"
        url=url1+url2+data
    elif which=='Techcrunch':
        url2="techcrunch&sortBy=top&apiKey="
        #url="https://newsapi.org/v1/articles?source=techcrunch&sortBy=top&apiKey=1eed8bf5067c4989822bdf396b2e7b3b"
        url=url1+url2+data        
    elif which=='Techradar':
        url2="techradar&sortBy=top&apiKey="
        #url="https://newsapi.org/v1/articles?source=techradar&sortBy=top&apiKey=1eed8bf5067c4989822bdf396b2e7b3b"
        url=url1+url2+data
    elif which=='Economist':
        url2="the-economist&sortBy=top&apiKey="
        #url=" https://newsapi.org/v1/articles?source=the-economist&sortBy=top&apiKey=1eed8bf5067c4989822bdf396b2e7b3b"
        url=url1+url2+data
    elif which=='USA':
        url2="usa-today&sortBy=top&apiKey="
        url="https://newsapi.org/v1/articles?source=usa-today&sortBy=top&apiKey=1eed8bf5067c4989822bdf396b2e7b3b"
        url=url1+url2+data
    return url

def getdict(listjson):
    """return a list of dictionaries from json list"""
    articles=dict()
    count=0

   #print(response.content)
    for item in listjson["articles"]:
        indarticle=dict()
        title=item["title"]
        url=item["url"]
        desc=item["description"]
    
        indarticle["title"]=title
        indarticle["url"]=url
        indarticle["desc"]=desc
    
        articles[count]=indarticle
        count+=1
    return articles

def getarticles(articles):
    """print articles in newspaper API"""
    lg=len(articles)    
    for i in range(0,lg):     
        print('--------------------------')
        print(articles[i]["title"])
        #        f.write("\n")
        print(articles[i]["url"])
#        f.write("\n")
        print(articles[i]["desc"])
        print('--------------------------')

def newspr(media):
        articles=main(media)
        lg=len(articles)
      
        for i in range(0,lg): 

            title=articles[i]["title"]
            url=articles[i]["url"]
            Buttonart=tk.Button(self, text=title,command=lambda: opart(url))
            Buttonart.pack()


#response = requests.get("https://newsapi.org/v1/articles?source=bild&sortBy=latest&apiKey=1eed8bf5067c4989822bdf396b2e7b3b")
def main(which,data):
    """get articles of newspaper in the list"""    
           
        
    url=geturl(which,data)
    #print(url)   
    info=urllib.request.urlopen(url)
            
            #returns corresponding strings
    infotxt=info.read().decode('utf-8')
            #returns json objects taken from list                 
    objson = json.loads(infotxt)    
    
    articles=getdict(objson)
    
    return articles
#print(listjson)
    #getarticles(articles)
        

        
    

#main()    


#        f.write("\n")
        


    
#for item in articles:
#    print(item, articles[item])
#df=pd.DataFrame(articles)
#df.to_html('bild.html')