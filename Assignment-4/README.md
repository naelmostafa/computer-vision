# Assignment 4

## Introduction

In this assignment, we worked on COCO dataset, which is a large-scale object detection, segmentation, and captioning dataset.
We were required to to run 3 different models on the COCO dataset and compare the results.

## Model 1: Faster R-CNN resnet50

- Faster R-CNN is a state-of-the-art object detection model. It is based on the R-CNN model, **which is a two-stage object detection model**.
- The first stage of R-CNN is a **selective search algorithm**, which generates a large number of region proposals.
- The second stage is a **classifier that classifies each region proposal into one of the 20 object classes**.
- The classifier is a **linear SVM trained on the features extracted from the region proposals**.
- The R-CNN model is slow because it requires running the selective search algorithm on each image.
- Faster R-CNN addresses this problem by using a deep convolutional network to generate region proposals.
- The deep network is a fully convolutional network that takes an image as input and outputs a set of region proposals.
- The region proposals are then classified by the same linear SVM classifier used in R-CNN.
- The Faster R-CNN model is **faster than R-CNN because it only requires running the deep network once per image**.
- The deep network is trained end-to-end, which means that it is trained jointly with the linear SVM classifier.

## Model 2: FCOS (Fully Convolutional One-Stage Object Detection)

- FCOS is a **one-stage object detection model**.
- It is based on the FPN model, which is a feature pyramid network.
- The FPN model is a deep convolutional network that takes an image as input and outputs a set of feature maps.
- The **feature maps are used to generate region proposals**.
- The region proposals are then classified by a linear SVM classifier.
- The FPN model is trained end-to-end, which means that it is trained jointly with the linear SVM classifier.
- FCOS is **faster than Faster R-CNN because it is a one-stage model**.
- FCOS is also **more accurate than Faster R-CNN because it uses a feature pyramid network to generate region proposals**.

## Model 3: SSD (Single Shot MultiBox Detector)

- SSD is a **one-stage object detection model**.
- It is based on the FPN model, which is a feature pyramid network.
- The FPN model is a deep convolutional network that takes an image as input and outputs a set of feature maps.
- The **feature maps are used to generate region proposals**.
- The region proposals are then classified by a linear SVM classifier.
- The FPN model is trained end-to-end, which means that it is trained jointly with the linear SVM classifier.
- SSD is **faster than Faster R-CNN because it is a one-stage model**.
- SSD is also **more accurate than Faster R-CNN because it uses a feature pyramid network to generate region proposals**.

## Results

- The results of the 3 models are shown in the following table:

| Model | mAP | FPS |
| --- | --- | --- |
| Faster R-CNN resnet50 | 0.xx | x.x |
| FCOS | 0.xxx | x.x |
| SSD | 0.xxx | x.x |

## Conclusion

- In this assignment, we worked on COCO dataset, which is a large-scale object detection, segmentation, and captioning dataset.
- We ran 3 different models on the COCO dataset and compared the results.

## References

- [Faster R-CNN](https://arxiv.org/abs/1506.01497)
- [FCOS](https://arxiv.org/abs/1904.01355)
- [SSD](https://arxiv.org/abs/1512.02325)
