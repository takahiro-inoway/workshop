# sample_2.py

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# 自分の位置を取得
pos = mc.player.getPos()

# 位置を表示
print("あなたの位置:")
print(pos.x)
print(pos.y)
print(pos.z)
