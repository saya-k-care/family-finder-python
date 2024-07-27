
import sys
from openai.types.chat.chat_completion import ChatCompletion

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

str1 = "ChatCompletion(id='chatcmpl-9on2sEj4BoQScVmTFBqfYSueV9hKo', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='No.', role='assistant', function_call=None, tool_calls=None))], created=1721891958, model='gpt-4o-mini-2024-07-18', object='chat.completion', service_tier=None, system_fingerprint='fp_661538dc1f', usage=CompletionUsage(completion_tokens=2, prompt_tokens=32, total_tokens=34))"


#ChatCompletion obj = eval(str1)

#print (obj)