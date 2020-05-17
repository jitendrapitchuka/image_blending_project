import cv2
import numpy as np
def blendimages1(image1,image2):
    img=cv2.imread(image1)
    img2=cv2.imread(image2)
    
    #print(img.shape)#returns a tuple of no of rows,coloumns,and channels
    width=500
    height=500


    dsize=(width,height)

    img=cv2.resize(img,dsize)
    img2=cv2.resize(img2,dsize)
    



  



    #dst=cv2.add(img,img2)
    dst=cv2.addWeighted(img,.6,img2,.4,0,)
    cv2.imshow('image',dst)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

    cv2.imwrite('/home/jitendra/django/first_project/media/final.png',dst)
    return "/home/jitendra/django/first_project/media/final.png"


