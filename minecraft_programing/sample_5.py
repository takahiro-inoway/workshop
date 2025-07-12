# sample_5.py

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# 自分の位置を取得
pos = mc.player.getPos()

# 縦に積み上げる
for y in range(3):
    mc.setBlock(pos.x + 3, pos.y + y, pos.z, 1)
