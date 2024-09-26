import os
import requests
import json

def send_message_to_telegram(message, button_text='想反馈问题❓反馈个锤子，哪有人给你维护!', button_url='https://www.google.com'):
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')

    if not telegram_bot_token or not telegram_chat_id:
        print("Error: Missing environment variables.")
        return

    url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'
    payload = {
        'chat_id': telegram_chat_id,
        'text': message,
        'reply_markup': json.dumps({
            'inline_keyboard': [[{'text': button_text, 'url': button_url}]]
        })
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code != 200:
        print(f"Error: {response.status_code}, {response.text}")
    
    return response.json()

if __name__ == "__main__":
    # 从环境变量获取自定义消息
    custom_message = os.getenv('CUSTOM_MESSAGE', '我是默认的提醒消息！！！！')
    response = send_message_to_telegram(custom_message)
    print(response)