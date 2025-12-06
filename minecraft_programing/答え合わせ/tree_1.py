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
g = 133
d = 161
r = 41

b = 49
w = 35

dotlist = [
  [0, 0, 0, 0, 0, 0, 0, 0, r, r, 0, 0, 0, 0, 0, 0, 0, r],
  [0, 0, 0, 0, 0, 0, 0, r, r, r, r, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, r, 0, 0, 0, 0, 0, g, g, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, g, g, g, g, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, g, g, g, g, 0, 0, 0, r, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, g, g, d, d, d, g, 0, 0, 0, 0, 0, 0],
  [r, 0, 0, 0, 0, 0, g, d, d, g, g, g, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, d, g, g, g, g, g, g, d, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, g, g, d, d, d, g, g, d, g, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, d, g, g, g, g, g, g, g, g, d, 0, 0, 0, 0],
  [0, 0, 0, 0, d, d, g, g, g, g, g, g, d, d, 0, 0, 0, r],
  [0, 0, 0, g, d, d, d, g, g, g, g, g, g, g, g, 0, 0, 0],
  [0, 0, 0, g, g, d, d, d, d, d, g, g, g, g, g, 0, 0, 0],
  [0, 0, d, g, g, g, g, g, g, g, g, g, d, d, d, g, 0, 0],
  [0, 0, d, d, d, d, 0, d, d, d, 0, 0, d, 0, d, d, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, r, r, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, r, r, 0, 0, 0, 0, 0, 0, 0, 0],
  [g, 0, g, 0, 0, 0, r, r, r, r, r, r, 0, 0, 0, g, 0, g]
]

dot_tate = len(dotlist)

dotlist2 = [
  [0, r, 0, 0, 0, 0, 0, 0, r, r, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, r, r, r, r, r, r, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, r, r, 0, 0, 0, 0, 0, r, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, g, g, g, g, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, r, 0, 0, g, g, g, g, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, g, g, r, d, d, g, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, g, g, d, g, g, g, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, d, r, g, g, g, g, g, d, 0, 0, r, 0, 0],
  [0, 0, 0, 0, g, g, d, d, d, g, g, d, g, 0, 0, 0, 0, 0],
  [r, 0, 0, 0, d, g, g, g, g, g, g, g, d, r, 0, 0, 0, 0],
  [0, 0, 0, 0, d, g, g, g, g, r, g, d, d, d, 0, 0, 0, 0],
  [0, 0, 0, r, d, d, g, g, g, g, g, d, d, g, g, 0, 0, 0],
  [0, 0, 0, g, g, d, d, d, d, d, g, g, g, g, g, 0, 0, 0],
  [0, 0, d, d, g, r, g, g, g, g, g, g, g, g, d, g, 0, 0],
  [0, 0, d, d, d, d, 0, g, d, d, 0, 0, d, 0, d, d, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, r, r, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, r, r, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, g, 0, g, 0, 0, r, r, r, r, r, r, 0, 0, g, 0, g, 0]
]

dot_tate2 = len(dotlist2)

#count
count = 0

while True:
    for row_i in range(dot_tate):
        
        row = dotlist[row_i]

        for col_i in range(len(row)):
            
            art_x = px + col_i
            art_y = py + (dot_tate - row_i)
            art_z = pz + 10
            
            mc.setBlock(art_x, art_y, art_z, row[col_i])
    
    time.sleep(0.4)    
    count = count + 1

    for row_i in range(dot_tate2):
        
        row = dotlist2[row_i]

        for col_i in range(len(row)):
            
            art_x = px + col_i
            art_y = py + (dot_tate - row_i)
            art_z = pz + 10
            
            mc.setBlock(art_x, art_y, art_z, row[col_i])

    time.sleep(0.4)
    count = count + 1

mc.postToChat("The Block Art")

