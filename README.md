# Introduction to YOLOv10: Real-time Object Detection
## Abstract
Over the past years, YOLOs have emerged as the predominant paradigm in the field of real-time object detection owing to their effective balance between computational cost and detection performance. Researchers have explored the architectural designs, optimization objectives, data augmentation strategies, and others for YOLOs, achieving notable progress. However, the reliance on the non-maximum suppression (NMS) for post-processing hampers the end-to-end deployment of YOLOs and adversely impacts the inference latency. Besides, the design of various components in YOLOs lacks the comprehensive and thorough inspection, resulting in noticeable computational redundancy and limiting the model's capability. It renders the suboptimal efficiency, along with considerable potential for performance improvements. In this work, we aim to further advance the performance-efficiency boundary of YOLOs from both the post-processing and the model architecture. To this end, we first present the consistent dual assignments for NMS-free training of YOLOs, which brings the competitive performance and low inference latency simultaneously. Moreover, we introduce the holistic efficiency-accuracy driven model design strategy for YOLOs. We comprehensively optimize various components of YOLOs from both the efficiency and accuracy perspectives, which greatly reduces the computational overhead and enhances the capability. The outcome of our effort is a new generation of YOLO series for real-time end-to-end object detection, dubbed YOLOv10. Extensive experiments show that YOLOv10 achieves the state-of-the-art performance and efficiency across various model scales. For example, our YOLOv10-S is 1.8$\times$ faster than RT-DETR-R18 under the similar AP on COCO, meanwhile enjoying 2.8$\times$ smaller number of parameters and FLOPs. Compared with YOLOv9-C, YOLOv10-B has 46\% less latency and 25\% fewer parameters for the same performance.

![image](https://github.com/denghv/Vegetables_Fruit_Detection/assets/137135014/a41a0866-c716-40d0-9d4d-e1f41d01aba7)
## 
## Citation
```python
@article{wang2024yolov10,
  title={YOLOv10: Real-Time End-to-End Object Detection},
  author={Wang, Ao and Chen, Hui and Liu, Lihao and Chen, Kai and Lin, Zijia and Han, Jungong and Ding, Guiguang},
  journal={arXiv preprint arXiv:2405.14458},
  year={2024}
}
``` 
# Using YOLOv10 for Real-time Vegetables & Fruit Detection
## Introduction 
This is our Machine Learning's project. At the beginning, we used YOLOv8 with fine-tuning technologies to build our model but the output we gained is not highly accurate. So we decided to use YOLOv10 instead and its performance was much better than we expected.
## About dataset

We built our own dataset by manual-annotation and data-argumention with Roboflow. You are welcomed to use our dataset by following this link: https://universe.roboflow.com/ai-projects-rulo4/vegetables-fruit-detection/dataset/2 

Our dataset has more than 700 images including five classes of vegetables and fruit: banana, apple, watermelon, chili, carrot.
## Installation
Clone project
```
git clone https://github.com/denghv/Vegetables_Fruit_Detection.git
```

```conda``` virtual environment is recommended.

```python
conda create -n yolov10 python=3.9
conda activate yolov10
pip install -r requirements.txt
pip install -e .
```
## Demo
```
--webcam_inference.py
```
Thanks for great implementations!



