This project creates a Tkinter interface. The Media menu lets one choose a newspaper, and the titles of the 
last news articles are shown in the main frame. 

Now, the program is not very clean nor does it use the memory in a very efficient way. Another weak point is that, 
in order to make it work, the user has to save the full link with API key in a text file data.txt. The link is obtained 
by signing up on the newsapi.org website. 

The objective was of course to make the application self-sufficient so that the program goes to look if it finds 
a file called data.txt on the current directory, if it doesn't, it will print ask the user to give in the http link, 
else, it just carries on. 

Unfortunately, I was not able to initialize the data variable (variable giving the API key) correctly since the program 
loads up all the pages before it actually asks the user for the http link containing the API key. I get an internal server 
error if I try to do this. I suppose I should fundamentally change the program structure, but I don't know how to do this.

Any help is welcome.

Thanks.

