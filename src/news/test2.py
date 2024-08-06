import json
import jsonpickle
from news.get_news import GetNews
from rss_google import RSSGoogle
import traceback
from news.news_redis import News

def process_google_news(news_src_list, old_news_redis_obj):
    try:
        news_src_list = RSSGoogle.processGoogleNews(news_src_list, old_news_redis_obj)
        print('Total Length->', len(news_src_list), ' json_data raw -->', news_src_list)
        news_src_json = jsonpickle.encode(news_src_list)
        print('news_src_json  -->', news_src_json)
    except Exception as error:
        print("An exception occurred:", error)
        print(traceback.format_exc())
    return news_src_json

def process_cn(news_redis_obj):
    try:
        for value in news_redis_obj:
            try:
                news_prepare_cn = News()
                news_prepare_cn.description = value.title
                news_prepare_cn.bible_life = value.bible_life
                json_string = 'description_cn:' + str(news_prepare_cn.description) + '  + bible_life_cn:' + str(news_prepare_cn.bible_life)
                
                print("news_cn_json-->" + json_string)
                                        
                data = '{"description_cn": ["出色"], "bible_life_cn": ["面对压力"], "pinyin": ["面对压力"]}'

                json_dict = json.loads(data)
                value.description_cn = json_dict["description_cn"]
                value.bible_life_cn = json_dict["bible_life_cn"]
                value.bible_life_cn = json_dict["bible_life_cn"]

            except Exception as error:
                print("An exception occurred:", error)
                print(traceback.format_exc())
    except Exception as error:
        print("An exception occurred:", error)
        print(traceback.format_exc())
    return news_redis_obj

# Write JSON data to a file
file_path = "player_info.json"

news_src_list = []
old_news_redis_obj = GetNews.get_today_all_news()
news_src_json = process_google_news(news_src_list, old_news_redis_obj)

news = News()
news_src_list.append(news)

news_redis_obj = jsonpickle.decode(news_src_json)

news_src_json = process_cn(news_redis_obj)

news_src_json = jsonpickle.encode(news_redis_obj)

with open(file_path, "w", encoding="utf-8") as file:
    file.write(news_src_json)

# Read the JSON data from the file and print it
with open(file_path, "r", encoding="utf-8") as file:
    read_data = file.read()
json_obj = jsonpickle.decode(read_data)

for news in json_obj:
    print("news description_cn->", news.description_cn)
    print("news bible_life_cn->", news.bible_life_cn)