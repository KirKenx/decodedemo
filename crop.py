import cv2
import numpy as np
import os
filenames=os.listdir()
def cropim(s,name):
    image= cv2.imread(s,cv2.IMREAD_COLOR)
    (h, w, d) = image.shape
    image_crop = image[0:200, 0:158, :] #h điền thông số ở dòng này MxN pixel
    crop_name = name+"_crop"+".jpg"
    cv2.imwrite(crop_name, image_crop)
    print("width={}, height={}, depth={}".format(w, h, d))
    roi = image[0:200, 0:159]
    cv2.imshow("ROI", roi)
    cv2.waitKey(0)

for filename in filenames:
    arr=filename.split(".",1)
    # print(filename)
    if( arr[1]=="jpg" ):
        cropim(filename,arr[0])

