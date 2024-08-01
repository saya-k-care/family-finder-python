from _datetime import date
import jsonpickle
import traceback
import os
from news.gpt import GPT
from rss_google import RSSGoogle
import logging
from news.get_news import GetNews

def translate_my_desc(news_redis_obj):
    for value in news_redis_obj:
        try:
        # print(value.title)
            if value.is_duplicate == True:
                print ("skip translate_my_desc,", value.description_my)
            else:
                answer = GPT.askGPT_translate_my(value.description)
                value.description_my = answer
        
        except Exception as error:
            print("An exception occurred," , error)
            print(traceback.format_exc())
    return news_redis_obj

logging.basicConfig(filename='store_head_news.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logger = logging.getLogger('urbanGUI')

logging.info("Starting process news")

def process_sports_news(news_src_list, old_news_redis_obj):
    try:
        news_src_list = RSSGoogle.processGoogle_sport_News(news_src_list, old_news_redis_obj)
        print ('Total Length->', len(news_src_list), ' json_data raw -->' , news_src_list)
        news_src_json = jsonpickle.encode(news_src_list)
        
    except Exception as error:
            print("An exception occurred," , error)
            print(traceback.format_exc())
    return news_src_json

def make_news_temp_file(news_src_list,file_name):
    try:
# r = redis.Redis(host='bayi', port=8150, db=0)

        redis_file = open(file_name + "_temp", "w")
        redis_file.write(news_src_json)
        redis_file.close()

        redis_file = open(file_name + "_temp", "r+")
        news_redis_json = redis_file.read()
        redis_file.close()
        
    except Exception as error:
            print("An exception occurred," , error)
            print(traceback.format_exc())
    return news_src_json

news_src_list=[]
old_news_redis_obj = GetNews.get_today_all_news_sport()
news_src_json = process_sports_news(news_src_list, old_news_redis_obj)
news_dir = os.environ.get('NEWS_DIR')
file_name = str(news_dir) + str(date.today()) + "_redis_news_sport.txt"

news_redis_json = make_news_temp_file(news_src_list, file_name)
# r.set(today_date, news_src_json)

#news_redis_json = r.get(today_date);

print ('file news -->' + news_redis_json)
news_redis_obj = jsonpickle.decode(news_redis_json)
print ('length news_redis_obj after save -->' , len(news_redis_obj))

news_redis_obj = translate_my_desc(news_redis_obj)
logging.info("processed bahasa")
redis_file = open(file_name, "w")
        
news_src_json = jsonpickle.encode(news_redis_obj)
news_redis_obj = list(dict.fromkeys(news_redis_obj))
redis_file.write(news_src_json)
redis_file.close()
logging.info("processing done")
#return "Yes, it highlights the need for attitudes to evolve with new policies for effective implementation."
