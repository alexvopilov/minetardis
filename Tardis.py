import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.connection as connection
from math import *

ip = input()
mc = minecraft.Minecraft.create(address=ip)
start_x = 0
start_y = 0
start_z = 0

#Clear field
for x in range(100):
    for y in range(-30,150):
        for z in range(100):
            mc.setBlock(start_x+x,start_y+y,start_z+z,0)

#Base
for x in range(100):
    for z in range(100):
        mc.setBlock(start_x+x,-20,start_z+z,2)
for x in range(90):
    for z in range(90):
        mc.setBlock(start_x+x+5,-19,start_z+z+5,0)
        mc.setBlock(start_x+x+5,-19,start_z+z+5,1,6)

#Base TARDIS
for x in range(60):
    for z in range(60):
        for y in range(3):
            mc.setBlock(start_x+x+23,-18+y,start_z+z+23,0)
            mc.setBlock(start_x+x+23,-18+y,start_z+z+23,35,11)
            
#Base TARDIS
for x in range(58):
    for z in range(58):
        mc.setBlock(start_x+x+24,-15,start_z+z+24,0)
        mc.setBlock(start_x+x+24,-15,start_z+z+24,35,11)
        
#Base TARDIS
for x in range(56):
    for z in range(56):
        mc.setBlock(start_x+x+25,-14,start_z+z+25,0)
        mc.setBlock(start_x+x+25,-14,start_z+z+25,35,11)

#4 columns
for x in (0,54,55,1):
    for z in (0,55,54,1):
        for y in range(82):
            mc.setBlock(start_x+x+25,-13+y,start_z+z+25,35,11)

for x in (54,55,2,3):
    for z in (54,55,2,3):
        for y in range(82):
            mc.setBlock(start_x+x+24,-13+y,start_z+z+24,35,11)

#insider
for x in range(23,75):
    for z in range(24,76):
        for y in range(82):
            mc.setBlock(start_x+4+x,-13+y,start_z+3+z,22)

#Medium columns
for i in ( (25,25,26,26,54,53,55,52,0,1),(79,79,79,79,54,53,55,52,0,1),(52,53,51,54,25,25,26,26,1,0),(52,53,51,54,79,79,79,79,1,0) ):
    for z in range(2):
        for y in range(82):
            mc.setBlock(start_x+i[4]+z*i[8],-13+y,start_z+i[0]+z*i[9],35,11)
            mc.setBlock(start_x+i[5]+z*i[8],-13+y,start_z+i[1]+z*i[9],35,11)
    for y in range(82):
        mc.setBlock(start_x+i[6],-13+y,start_z+i[2],35,11)
        mc.setBlock(start_x+i[7],-13+y,start_z+i[3],35,11)

#Crops
for j in (78,27):
    for i in (0,27):
        for _y in (0,16+2,16*2+4,16*3+6):
            for _z in range(19):
                for y in range(16):
                    mc.setBlock(start_x+j,-11+y+_y,start_z+30+i+_z,0)
                    if y == 0 or y == 15 or _z == 0 or _z == 18:
                        mc.setBlock(start_x+j,-11+y+_y,start_z+30+i+_z,49)
for j in (78,27):
    for i in (0,27):
        for _y in (0,16+2,16*2+4,16*3+6):
            for _z in range(19):
                for y in range(16):
                    mc.setBlock(start_x+i+31+_z,-11+y+_y,start_z-0+j,0)
                    if y == 0 or y == 15 or _z == 0 or _z == 18:
                        mc.setBlock(start_x+i+31+_z,-11+y+_y,start_z-0+j,49)

#Windows
for j in (78,27):
    for i in (0,27):
        for _z in range(1,19-1):
            for y in range(1,16-1):
                mc.setBlock(start_x+j-1+2*(j%2),-11+y+16*3+6,start_z+30+i+_z,35)
                if _z % 6 == 0 or y == 7:
                    mc.setBlock(start_x+j,-11+y+16*3+6,start_z+30+i+_z,49)
for j in (78,27):
    for i in (0,27):
        for _z in range(1,19-1):
            for y in range(1,16-1):
                mc.setBlock(start_x+i+31+_z,-11+y+16*3+6,start_z-1+j+2*(j%2),35)
                if _z % 6 == 0 or y == 7:
                    mc.setBlock(start_x+i+31+_z,-11+y+16*3+6,start_z+j,49)

#The Door
for _z in range(2,17):
    for y in range(2,14):
        mc.setBlock(start_x+58+_z,-11+y+16*2+4,start_z+28,35)
word_matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,1,0,0,1,1,1,0,0,0,1,0,0,0],
              [0,0,0,1,0,1,1,0,0,1,1,1,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,1,1,0,1,0,1,1,0,0,0,1,0,0,0],
              [0,0,0,1,0,0,0,0,0,0,0,0,1,0,0],
              [0,0,1,0,0,0,1,0,0,0,1,1,0,0,0],
              [0,0,0,1,0,1,1,0,0,1,0,1,0,0,0],
              [0,0,1,0,1,1,1,0,0,1,0,0,0,1,0],
              [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
              ]
for _z in range(2,15):
    for y in range(2,12):
        if word_matrix[y][_z]==1:
            mc.setBlock(start_x+60+_z,-9+y+16*2+4,start_z+28,35,8)
        
for i in range(7):
    mc.setBlock(start_x+50,33-i,start_z+26,35)
    
for i in (50,51):
    for j in (14,15):
        mc.setBlock(start_x+i,33-j,start_z+27,35,8)

#Table Matrix
a = [[0 for i in range(48)] for _ in range(7)]
for i in (2,3,7,10,14,15,16,19,20,22,23,24,31,32,36,39,41):
    a[1][i] = 1
for i in (2,4,6,8,10,15,18,22,31,33,35,37,39,41):
    a[2][i] = 1
for i in (2,3,6,8,10,15,18,22,23,24,31,32,35,37,40):
    a[3][i] = 1
for i in (2,6,8,10,15,18,22,31,33,35,37,39,41):
    a[4][i] = 1
for i in (2,7,10,11,12,14,15,16,19,20,22,23,24,31,32,36,39,41):
    a[5][i] = 1

#The top begin
for _t in (0,53):
    for i in range(52):
        for j in range(11):
            mc.setBlock(start_x+77-i,62+j,start_z+26+_t,35,11)   
            if j>9:
                continue
            mc.setBlock(start_x+78-i,63+j,start_z+27+_t-2*(53-_t)/53,35,11)
            if j>6 or i>47:
                continue
            if a[len(a)-j-1][i*(_t//53) + (len(a[j])-1-i)*((53-_t)//53) ] == 1:
                mc.setBlock(start_x+76-i,64+j,start_z+24+57*(53-_t)/53,35)
            else:
                mc.setBlock(start_x+76-i,64+j,start_z+24+57*(53-_t)/53,35,15)
for _t in (0,53):
    for i in range(52):
        for j in range(11):
            mc.setBlock(start_x+79-_t,62+j,start_z+77-i,35,11)
            if j>9:
                continue
            mc.setBlock(start_x+80-_t-2*(53-_t)/53,63+j,start_z+81-i,35,11)
            if j>6 or i>47:
                continue
            if a[len(a)-j-1][i*(_t//53) + (len(a[j])-1-i)*((53-_t)//53) ] == 1:
                mc.setBlock(start_x+80-55*(53-_t)/53,64+j,start_z+75-i,35)
            else:
                mc.setBlock(start_x+80-55*(53-_t)/53,64+j,start_z+75-i,35,15)

#Roof
for y in range(3):
    for x in range(52):
        for z in range(54):
            mc.setBlock(x+27,73+y,z+26,35,11)
for y in range(4):
    for x in range(1,51):
        for z in range(1,53):
            mc.setBlock(x+27,76+y,z+26,35,11)
for y in range(6):
    for x in range(3+y,51-y):
        for z in range(2+y,53-y-1):
            if x==z or x ==y or z==y or x==z-1 or x ==y-1 or z==y-1 or x==z+1 or x ==y+1 or z==y+1                 or x==53-z or x ==53-y or z==53-y or x==53-z-1 or x ==53-y-1 or z==53-y-1 or x==53-z+1 or x ==53-y+1 or z==53-y+1:
                mc.setBlock(x+26,80+y,z+26,35,11)
            else:
                mc.setBlock(x+26,80+y,z+26,22)

#The lamp
for y in range(4):
    for x in range(8):
        for z in range(8):
            mc.setBlock(49+x,86+y,49+z,35,11)
            
for y in range(9):
    for x in range(4):
        for z in range(4):
            if y ==0 or y>6:
                mc.setBlock(51+x,90+y,51+z,35,11)
            elif x == 0 or z == 0 or x==3 or z==3:
                mc.setBlock(51+x,90+y,51+z,20)
            else:
                mc.setBlock(51+x,90+y,51+z,138)