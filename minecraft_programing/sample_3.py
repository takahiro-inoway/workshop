# sample_3.py

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# 自分の位置を取得
pos = mc.player.getPos()

# 自分の目の前にブロックを置く
mc.setBlock(pos.x + 3, pos.y, pos.z, 1)