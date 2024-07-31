import openai
import os
from _datetime import date
import requests

ai_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = ai_key

class GPT:
    @staticmethod
    def askGPT(str):
        ques = str + " .Is this a positive, not politic related and important news? Answer yes or no and explain in less than 15 words";
        completion = openai.chat.completions.create(
            model="gpt-4o-mini",
            
            messages=[
                {"role": "user", "content": ques}
                ],)
    
        print(completion.choices[0].message.content)
        return completion.choices[0].message.content

    @staticmethod
    def askGPT_well_being(str):
        ques = str + " .The corruption surge. How is this news impact well being if reading too much. Explain in less than 15 words";
        completion = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": ques}
                ],)
    
        print(completion.choices[0].message.content)
        return completion.choices[0].message.content

    @staticmethod
    def askGPT_badminton():
        today_date = str(date.today())
        r = requests.get("https://news.google.com/rss/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVTFaR2dKTldTZ0FQAQ?hl=en-MY&gl=MY&ceid=MY:en")
        trim_str = r.text[0:2000]
        print ("trim_str-->" + trim_str)
        ques = trim_str + " . Give me sport comments summary in 50 words";
        completion = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": ques}
                ],)
        
        result = completion.choices[0].message.content
        print(result)
        
        #summary = result + " .Provide a score result and some sport comments"
        #completion = openai.chat.completions.create(
        #    model="gpt-4o",
        #    messages=[
        #        {"role": "user", "content": summary}
        #        ],)
        #result = completion.choices[0].message.content
        #print(result)      
        return completion.choices[0].message.content
    
    @staticmethod
    def askGPT_bible(str):
        ques = str + " Map this news to Bible verse in less than 20 words";
        completion = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": ques}
                ],)
    
        print(completion.choices[0].message.content)
        return completion.choices[0].message.content

    @staticmethod
    def askGPT_bible_life(str):
        ques = str + " . Give a Bible life example in less than 50 words";
        completion = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": ques}
                ],)
    
        print(completion.choices[0].message.content)
        return completion.choices[0].message.content

    @staticmethod
    def askGPT_description(str):
        ques = str + " . Summarize this in less than 50 words";
        completion = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": ques}
                ],)
    
        print(completion.choices[0].message.content)
        return completion.choices[0].message.content
            
    @staticmethod
    def askGPTDummyYes(str):
        return "Yes, it highlights the need for attitudes to evolve with new policies for effective implementation."

    @staticmethod
    def askGPTDummyWellBeing(str):
        return "Excessive exposure to corruption news can heighten stress and erode trust in institutions."

    @staticmethod
    def askGPTDummyNo(str):
        return "No, it reflects divisive rhetoric, which can intensify political tensions."       
     
#GPT.askGPT("Over 142,000 individuals released from bankruptcy under Second Chance Policy, says PM.")
GPT.askGPT_badminton()
