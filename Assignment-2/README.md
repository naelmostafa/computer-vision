# Computer Vision Assignment 2

## Introduction

it was required to implement

* Augmented Reality with planar homographies
* Image mosaic

## Augmented Reality

The augmented reality uses the following steps to overlay a video in another video:

* Get the corresponding points between the image of the object and all the frames of the video
* Get the homography matrix between the image of the object and the frame
* Warp the image of the object to the frame using the homography matrix
* Overlay the warped image on the frame

## Image Mosaic

The image mosaic uses the following steps to create a mosaic:

* Correspondece between the images and homography matrix between them
* warp image planes
* Stitch the warped images
