from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, JoinEvent
)

import codecs
import json

app = Flask(__name__)


def get_json_data():
    with codecs.open('config.json') as f:
        data = json.load(f)
        print(data)
    return data


dic_config = get_json_data()

line_bot_api = LineBotApi(dic_config['LINE_API']['CHANNEL_ASSESS_TOKEN'])
handler = WebhookHandler(dic_config['LINE_API']['WEB_HOOK_HANDLER'])


@app.route("/")
def home():
    return 'home OK'


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="you said:" + event.message.text))


@handler.add(JoinEvent)
def handle_join(event):
    try:
        newcoming_text = "謝謝邀請我這個機器來至此群組！！我會盡力為大家服務的～(group_id = {})".format(event.source.group_id)
        print(newcoming_text)
    except Exception as e:
        print(e)
        newcoming_text = "謝謝邀請我這個機器來至此群組！！我會盡力為大家服務的～(error)"
        pass

    line_bot_api.reply_message(
        event.reply_token,
        TextMessage(text=newcoming_text)
    )
    print("JoinEvent =", JoinEvent)


if __name__ == "__main__":
    app.run()
