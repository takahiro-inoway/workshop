# sample_7.py

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# 自分の位置を取得
pos = mc.player.getPos()

# テレポート
mc.player.setPos(pos.x - 3, pos.y, pos.z)
