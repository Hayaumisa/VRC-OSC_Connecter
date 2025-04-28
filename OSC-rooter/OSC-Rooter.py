#OSC-Rooter
#OSC信号を受け取ったとき複数のアドレスとポートに転送するプログラムです。

import socket

def forward_osc_signal():
    # ip,ポート設定等
    local_ip = '127.0.0.1'
    receive_port = 10000
    send_port1 = 10001
    send_port2 = 10000
    send_port3 = 10000
    try:
        # 受信用ソケットを作成
        receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        receive_socket.bind((local_ip, receive_port))
        print(f"Listening for OSC signals on {local_ip}:{receive_port}")

        while True:
            # OSC信号を受信
            data, addr = receive_socket.recvfrom(1024)
            print(f"Received OSC signal from {addr}: \n{data}")

            # 転送先1に送信
            send_socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            send_socket1.sendto(data, (local_ip, send_port1))
            print(f"Forwarded OSC signal to {local_ip}:\n{send_port1}")

            # 転送先2に送信
            send_socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            send_socket2.sendto(data, ('192.168.137.106', send_port2))
            print(f"Forwarded OSC signal to 192.168.137.106:\n{send_port2}")
            
            # 転送先3に送信
            send_socket3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            send_socket3.sendto(data, ('192.168.137.138', send_port3))
            print(f"Forwarded OSC signal to 192.168.137.138:\n{send_port3}")
    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        receive_socket.close()
        send_socket1.close()
        send_socket2.close()
        send_socket3.close()

if __name__ == "__main__":
    forward_osc_signal()

