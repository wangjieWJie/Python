import requests
import json

url = "https://api.openai-hk.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer hk-6vi52y1000039795d87e01734779f587c5d4cbe9812bbb9c"
}

data = {
    "max_tokens": 1200,
    "model": "gpt-3.5-turbo",
    "temperature": 0.8,
    "top_p": 1,
    "presence_penalty": 1,
    "messages": [
        {
            "role": "system",
            "content": "You are 王杰, a humorous chinese. all of the questions or statements below are WeChat messages sent to you by others, please review the chat messages carefully and react to them in context."
        },
        {
            "role": "user",
            "content": "王杰是翘嘴嘛"
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data).encode('utf-8') )
result = response.content.decode("utf-8")

print(result)