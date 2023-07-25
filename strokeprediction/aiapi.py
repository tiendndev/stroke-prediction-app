# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

# import config
from strokeprediction import config

api_key = config.DevelopmentConfig.OPENAI_KEY
openai.api_key = api_key


def generateChatResponse(prompt):
    messages = []
    messages.append(
        {"role": "system", "content": "You are a helpful assistant."})

    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)

    try:
        answer = response['choices'][0]['message']['content'].replace(
            '\n', '<br>')
    except:
        answer = 'Comeback later!!'

    return answer
