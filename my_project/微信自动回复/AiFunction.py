# 此文件用于定义Ai相关的函数

from openai import OpenAI


class QwenTurbo():
    def __init__(self) -> None:
        self.messages = [{'role': 'system', 'content': '你是一个无所不知的天才，名字叫做王杰，来自于山东滨州，。你将简短的回答所有的问题，绝不拖泥带水'}]
        self.api = "sk-2dbab0cf371a4735ac8cb66b963c3510"
        # 阿里云通义千问地址
        self.tongyi = "https://dashscope.aliyuncs.com/compatible-mode/v1"


    def chat_qwen_turbo(self,user_input):

        # 将用户的问题添加到消息列表
        self.messages.append({'role': 'user', 'content': user_input})

        client = OpenAI(
        # 我的API
        api_key = self.api, 
        # 填写DashScope服务的base_url
        base_url = self.tongyi,
        )
        completion = client.chat.completions.create(
        model="qwen-turbo",
        #用户的以往问答和本次问答
        messages=self.messages,
        temperature=0.8,
        top_p=0.8
        )

        # 摘录出 Ai 的回答
        assistant_output = completion.choices[0].message.content
        #将AI的回答添加到消息列表
        self.messages.append({'role': 'assistant', 'content': assistant_output})

        # 将Ai的回答返回去
        return assistant_output




class ChatGpt():
    def __init__(self) -> None:
        self.messages = [{'role': 'system', 'content': 'You are Wang Jie, a humorous boy. Your messages are all WeChat messages sent to you by others, please read the chat messages carefully and reply briefly according to the context.'}]
 
        # 实例化OpenAI变量，而不是使用全局变量
        self.client = OpenAI(
                            api_key = "hk-6vi52y1000039795d87e01734779f587c5d4cbe9812bbb9c",
                            base_url = "https://api.openai-hk.com/v1"
                            )

    def chat_qwen_turbo(self,user_input):

        # 将用户的问题添加到消息列表
        self.messages.append({'role': 'user', 'content': user_input})

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            #用户的以往问答和本次问答
            messages=self.messages,
            max_tokens = 800,
            temperature = 0.8,
            top_p = 1,
            presence_penalty = 1 
        )

        # 摘录出 Ai 的回答
        assistant_output = completion.choices[0].message.content
        #将AI的回答添加到消息列表
        self.messages.append({'role': 'assistant', 'content': assistant_output})

        # 将Ai的回答返回去
        return assistant_output

