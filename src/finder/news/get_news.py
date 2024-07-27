import jsonpickle
import os
import json


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

print (GetNews.getNews("2024-07-26", True))