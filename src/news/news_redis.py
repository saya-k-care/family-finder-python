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
    bible_ai = None
    
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
