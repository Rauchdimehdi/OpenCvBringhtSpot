import numpy as np
import argparse
import cv2

#Construct the argument parse and parse the arguments

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",help="path to the image")
ap.add_argument("-r","--radius", type=int, help="radius of Gaussian blur; must be odd")
args = vars(ap.parse_args())

#Convert the image to grayscale
image = cv2.imread(args["image"])
origin = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#trying to find the image area with high intensity value
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
cv2.circle(image, maxLoc, 5, (255,0,0), 2)

#showing the result of naive method
cv2.imshow("Naive", image)

#Applying Gaussian blur method
gray = cv2.GaussianBlur(gray, (args["radius"], args["radius"]), 0)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
origin = image.copy()
cv2.circle(image, maxLoc, args["radius"], (255,0,0), 2)

#Display results
cv2.imshow("Robust", image)
cv2.waitKey(0)