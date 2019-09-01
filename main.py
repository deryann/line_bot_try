from linebot import LineBotApi
from linebot.models import TextSendMessage
import json
import codecs


def main_fun(dic_data):
    line_bot_api = LineBotApi(dic_data['LINE_API']['CHANNEL_ASSESS_TOKEN'])
    # push message to one user
    line_bot_api.push_message(dic_data['LINE_API']['TO_USER_ID'], TextSendMessage(text='Hello World!'))

    # push message to one group
    line_bot_api.push_message(dic_data['LINE_API']['TO_GROUP_ID'], TextSendMessage(text='時間到了~打 lol 囉!'))


def get_json_data():
    with codecs.open('config.json') as f:
        data = json.load(f)
        print(data)
    return data
    pass


if __name__ == "__main__":
    dic_config = get_json_data()
    main_fun(dic_config)
