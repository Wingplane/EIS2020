from mcpi.minecraft import Minecraft
import mcpi.block as block
import numpy as np
import cv2
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()
a=200
b=200

img=cv2.imread("showmypic.jpg")
GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh1=cv2.threshold(GrayImage,180,255,cv2.THRESH_BINARY)
resized_image=~cv2.resize(thresh1,(b,a))


for x in range(a):
    for y in range(b):
        mc.setBlock(pos.x+a-x-1,pos.y,pos.z+y,173)
        print("finish")

for x in range(a):
    for y in range(b):
        if resized_image[x][y]==0:
            mc.setBlock(pos.x+a-x-1,pos.y,pos.z+y,35)
            print("end")
