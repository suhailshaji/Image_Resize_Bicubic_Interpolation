import cv2
import numpy as np
import math
import sys
import time
import os
from os import listdir


def u(s, a):
	if (abs(s) >= 0) & (abs(s) <= 1):
		return (a+2)*(abs(s)**3)-(a+3)*(abs(s)**2)+1
	elif (abs(s) > 1) & (abs(s) <= 2):
		return a*(abs(s)**3)-(5*a)*(abs(s)**2)+(8*a)*abs(s)-4*a
	return 0



def padding(img, H, W, C):
	zimg = np.zeros((H+4, W+4, C))
	zimg[2:H+2, 2:W+2, :C] = img
	
	
	zimg[2:H+2, 0:2, :C] = img[:, 0:1, :C]
	zimg[H+2:H+4, 2:W+2, :] = img[H-1:H, :, :]
	zimg[2:H+2, W+2:W+4, :] = img[:, W-1:W, :]
	zimg[0:2, 2:W+2, :C] = img[0:1, :, :C]
	
	
	zimg[0:2, 0:2, :C] = img[0, 0, :C]
	zimg[H+2:H+4, 0:2, :C] = img[H-1, 0, :C]
	zimg[H+2:H+4, W+2:W+4, :C] = img[H-1, W-1, :C]
	zimg[0:2, W+2:W+4, :C] = img[0, W-1, :C]
	return zimg


# Bicubic operation
def bicubic(img, ratio, a):
	
	
	H, W, C = img.shape

	img = padding(img, H, W, C)
	

	dH = math.floor(H*ratio)
	dW = math.floor(W*ratio)


	dst = np.zeros((dH, dW, 3))
	

	h = 1/ratio

	print('Start Bicubic interpolation')
	print('Proccessing image...........')
	print("****************************")
	inc = 0
	
	for c in range(C):
		for j in range(dH):
			for i in range(dW):
				
				
				x, y = i * h + 2, j * h + 2

				x1 = 1 + x - math.floor(x)
				x2 = x - math.floor(x)
				x3 = math.floor(x) + 1 - x
				x4 = math.floor(x) + 2 - x

				y1 = 1 + y - math.floor(y)
				y2 = y - math.floor(y)
				y3 = math.floor(y) + 1 - y
				y4 = math.floor(y) + 2 - y
				
			
				mat_l = np.matrix([[u(x1, a), u(x2, a), u(x3, a), u(x4, a)]])
				mat_m = np.matrix([[img[int(y-y1), int(x-x1), c],
									img[int(y-y2), int(x-x1), c],
									img[int(y+y3), int(x-x1), c],
									img[int(y+y4), int(x-x1), c]],
								[img[int(y-y1), int(x-x2), c],
									img[int(y-y2), int(x-x2), c],
									img[int(y+y3), int(x-x2), c],
									img[int(y+y4), int(x-x2), c]],
								[img[int(y-y1), int(x+x3), c],
									img[int(y-y2), int(x+x3), c],
									img[int(y+y3), int(x+x3), c],
									img[int(y+y4), int(x+x3), c]],
								[img[int(y-y1), int(x+x4), c],
									img[int(y-y2), int(x+x4), c],
									img[int(y+y3), int(x+x4), c],
									img[int(y+y4), int(x+x4), c]]])
				mat_r = np.matrix(
					[[u(y1, a)], [u(y2, a)], [u(y3, a)], [u(y4, a)]])
				
			
				dst[j, i, c] = np.dot(np.dot(mat_l, mat_m), mat_r)


	sys.stderr.write('\n')
	
	
	sys.stderr.flush()
	return dst





DirPath = '/home/suhail/Desktop/Office/Upsampling/images'
Files = os.listdir(DirPath)
count =0
for File in Files:
    imgPath = os.path.join(DirPath, File)
    print(imgPath)

    img =cv2.imread(imgPath)
    
    ratio = 2

    a = -1/2	

    i= img
    dst = bicubic(img, ratio, a)
    print('Completed!')
    cv2.imwrite(f'/home/suhail/Desktop/Office/Upsampling/reseize/resize_{count}.jpeg', dst)
    #bicubicImg = cv2.imread('/home/suhail/Desktop/Office/Upsampling/reseize/resize {count}.png')


    print('Original Image Shape:', img.shape)
    #print('Generated Bicubic Image Shape:', bicubicImg.shape)
    count += 1
	
	
print('**********************************')
print("Total Number Of Images:",len(Files))	
print('**********************************')
print(File)
# img = cv2.imread('0031.JPEG')




	
	
# cv2.imwrite(f'/home/suhail/Desktop/Office/Upsampling/reseize/resize{File}')
	