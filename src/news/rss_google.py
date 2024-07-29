
from dateparser.data.numeral_translation_data import root
import feedparser
from news.news_redis import News
from news.gpt import GPT

#r = requests.get("https://news.google.com/rss?hl=en-MY&gl=MY&ceid=MY:en")

rss_url = "https://news.google.com/rss?hl=en-MY&gl=MY&ceid=MY:en"
feed = feedparser.parse(rss_url)

class RSSGoogle:
    @staticmethod
    def processGoogleNews(news_src_list):
        if feed.status == 200:
            for entry in feed.entries:
                newsObject = News()
                #print (entry)
                newsObject.pubDate = entry.published
                newsObject.title = entry.title
                newsObject.link = entry.link
                newsObject.description = entry.description                
                newsObject.description = GPT.askGPT_description(entry.description)
                #newsObject.image_url = object['image_url'];
                news_src_list.append(newsObject)
                print("\n", entry.title)
                print(entry.link)
                print (newsObject.description)
                news_src_list.append(newsObject)
        else:
            print("Failed to get RSS feed. Status code:", feed.status)
        return news_src_list
    
news_src_list=[]
print (RSSGoogle.processGoogleNews(news_src_list))
