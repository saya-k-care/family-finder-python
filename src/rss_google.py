import feedparser
from news.news_redis import News
from news.gpt import GPT
import jsonpickle
import json
from news.get_news import GetNews

#r = requests.get("https://news.google.com/rss?hl=en-MY&gl=MY&ceid=MY:en")

rss_url = "https://news.google.com/rss?hl=en-MY&gl=MY&ceid=MY:en"

rss_sport_url =  "https://news.google.com/rss/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVTFaR2dKTldTZ0FQAQ?hl=en-MY&gl=MY&ceid=MY:en"

feed = feedparser.parse(rss_url)

feed_sport = feedparser.parse(rss_sport_url)

class RSSGoogle:
   
    @staticmethod
    def process_malay_cn(cn_my_obj, newsObject):
        print (cn_my_obj)
        print (cn_my_obj.encode('utf-8'))
        cn_my_obj = jsonpickle.encode(cn_my_obj.encode('utf-8'))

        print(cn_my_obj)
        print (json.dumps(str(cn_my_obj).encode('utf-8')))
        json_str = cn_my_obj.decode('utf-8')

        # Load the JSON data
        data = json.loads(json_str)

        # Print the value associated with the "summary" key
        summary_value = data["summary"]
        #chinese_value = data["Chinese"]
        malay_value = data["Bahasa"]
        print("malay_value-->" , malay_value)
        #print("chinese_value-->" , chinese_value)
        print("summary_value-->" , summary_value)
        newsObject.description = summary_value
        #newsObject.description_cn = chinese_value
        newsObject.malay_value = malay_value
        return newsObject

    @staticmethod
    def is_google_news_duplicate(old_news_src_list, value):
        if old_news_src_list != None:
            
            if value in old_news_src_list:
            #print ("value is duplicate-->" + value)
                old_news_src_list = jsonpickle.decode(old_news_src_list)
                for i,x in enumerate(old_news_src_list):
                    if x.title == value:
                    #print ("old_object-->" + x.title)
                        return x
        return None
    
    @staticmethod
    def set_object_news(newsObject, entry):
        newsObject.pubDate = entry.published
        newsObject.title = entry.title
        newsObject.link = entry.link
        newsObject.description = entry.description   
        return newsObject
    
    @staticmethod
    def processGoogleNews(news_src_list, old_news_redis_obj):
        if feed.status == 200:
            for i, entry in enumerate(feed.entries):
                newsObject = News()
                old_object = RSSGoogle.is_google_news_duplicate(old_news_redis_obj, entry.title)
                if (old_object != None):
                    newsObject = News.set_object(old_object)
                    newsObject.is_duplicate = True
                    print ("skip ask GPT -->" + old_object.title)
                else:                    
                    newsObject = RSSGoogle.set_object_news(newsObject, entry)
                    print ("new object, ask GPT -->" + newsObject.title)
                    newsObject.description = GPT.askGPT_description(entry.description)         
                    print ("newsObject.description -->" , newsObject.description)
                    #print ("new_object title-->" , newsObject.title)
                #newsObject = RSSGoogle.process_malay_cn(newsObject.description, newsObject)
                #newsObject.image_url = object['image_url'];
                
                news_src_list.append(newsObject)
                #print("\n", newsObject.description)
                if (i == 20):
                    break
        else:
            print("Failed to get RSS feed. Status code:", feed.status)
        return news_src_list

    @staticmethod
    def processGoogle_sport_News(news_src_list, old_news_redis_obj):
        if feed_sport.status == 200:
            for i, entry in enumerate(feed_sport.entries):
                newsObject = News()
                old_object = RSSGoogle.is_google_news_duplicate(old_news_redis_obj, entry.title)
                if (old_object != None):
                    newsObject = News.set_object(old_object)
                    newsObject.is_duplicate = True
                    print ("skip ask GPT -->" + old_object.title)
                else:                    
                    newsObject = RSSGoogle.set_object_news(newsObject, entry)
                    print ("new object, ask GPT -->" + newsObject.title)
                    newsObject.description = GPT.askGPT_description(entry.description)         
                    print ("newsObject.description -->" , newsObject.description)
                    #print ("new_object title-->" , newsObject.title)
                #newsObject = RSSGoogle.process_malay_cn(newsObject.description, newsObject)
                #newsObject.image_url = object['image_url'];
                
                news_src_list.append(newsObject)
                #print("\n", newsObject.description)
                if (i == 0):
                    break
        else:
            print("Failed to get RSS feed. Status code:", feed.status)
        return news_src_list
    
if __name__ == '__main__':  
    news_src_list=[]
    print ("running")
    old_news_src_list = GetNews.get_today_all_news()
    print ("old_news_src_list--->" ,old_news_src_list)
    news_src_json = RSSGoogle.processGoogleNews(news_src_list, old_news_src_list)
    print ("news_src_json-->" , news_src_json)
    #print (RSSGoogle.processGoogleNews(news_src_list))

