import requests
import json
import nltk
from newspaper import Article
api_key = "your api key from NewsAPI"
url = f"https://newsapi.org/v2/top-headlines?sources=google-news&pageSize=1&apiKey={api_key}"
response = requests.get(url)
nltk.download('punkt')
if response.status_code == 200:
    data = json.loads(response.text)
    articles = data["articles"]
    articleactual = articles[0]
    url1 = articleactual["url"]
else:
    print("Failed to fetch the news article")

article = Article(url1)
article.download()
article.parse()
print(url1)
with open('article.txt', 'w') as f:
     f.write(article.text)

article.nlp()
with open('summary.txt', 'w') as f:
  f.write(article.summary)
  
# TODO: 
# 1. Use newspaper3k module to get keywords from article and fetch a relevant video. 
# 2. Use pyttsx3 or any other text to speech service to get the audio.
