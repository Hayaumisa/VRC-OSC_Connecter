#VRC-OSC_RootServer
#VRChatから受け取った特定のOSC信号をラズベリーパイ等のデバイスに転送するプログラムです。



# 必要なライブラリをインポート
import socket
import datetime
from pythonosc import udp_client, dispatcher, osc_server

# ローカルホストのIPアドレスとポート
local_ip = "127.0.0.1"
local_port = 9001

# 転送先のIPアドレスとポート
target_ip = "192.168.1.226"
#target_ip = "127.0.0.1"
target_port = 10000

# OSCメッセージを受信したときの処理
def handle_osc_message(address, *args):
    conditions = ["/avatar/parameters/OSC1","/avatar/parameters/OSC2", "/avatar/parameters/OSC3", "/avatar/parameters/OSC4"]
    if address in conditions:
    # メッセージを転送
        client.send_message(address, args)
        dt_now = datetime.datetime.now()
        print("メッセージを送信しました。",dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
        #print(dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
        
    else:
    #でなければすべて無視する
       # print("このメッセージは無視されます。")
        pass
    

# OSCサーバーを設定
dispatcher = dispatcher.Dispatcher()
dispatcher.set_default_handler(handle_osc_message)
server = osc_server.ThreadingOSCUDPServer((local_ip, local_port), dispatcher)

# 転送先のクライアントを設定
client = udp_client.SimpleUDPClient(target_ip, target_port)

# サーバーを起動
print("IR Tracking Server System Ver.2.0")
print(f"OSCサーバーを {local_ip}:{local_port} で起動中...")
server.serve_forever()