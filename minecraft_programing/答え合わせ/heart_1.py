import time
from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

for i in range(7, 0, -1):
    mc.postToChat(str(i))
    time.sleep(1)

pos = mc.player.getTilePos()

px = pos.x
py = pos.y
pz = pos.z

y = 41

dotlist = [
    [0, y, y, 0, y, y, 0],
    [y, y, y, y, y, y, y],
    [y, y, y, y, y, y, y],
    [0, y, y, y, y, y, 0],
    [0, 0, y, y, y, 0, 0],
    [0, 0, 0, y, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

dot_tate = len(dotlist)

for row_i in range(dot_tate):
    
    row = dotlist[row_i]

    for col_i in range(len(row)):
        
        art_x = px + col_i
        art_y = py + (dot_tate - row_i)
        art_z = pz + 10
        
        mc.setBlock(art_x, art_y, art_z, row[col_i])
        time.sleep(0.05)


mc.postToChat("The Block Art")

