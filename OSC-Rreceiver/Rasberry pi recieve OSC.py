#Rasberry pi recieve OSC
#OSC-Receiverから受け取った信号を元にGPIOの入出力を管理します。


# 必要なライブラリをインポート
from pythonosc import dispatcher, osc_server
import RPi.GPIO as GPIO
import datetime
# GPIOピンの設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT)  # 例: GPIOピン19を使用
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT) 
GPIO.setup(26, GPIO.OUT)
# OSCメッセージを受信したときの処理

def handle_osc_message(address,value):
    if address == "/avatar/parameters/OSC1" and value == True:
        GPIO.output(26, GPIO.LOW)
        dt_now = datetime.datetime.now()
        print("リレースイッチ1が ONになりました。アドレス:", address,"  時刻:",dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
    elif address == "/avatar/parameters/OSC1" and value == False:
        GPIO.output(26, GPIO.HIGH)
        dt_now = datetime.datetime.now()
        print("リレースイッチ1がOFFになりました。アドレス:", address,"  時刻:",dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
        
    elif address == "/avatar/parameters/OSC2" and value == True:
        GPIO.output(19, GPIO.LOW)
        dt_now = datetime.datetime.now()
        print("リレースイッチ2が ONになりました。アドレス:", address,"  時刻:",dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
    elif address == "/avatar/parameters/OSC2" and value == False:
        GPIO.output(19, GPIO.HIGH)
        dt_now = datetime.datetime.now()
        print("リレースイッチ2がOFFになりました。アドレス:", address,"  時刻:",dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
        
    elif address == "/avatar/parameters/OSC3" and value == True:
        GPIO.output(13, GPIO.LOW)
        dt_now = datetime.datetime.now()
        print("リレースイッチ3が ONになりました。アドレス:", address,"  時刻:",dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
    elif address == "/avatar/parameters/OSC3" and value == False:
        GPIO.output(13, GPIO.HIGH)
        dt_now = datetime.datetime.now()
        print("リレースイッチ3がOFFになりました。アドレス:", address,"  時刻:",dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
        
    elif address == "/avatar/parameters/OSC4" and value == True:
        GPIO.output(6, GPIO.LOW)
        dt_now = datetime.datetime.now()
        print("リレースイッチ4が ONになりました。アドレス:", address,"  時刻:",dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
    elif address == "/avatar/parameters/OSC4" and value == False:
        GPIO.output(6, GPIO.HIGH)
        dt_now = datetime.datetime.now()
        print("リレースイッチ4がOFFになりました。アドレス:", address,"  時刻:",dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
    else:
        # 他のアドレスの場合は何もしない
        pass    
# OSCサーバーを起動
 #osc通信の設定
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/avatar/parameters/OSC1", handle_osc_message)
dispatcher.map("/avatar/parameters/OSC2", handle_osc_message)
dispatcher.map("/avatar/parameters/OSC3", handle_osc_message)
dispatcher.map("/avatar/parameters/OSC4", handle_osc_message)
 #受信サーバーを動かす
server = osc_server.ThreadingOSCUDPServer(("192.168.1.226",10000), dispatcher)
print("OSCサーバーを起動中...")
server.serve_forever()
