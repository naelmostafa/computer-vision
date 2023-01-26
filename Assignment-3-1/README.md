# Computer vision Assignment 3

## Introduction

This assignment is about stereo vision where we will implement and test some simple stereo algorithms.
In each case you will take two images Il and Ir (a left and a right image) and compute the
horizontal disparity (ie., shift) of pixels along each scanline. This is the so-called baseline stereo
case, where the images are taken with a forward-facing camera, and the translation between
cameras is along the horizontal axis. We will calculate the disparity using two ways

## 1. Block Matching

In this part we will implement a simple block matching algorithm. The algorithm is as follows:

1. Get the disparity by matching the left image with the right image.
2. Compute the cost of each pixel by comparing the left image with the right image.
    - SSD (Sum of Squared Differences)
    - SAD (Sum of Absolute Differences)
3. Find the minimum cost pixel in the window and assign the disparity to the pixel.

We will use window size of 1x1 5x5 and 9x9 and compare the results.

## 2. Dynamic Programming

In this part we will implement a dynamic programming algorithm. The algorithm is as follows:

- Get the minimum cost by matching a whole row in the image.
