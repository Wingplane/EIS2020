from mcpi.minecraft import Minecraft
import mcpi.block as block
import numpy as np
import cv2
import time

mc = Minecraft.create()
pos = mc.player.getTilePos()
lay = [230,150,20]
a = 32
b = 32

def mypic(i):
    img = cv2.imread("mmypic.jpg")
    GrayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(GrayImage,lay[i],255,cv2.THRESH_BINARY)
    resized_image =~ cv2.resize(thresh1,(32,32))
    return resized_image

for x in range(a):
    for y in range(b):
        mc.setBlock(pos.x+a-x-1, pos.y, pos.z+y, 35)
for i in range(3):
    resized_image = mypic(i)
    for x in range(a):
        for y in range(b):
            if (resized_image[x][y] != 0):
                mc.setBlock(pos.x+a-x-1, pos.y, pos.z+y, 173)


