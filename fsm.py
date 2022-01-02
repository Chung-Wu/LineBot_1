from transitions.extensions import GraphMachine
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
from utils import send_text_message

from userdata import User
import graph
import os
import userdata


user = User(0)

class TocMachine(GraphMachine):
    
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
     
    def is_going_to_purchase_bread(self, event):
        text = event.message.text

        if("added bread" in text.lower() and "shopping cart" in text.lower()):
            temp = text.split(' ')
            temp_bread = temp[2]
            if(temp_bread == '01'):
                user.add_bread("蒜香起士")
            elif(temp_bread == '02'):
                user.add_bread("黑旋風")
            elif(temp_bread == '03'):
                user.add_bread("墨西哥奶酥")
            elif(temp_bread == '04'):
                user.add_bread("肉鬆沙拉")
            elif(temp_bread == '05'):
                user.add_bread("海苔肉鬆")
            elif(temp_bread == '06'):
                user.add_bread("蔥捲")
            elif(temp_bread == '07'):
                user.add_bread("雙條培根")
            elif(temp_bread == '08'):
                user.add_bread("起酥肉鬆")
            elif(temp_bread == '09'):
                user.add_bread("網狀鮪魚")
            elif(temp_bread == '10'):
                user.add_bread("天然雙色")
            elif(temp_bread == '11'):
                user.add_bread("牛奶波蘿")
            elif(temp_bread == '12'):
                user.add_bread("起酥紅豆")
            
            

        
        return text.lower() == "purchase bread" or ("added bread" in text.lower() and "shopping cart" in text.lower())
    
    def on_enter_purchase_bread(self, event):

        reply_token = event.reply_token
        message = graph.bread
        message_to_reply = FlexSendMessage("show the list", message)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, message_to_reply)
        

    def on_exit_state1(self):
        print("Leaving state1")

    def on_exit_state2(self):
        print("Leaving state2")

    def is_going_to_shopping_list(self, event):
        
        text = event.message.text
        reply_token = event.reply_token
        
        
        
    
        #send_text_message(reply_token, temp)
        # send_text_message(reply_token, "added" in text.lower() and "shopping cart" in text.lower())

        #return text.lower() == "added to shopping cart"
        # return "added" in text.lower() and "shopping cart" in text.lower()
        return text.lower() == "end buying"


    def on_enter_shopping_list(self, event):
        
        reply_token = event.reply_token
        data = ''
        data += "你的購買清單:\n"
        # send_text_message(reply_token, "entering shopping list state")
        for bread in user.breads:
            data += bread
            data += '\n'
        data += '[系統] 請手動輸入 confirm 確認訂單'
        send_text_message(reply_token, data)
        
        self.go_back()
        # send_text_message(reply_token, user.breads)
        #send_text_message(reply_token, breads)

    def is_going_to_confirm(self, event):
        text = event.message.text
        return text.lower() == "confirm"

    def on_enter_confirm(self, event):
        reply_token = event.reply_token
        data = ''
        data += "你的購買清單:\n"
        # send_text_message(reply_token, "entering shopping list state")
        for bread in user.breads:
            data += bread
            data += '\n'
        print("======================")
        print(data)
        print("======================")
        user.breads = []
        send_text_message(reply_token, "謝謝惠顧\n店家已經收到訂單囉!")

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "menu"
        
    def on_enter_menu(self, event):

        reply_token = event.reply_token
        message = graph.menu
        message_to_reply = FlexSendMessage("show the list", message)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, message_to_reply)

    
    def is_going_to_purchase_cake(self, event):
        text = event.message.text

        if("added cake" in text.lower() and "shopping cart" in text.lower()):
            temp = text.split(' ')
            temp_bread = temp[2]

            if(temp_bread == '01'):
                user.add_bread("雙心草莓")
            elif(temp_bread == '02'):
                user.add_bread("雙心葡萄")
            elif(temp_bread == '03'):
                user.add_bread("雙心肉鬆")
            elif(temp_bread == '04'):
                user.add_bread("摩卡咖啡捲")
            elif(temp_bread == '05'):
                user.add_bread("花生瑞士捲")
            elif(temp_bread == '06'):
                user.add_bread("芋頭蛋糕")
            elif(temp_bread == '07'):
                user.add_bread("蜂蜜蛋糕")
            elif(temp_bread == '08'):
                user.add_bread("蜂蜜捲")
            elif(temp_bread == '09'):
                user.add_bread("巧克力米蛋糕")
            elif(temp_bread == '10'):
                user.add_bread("焦糖布丁蛋糕")
            elif(temp_bread == '11'):
                user.add_bread("黃金瓦那")
            elif(temp_bread == '12'):
                user.add_bread("藍莓捲")
        
        return text.lower() == "purchase cake" or ("added cake" in text.lower() and "shopping cart" in text.lower())
       
    def on_enter_purchase_cake(self, event):

        reply_token = event.reply_token
        message = graph.cake
        message_to_reply = FlexSendMessage("show the list", message)
        line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
        line_bot_api.reply_message(reply_token, message_to_reply)

    
        