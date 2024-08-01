import jsonpickle
import os
import json
import traceback
from news.gpt import GPT
from _datetime import date


class GetNews:
    @staticmethod
    def getNews(date, is_positive):
        news_dir = os.environ.get('NEWS_DIR')
        file_name = str(news_dir) + str(date) + "_redis_news.txt"
        print ('Opening file_name-->' , file_name)
        redis_file = open(file_name, "r+")
        news_redis_json = redis_file.read()
        redis_file.close()

        news_redis_obj = jsonpickle.decode(news_redis_json)
        news_redis_obj = list(filter(lambda x: x.isPositive == is_positive, news_redis_obj))

        json_news = jsonpickle.encode(news_redis_obj)
        return json_news

    @staticmethod
    def getHeadline():
        news_dir = os.environ.get('NEWS_DIR')
        file_name = str(news_dir) + str(date.today()) + "_redis_news.txt"

        redis_file = open(file_name, "r+")
        news_redis_json = redis_file.read()
        redis_file.close()
        
        print ('file news -->' + news_redis_json)
        news_redis_obj = jsonpickle.decode(news_redis_json)
        news_redis_obj = list(dict.fromkeys(news_redis_obj))
        print ('length news_redis_obj after clean up -->' , len(news_redis_obj))

        for i, value in enumerate(news_redis_obj):
            try:
                news_no = "News ID " + str(i) + ":" + value.title
                print (news_no)
        
            except Exception as error:
                print("An exception occurred," , error)
                print(traceback.format_exc())
        
print (GetNews.getHeadline())
#print (GetNews.getNews("2024-07-26", True))