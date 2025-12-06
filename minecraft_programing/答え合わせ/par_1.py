import time
import random
from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

for i in range(5, 0, -1):
    mc.postToChat(str(i))
    time.sleep(1)

while True:
    pos = mc.player.getTilePos()
    px = pos.x + random.randint(-2, 2)
    pz = pos.z + random.randint(-2, 2)
    py = pos.y
    
    mc.setBlock(px, py, pz, 41)
    
    mc.postToChat("5seconds!!")
    for i in range(5, 0, -1):
        mc.postToChat(str(i))
        time.sleep(1)
    
    new_pos = mc.player.getTilePos()
    new_px = new_pos.x
    new_pz = new_pos.z
    new_py = new_pos.y

    if new_px == px and new_pz == pz and new_py == py + 1:
        mc.postToChat("Good!!")
    else:
        mc.postToChat("Game Over")
        break
    
    