# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 22:59:23 2018

@author: 张泊明
"""
import urllib
import os
import sys
import time
import glob
import cv2
import numpy as np
import matplotlib.pyplot as plt

#https://jaccount.sjtu.edu.cn/jaccount/captcha

def downloadImg(imgUrl):
    global DOMAIN
    filePath = "cap"
    fileName = str(int(round(time.time() * 1000))) + ".jpg"
    fileFullPath = filePath + "\\" + fileName
    try:
        headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }
        req = urllib.request.Request(imgUrl, headers = headers)
        response = urllib.request.urlopen(req, timeout = 10)
        urlImg = response.read()
        try:
            if(not os.path.exists(filePath)):
                os.makedirs(filePath) 
            with open(fileFullPath,'wb') as f:
                f.write(urlImg)
            print("Download Success:" + fileFullPath)
            return fileFullPath
        except:
            print("Unexpected error:" + str(sys.exc_info()))
            return ""
    except:
        print("Unexpected error:" + str(sys.exc_info()))
        return ""
# 自适应阀值二值化
def get_dynamic_binary_image():
  for file in glob.glob("cap\*.png"):
      filename = 'binary_img/' + file.split('.')[0].split("\\")[1] + '.bmp'
      im = cv2.imread(file)
      im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #灰值化
      # 二值化
      #th1 = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
      ret,th1 = cv2.threshold(im,180,255,cv2.THRESH_BINARY)
      cv2.imwrite(filename,th1)

def get_image():
    for file in glob.glob("binary_img\*.jpg"):
        print(file)
        im = cv2.imread(file,0)
        print(im.shape[1],im.shape[0])
        im = 255 - im
        cv2.namedWindow("Image")   
        cv2.imshow("Image", im) 
        cv2.waitKey (0)  
        cv2.destroyAllWindows() 
        break

for _ in range(100):
    downloadImg("https://jaccount.sjtu.edu.cn/jaccount/captcha")
#print(glob.glob("captcha\*.jpg"))
#get_dynamic_binary_image()
#get_dynamic_binary_image()

def my_save():
    a = np.array([[1,2,3],[4,5,6]])
    b = np.arange(0, 1.0, 0.1)
    c = np.sin(b)
    np.save("result.npy", [a,b,c])

#plt.imshow(np.load("img.npy")[0])



