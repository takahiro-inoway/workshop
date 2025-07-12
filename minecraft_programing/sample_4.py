# sample_4.py

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# 自分の位置を取得
pos = mc.player.getPos()

# 色々なブロックを置く
mc.setBlock(pos.x + 3, pos.y, pos.z, 1)  # 石
mc.setBlock(pos.x + 3, pos.y, pos.z + 1, 2)  # 草ブロック
mc.setBlock(pos.x + 3, pos.y, pos.z + 2, 41)  # 金ブロック
mc.setBlock(pos.x + 3, pos.y, pos.z + 3, 57)  # ダイヤモンドブロック
