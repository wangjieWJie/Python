from openai import OpenAI
import os


#单轮对话

#改代码复制于 ：  https://help.aliyun.com/zh/dashscope/developer-reference/use-qwen?spm=a2c4g.11186623.0.i0
def get_response():

    OPENAI_API_KEY = "sk-2dbab0cf371a4735ac8cb66b963c3510"
    client = OpenAI(
        api_key="sk-2dbab0cf371a4735ac8cb66b963c3510", # 如果您没有配置环境变量，请在此处用您的API Key进行替换
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope服务的base_url
    )
    completion = client.chat.completions.create(
        model="qwen-turbo",
        messages=[
            {'role': 'system', 'content': 'You are 王杰, a humorous chinese. all of the questions or statements below are WeChat messages sent to you by others, please review the chat messages carefully and react to them in context.'},
            {'role': 'user', 'content': '我服了'}],
        temperature=0.8,
        top_p=0.8
        )
    print(completion.model_dump_json())



# 多轮对话

def get_responses(messages):
    client = OpenAI(
        # 如果您没有配置环境变量，请在此处用您的API Key进行替换
        api_key="sk-2dbab0cf371a4735ac8cb66b963c3510", 
        # 填写DashScope服务的base_url
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    completion = client.chat.completions.create(
        model="qwen-turbo",
        messages=messages,
        temperature=0.8,
        top_p=0.8
        )
    return completion




    
if __name__ == '__main__':
    #单轮对话
    get_response()

    #多轮对话
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}]
    # 您可以自定义设置对话轮数，当前为3
    for i in range(3):
        user_input = input("请输入：")
        # 将用户问题信息添加到messages列表中
        messages.append({'role': 'user', 'content': user_input})
        assistant_output = get_responses(messages).choices[0].message.content
        # 将大模型的回复信息添加到messages列表中
        messages.append({'role': 'assistant', 'content': assistant_output})
        print(f'用户输入：{user_input}')
        print(f'模型输出：{assistant_output}')
        print('\n')