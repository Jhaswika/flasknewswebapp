from flask import Flask ,render_template
from newsapi import NewsApiClient




app=Flask(__name__)
@app.route("/")
def main():
    return render_template("main.html")


@app.route("/index")
def index():
    newsapi=NewsApiClient(api_key="37f08828bed8408ca58538023c8e024e")
    topheadlines=newsapi.get_top_headlines(sources="al-jazeera-english")


    articles=topheadlines['articles']

    desc=[]
    news=[]
    img=[]


    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    

    mylist=zip(news,desc,img)


    return render_template('index.html',context=mylist)
@app.route("/bbc")    
def bbc():
    newsapi=NewsApiClient(api_key="37f08828bed8408ca58538023c8e024e")
    topheadlines=newsapi.get_top_headlines(sources="bbc-news")


    articles=topheadlines['articles']

    desc=[]
    news=[]
    img=[]


    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    

    mylist=zip(news,desc,img)


    return render_template('bbc.html',context=mylist)

@app.route("/google")    
def google():
    newsapi=NewsApiClient(api_key="37f08828bed8408ca58538023c8e024e")
    topheadlines=newsapi.get_top_headlines(sources="google-news-ar")


    articles=topheadlines['articles']

    desc=[]
    news=[]
    img=[]


    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    

    mylist=zip(news,desc,img)


    return render_template('google.html',context=mylist)

@app.route("/abc")    
def abc():
    newsapi=NewsApiClient(api_key="37f08828bed8408ca58538023c8e024e")
    topheadlines=newsapi.get_top_headlines(sources="abc-news")


    articles=topheadlines['articles']

    desc=[]
    news=[]
    img=[]


    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    

    mylist=zip(news,desc,img)


    return render_template('abc.html',context=mylist)

@app.route("/cbc")    
def cbc():
    newsapi=NewsApiClient(api_key="37f08828bed8408ca58538023c8e024e")
    topheadlines=newsapi.get_top_headlines(sources="cbc-news")


    articles=topheadlines['articles']

    desc=[]
    news=[]
    img=[]


    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    

    mylist=zip(news,desc,img)


    return render_template('cbc.html',context=mylist)

@app.route("/foxsport")    
def foxsport():
    newsapi=NewsApiClient(api_key="37f08828bed8408ca58538023c8e024e")
    topheadlines=newsapi.get_top_headlines(sources="fox-sports")


    articles=topheadlines['articles']

    desc=[]
    news=[]
    img=[]


    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    

    mylist=zip(news,desc,img)


    return render_template('foxsport.html',context=mylist)


if __name__=="__main__":
    app.run(debug=True)
        
        
