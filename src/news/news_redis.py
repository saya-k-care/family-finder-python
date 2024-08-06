import json
from pickle import NONE
class News:
    
    title = None
    link = None
    image_url = None
    pubDate = None
    isPositive = None
    news_ai = None
    well_being_ai = None
    description = None
    description_my = None
    description_cn = None
    bible_ai = None
    bible_life = None
    bible_life_cn = None
    is_duplicate = False
    headline = None
    pinyin = None
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
        
    @staticmethod
    def setNews(json_data):
        print ('json_data ====' , json_data)
        news = News()
        news = json.loads(json_data)

        print ('news received ====' , news)

        # convert received person to local Object
        newsLocal = News()
        newsLocal.__list__ = news

        return newsLocal 

    @staticmethod
    def set_object(old_object):
        news = News()
        news.title = old_object.title
        news.link = old_object.link
        news.image_url = old_object.image_url
        news.pubDate = old_object.pubDate
        news.isPositive = old_object.isPositive
        news.news_ai = old_object.news_ai
        news.well_being_ai = old_object.well_being_ai
        news.description = old_object.description
        news.description = old_object.description
        news.bible_life = old_object.bible_life
        news.description_my  = old_object.description_my
        news.headline = old_object.headline
        news.bible_life_cn = old_object.bible_life_cn
        news.description_cn = old_object.description_cn
        news.pinyin = old_object.pinyin
        return news 