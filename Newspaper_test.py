#pip3 install --ignore-installed --upgrade newspaper3k



from newspaper import Article
url = 'https://baijiahao.baidu.com/s?id=1622793331171522033&wfr=spider&for=pc'
news = Article(url, language='zh')
news .download()
news .parse()
print(news.text)
print(news.title)

print(news.html)
print(news.authors)
print(news.top_image)
print(news.movies)
print(news.keywords)
print(news.summary)
