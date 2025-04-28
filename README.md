# 無題

このプロジェクトでは、VRChatのExpressionMenuからRasberrypiなどのデバイスにOSC信号を利用して制御する仕組みを実現します。
VRChatOSCはポート9000と9001を利用しており、VRChatからの信号はローカル(127.0.0.1)の9001番に届きます。

PC側では、9001番で受信を行い、別のローカルポートやipへ転送する仕組みがVRC-OSC_RootServer.pyで、それぞれ

`"/avatar/parameters/OSC1","/avatar/parameters/OSC2","/avatar/parameters/OSC3", "/avatar/parameters/OSC4”`

の4つに反応します。

Unityでは、それぞれ

`OSC1`

`OSC2`

`OSC3`

`OSC4`

のパラメーターとそれぞれにトグルスイッチを設定してください。

PC側では常にVRC-OSC_RootServer.pyを動作させる必要があり、起動していなければ、転送することが出来ません。

また、python-OSCを利用しますので、お使いのpythonにpython-OSCを導入する必要があります。コマンドラインで

`pip install python-osc`  と入力してサクッと導入させましょう。

RasberryPi側にはRasberry pi recieve OSC.pyを走らせます。

この時も、Python-OSCを導入する必要があります。

`pip install python-osc`

本プログラムではGPIO6,13,19,26を使用して、リレースイッチを制御します。
