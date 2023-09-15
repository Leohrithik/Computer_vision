import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd
import glob2
import os,fnmatch
from pathlib import Path
from mtcnn.mtcnn import MTCNN
from skimage import measure

def extract_multiple_videos(intput_filenames, image_path_infile):
    """Extract video files into sequence of images."""
i = 1  # Counter of first video
cap=cv2.VideoCapture('C:\Computer_vision\Deepfake\crop1.mp4')
if (cap.isOpened()==False):
        print("Error opening file")
while True:
        ret,frame=cap.read()
            
        if ret:
            cv2.imwrite(os.path.join(image_path_infile,str(i)+'.jpg'),frame)
            # cv2.imshow('frame', frame)
            i+=1
        else:
            break
cv2.waitKey(3)
cap.release()

fake_video_name = "C:/Computer_vision/Deepfake/crop2.mp4"
fake_image_path_for_frame = "C:/Computer_vision/Deepfake"

real_video_name = "C:/Computer_vision/Deepfake/crop1.mp4"
real_image_path_for_frame = "C:/Computer_vision/Deepfake"

# Extract frames from video files
extract_multiple_videos([fake_video_name], fake_image_path_for_frame)
extract_multiple_videos([real_video_name], real_image_path_for_frame)

def mse(imageA,imageB):
    err=np.sum((imageA.astype("float")-imageB.astype("float"))**2)
    err/=float(imageA.shape[0]*imageA.shape[1])
    return err

def compare_images(imageA,imageB,title):
    m=mse(imageA,imageB)
    s=measure.compare_ssim(imageA,imageB)
    fig=plt.figure(title)
    plt.suptitle("MSE:%.2f,SSIM:%.2f"%(m,s))
    ax=fig.add_subplot(1,2,1)
    plt.imshow(imageA,cmap=plt.cm.gray)
    plt.axis("off")
    ax=fig.add_subplot(1,2,2)
    plt.imshow(imageB,cmap=plt.cm.gray)
    plt.axis("off")
    plt.show()

mse()
compare_images()
extract_multiple_videos()

# extract_multiple_videos(crop2.mp4,"C:\Computer_vision\Deepfake\crop2.mp4")
# extract_multiple_videos(crop1.mp4,"C:\Computer_vision\Deepfake\crop1.mp4")

# Example usage: Compare two images
# imageA = cv2.imread("path/to/imageA.jpg", cv2.IMREAD_GRAYSCALE)
# imageB = cv2.imread("path/to/imageB.jpg", cv2.IMREAD_GRAYSCALE)
# compare_images(imageA, imageB, "Image Comparison")