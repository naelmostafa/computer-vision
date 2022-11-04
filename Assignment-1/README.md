# Computer Vision Assignment 1

## Introduction
it was required to implement
* Image catroonifiy
* Road lane detection using Hough transform

## Cartoonify
The cartoonify uses the following steps to convert an image to cartoon:
* Convert the image to grayscale
* Apply median blur to the grayscale image
* Apply adaptive thresholding to the blurred image
* Apply bilateral filter to the original image
* Combine the bilateral filtered image and the thresholded image


## Road Lane Detection
The road lane detection uses the following steps to detect the lanes:
* Convert the image to grayscale
* Apply median blur to the grayscale image
* Apply canny edge detection to the blurred image
* Apply hough transform to the canny edge detected image
* Draw the detected lines on the original image

