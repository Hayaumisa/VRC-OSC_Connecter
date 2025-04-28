#試しにOSC信号を受信した場合にサーボモーターを動かすプログラムです。

import RPi.GPIO as GPIO
import time

# ポート番号の定義
Servo_pin = 18

# GPIOの設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(Servo_pin, GPIO.OUT)

# PWMの設定
Servo = GPIO.PWM(Servo_pin, 50)  # サーボモータSG90の周波数は50[Hz]
Servo.start(0)  # Servo.start(デューティ比[0-100%])

# 角度からデューティ比を求める関数
def servo_angle(angle):
    duty = 2.5 + (12.0 - 2.5) * (angle + 90) / 180
    return duty

# ここにOSC信号を受信してサーボモータの角度を制御するコードを追加してください

# 終了処理
Servo.stop()
GPIO.cleanup()