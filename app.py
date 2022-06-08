#載入LineBot所需要的模組
from flask import Flask, request, abort
 
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import 
 
# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('6TrqOKzDr76RVKb5Xw2nEZ5mP9KG889170IqexK4J4KgxOoy62Hb7Kmiv4YIoq0oEzUO0+iqGkWCMs/7x4b0JTRFHSykU4ID3DNBe5KpJCQHQ95qsGqoiGg2cJGDaAwBwpYoMtFE8heIRe3gIOhbEAdB04t89/1O/w1cDnyilFU=')
 
# 必須放上自己的Channel Secret
handler = WebhookHandler('9742010e899994246004b699b1ff042c')
# U5366202c11a895d1531620d6170eae28

line_bot_api.push_message('U5366202c11a895d1531620d6170eae28', TextSendMessage(text='你可以開始了'))
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
        abort(400)
 
    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

