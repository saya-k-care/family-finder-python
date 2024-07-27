import openai
openai.api_key = 'sk-None-ja7roqsWq1DCjWErYVqJT3BlbkFJqZ6eNRY9Nzslev5hPwov'

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
    def askGPTDummyYes(str):
        return "Yes, it highlights the need for attitudes to evolve with new policies for effective implementation."

    @staticmethod
    def askGPTDummyWellBeing(str):
        return "Excessive exposure to corruption news can heighten stress and erode trust in institutions."

    @staticmethod
    def askGPTDummyNo(str):
        return "No, it reflects divisive rhetoric, which can intensify political tensions."        
GPT.askGPT("Over 142,000 individuals released from bankruptcy under Second Chance Policy, says PM.")
