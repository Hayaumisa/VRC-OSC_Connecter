#������OSC�M������M�����ꍇ�ɃT�[�{���[�^�[�𓮂����v���O�����ł��B

import RPi.GPIO as GPIO
import time

# �|�[�g�ԍ��̒�`
Servo_pin = 18

# GPIO�̐ݒ�
GPIO.setmode(GPIO.BCM)
GPIO.setup(Servo_pin, GPIO.OUT)

# PWM�̐ݒ�
Servo = GPIO.PWM(Servo_pin, 50)  # �T�[�{���[�^SG90�̎��g����50[Hz]
Servo.start(0)  # Servo.start(�f���[�e�B��[0-100%])

# �p�x����f���[�e�B������߂�֐�
def servo_angle(angle):
    duty = 2.5 + (12.0 - 2.5) * (angle + 90) / 180
    return duty

# ������OSC�M������M���ăT�[�{���[�^�̊p�x�𐧌䂷��R�[�h��ǉ����Ă�������

# �I������
Servo.stop()
GPIO.cleanup()