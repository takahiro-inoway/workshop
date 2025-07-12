# sample_1.py

# マインクラフトに接続するプログラム
from mcpi.minecraft import Minecraft

# マインクラフトに接続
mc = Minecraft.create()

# チャットメッセージを送信
mc.postToChat("こんにちは、マインクラフト!")
