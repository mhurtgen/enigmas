# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 19:50:37 2016

@author: mhurtgen
"""

# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	
#In its present form, the program requires that the user stors the link returned by the APInews website after 
#signing up be stored in a file ccalled 'data.txt' stored in the same directoy as this file..
import tkinter as tk
import newsAPI_fin
import webbrowser


LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        menubar = tk.Menu(container)
        
        com = tk.Menu(menubar, tearoff=0)
        #media.add_command(label="Save settings", command=lambda: controller.show_frame(PageOne))
        com.add_separator()        
        
        com.add_command(label='Exit',command=lambda: self.endfile())#sys.exit())  
        
        menubar.add_cascade(label='File',menu=com)
        
        news = tk.Menu(menubar, tearoff=0)
        #media.add_command(label="Save settings", command=lambda: controller.show_frame(PageOne))
        news.add_separator()        
        
        news.add_command(label='BBC',command=lambda: self.show_frame(BBC))
        news.add_command(label='Newsweek',command=lambda: self.show_frame(Newsweek))  
        news.add_command(label='Time',command=lambda: self.show_frame(Time))     
        news.add_command(label='USA Today',command=lambda: self.show_frame(USA))     
        news.add_command(label='The Economist',command=lambda: self.show_frame(Economist))  
        news.add_command(label='Techcrunch',command=lambda: self.show_frame(Techcrunch))  
        news.add_command(label='Hacker',command=lambda: self.show_frame(Hacker))          
        news.add_command(label='Das Bild',command=lambda: self.show_frame(Bild))
        news.add_command(label='Die Zeit',command=lambda: self.show_frame(Zeit))          
        
        
        menubar.add_cascade(label='Media',menu=news)
        
#        menubar = tk.Menu(container)
        
        
        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (StartPage, Newsweek, Time, USA, Economist, Techcrunch, Hacker, Bild, Zeit, BBC):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
    
    def endfile(self):        
        self.destroy()        
        self.quit()
        

        
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        
        label = tk.Label(self, text="Choose your media", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
    def getAPI(self):
        """returns the API key"""
        with open('data.txt','r') as f:
                data=f.read()     
        lg=len(data)

        dt=data.rfind('=')
        #print(dt)
        #print(data[dt+1:lg])
        return data[dt+1:lg]
        #self.newspr('Das Bild')
    def newspr(self,media,data):
        """prints out the list of articles in the frame"""
        articles=newsAPI_fin.main(media,data)
        lg=len(articles)
      
        for i in range(0,lg): 

            title=articles[i]["title"]
            url=articles[i]["url"]
            Buttonart=tk.Button(self, text=title,command=lambda url_curr= url: webbrowser.open(url_curr))
            Buttonart.pack()

class Bild(StartPage,tk.Frame):
    """get articles of particular paper"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Das Bild", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        data=super(Bild,self).getAPI()
        
        self.newspr('Das Bild',data)
    
class Zeit(StartPage,tk.Frame):
    """get articles of particular paper"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Die Zeit", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        data=super(Zeit,self).getAPI()
        self.newspr('Die Zeit',data)

class BBC(StartPage,tk.Frame):
    """get articles of particular paper"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="BBC", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        data=super(BBC,self).getAPI()
        self.newspr('BBC',data)
    
        
class Newsweek(StartPage,tk.Frame):
    """get articles of particular paper"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Newsweek", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        data=super(Newsweek,self).getAPI()
        self.newspr('Newsweek',data)
        
class Time(StartPage,tk.Frame):
    """get articles of particular paper"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Time", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        data=super(Time,self).getAPI()
        self.newspr('Time',data)

class USA(StartPage,tk.Frame):
    """get articles of particular paper"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="USA today", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        data=super(USA,self).getAPI()
        self.newspr('USA',data)

class Economist(StartPage,tk.Frame):
    """get articles of particular paper"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="The Economist", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        data=super(Economist,self).getAPI()
        self.newspr('Economist',data)

class Techcrunch(StartPage,tk.Frame):
    """get articles of particular paper"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Techcrunch", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        data=super(Techcrunch,self).getAPI()
        self.newspr('Techcrunch',data)

class Techradar(StartPage,tk.Frame):
    """get articles of particular paper"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Techradar", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        data=super(Techradar,self).getAPI()
        self.newspr('Techradar',data)

class Hacker(StartPage,tk.Frame):
    """get articles of particular paper"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hacker", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        data=super(Hacker,self).getAPI()
        self.newspr('Hacker',data)

app = SeaofBTCapp()
app.mainloop()