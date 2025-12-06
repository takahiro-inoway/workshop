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
d = 3

b = 49
w = 35

dotlist = [
  [0, 0, b, b, b, 0, b, b, b, b, b, b, 0, b, b, 0],
  [0, b, y, y, y, b, y, y, y, y, y, y, b, y, y, b],
  [b, y, y, y, y, y, y, y, y, y, y, y, y, b, y, b],
  [b, y, y, y, y, y, y, y, y, y, y, y, y, y, y, b],
  [b, y, y, y, y, y, y, y, y, w, y, w, y, y, y, b],
  [0, b, y, y, y, y, y, y, y, b, y, b, y, y, y, b],
  [0, b, b, y, y, y, y, y, y, b, y, b, y, y, b, 0],
  [0, b, y, y, y, y, w, w, y, y, y, y, y, w, b, 0],
  [0, b, y, y, y, y, y, y, y, y, y, y, y, y, b, 0],
  [0, 0, b, y, y, y, y, y, y, y, b, y, y, y, b, 0],
  [0, 0, b, y, y, y, y, y, y, y, y, y, y, b, 0, 0],
  [0, b, w, b, y, y, y, y, y, y, y, y, y, b, 0, 0],
  [0, b, w, w, b, b, y, y, y, y, y, y, b, 0, 0, 0],
  [0, b, w, w, w, b, b, b, b, b, b, b, 0, 0, 0, 0],
  [0, b, w, w, b, 0, b, w, w, b, 0, 0, 0, 0, 0, 0],
  [0, 0, b, b, 0, 0, 0, b, b, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

dot_tate = len(dotlist)

dotlist2 = [
  [0, 0, 0, 0, 0, 0, b, b, b, b, b, b, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, b, y, y, y, y, y, y, b, 0, 0, 0],
  [0, 0, 0, 0, b, y, y, y, y, y, y, y, y, b, 0, 0],
  [0, 0, 0, b, y, y, y, y, y, y, y, y, y, y, b, 0],
  [0, 0, b, y, y, y, y, y, y, w, y, w, y, y, b, 0],
  [0, 0, b, y, y, y, y, y, y, b, y, b, y, y, b, 0],
  [0, 0, b, y, y, y, y, y, y, b, y, b, y, y, b, 0],
  [0, b, y, y, y, y, w, w, y, y, y, y, y, w, b, 0],
  [b, y, y, y, y, y, y, y, y, y, y, y, y, y, b, 0],
  [b, y, y, y, y, y, y, y, y, y, b, y, y, y, b, b],
  [b, y, y, y, y, y, y, y, y, y, y, y, y, b, y, b],
  [0, b, y, y, y, b, y, y, y, y, y, y, y, b, y, b],
  [0, b, b, b, b, b, y, y, y, y, y, y, b, b, b, 0],
  [0, b, w, w, w, b, b, b, b, b, b, b, 0, 0, 0, 0],
  [0, b, w, w, b, 0, b, w, w, b, 0, 0, 0, 0, 0, 0],
  [0, 0, b, b, 0, 0, 0, b, b, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
            
            mc.setBlock(art_x, art_y + count, art_z, row[col_i])
    
    time.sleep(0.4)    
    count = count + 1

    for row_i in range(dot_tate2):
        
        row = dotlist2[row_i]

        for col_i in range(len(row)):
            
            art_x = px + col_i
            art_y = py + (dot_tate - row_i)
            art_z = pz + 10
            
            mc.setBlock(art_x, art_y + count, art_z, row[col_i])

    time.sleep(0.4)
    count = count + 1

mc.postToChat("The Block Art")

