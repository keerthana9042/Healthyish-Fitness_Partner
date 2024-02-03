# Healthyish-Fitness_Partner
## Introduction
Obesity and overweight conditions are prevalent health concerns worldwide, leading to various medical complications and reduced quality of life. One significant factor contributing to weight gain is an imbalance between calorie intake from food and calorie expenditure through physical activity. Despite the widespread awareness of the importance of exercise in weight management, many individuals struggle to effectively regulate their weight due to challenges in accurately tracking calorie consumption and managing exercise routines.

Youtube Video link:https://youtube.com/watch?v=64qO1IFzbFw&feature=shared

## Objectives
The objective of the project "Weight Reduction through Exercise-based Calorie Consumption Management" is to develop a comprehensive solution that empowers individuals to effectively manage their weight through a combination of calorie-conscious eating habits and tailored exercise routines.The solution for weight reduction through exercise-based calorie consumption management encompasses a comprehensive platform that integrates various tools, features, and resources to support individuals in their journey towards achieving and maintaining a healthy weight. The solution is designed to address the challenges of calorie awareness, exercise efficiency, tracking and monitoring, personalization, education, and accessibility.

##  OneAPI

![image](https://github.com/SaranyaR-btech/Healthyish-Fitness-partner/assets/143238930/6da9704b-1093-4ce3-bd17-de14e2fe3a5b)

The oneAPI AI Analytics Toolkit [1] is implemented using the oneAPI Data Analytics Library (oneDAL), a powerful machine learning library that helps speed up big data analysis. oneDAL is an extension of Intel® Data Analytics Acceleration Library (DAAL) and is a part of oneAPI. oneAPI is a cross-industry, open, standards-based unified programming model that delivers a common developer experience across accelerator architectures.

## oneAPI Optimization

I have used oneAPI which provides enhancement to ML models using oneAPI libraries for low-level compute optimizations. Optimizing machine learning models using Intel's OneAPI involves focusing on key areas to enhance overall performance. First and foremost, leverage optimized libraries such as oneDAL to efficiently execute deep learning operations. Implement the Data Parallel C++ (DPC++),python programming model to tap into parallel processing capabilities across diverse architectures, including CPUs, GPUs, and accelerators. Explore offloading computationally intensive tasks to GPUs using OneAPI's capabilities, leading to significant speed improvements. Prioritize memory optimization strategies, including data layout optimizations, minimizing data movement, and utilizing cache-friendly data structures. Investigate quantization techniques to reduce precision and computational demands. Additionally, consider model pruning to eliminate unnecessary parameters and connections, thus streamlining computations. Use profiling tools to identify and address performance bottlenecks effectively. Finally, stay updated with the latest software and driver releases and engage with Intel's support resources for targeted guidance in optimizing specific areas of your machine learning workflow.

## Proposed System

Gradient boosting is a powerful machine learning technique used for both regression and classification tasks. It belongs to the ensemble learning methods, which combine multiple weak learners to create a strong learner. Gradient boosting builds models in a sequential manner, where each new model corrects the errors made by the previous one.High Predictive Power: Gradient boosting often yields highly accurate predictions, making it one of the most powerful techniques in machine learning.
Handles Nonlinear Relationships: It can capture complex relationships between features and target variables, making it suitable for a wide range of problems.
Robustness to Overfitting: By using shallow decision trees and regularization techniques, gradient boosting is less prone to overfitting compared to other models.
Feature Importance: Gradient boosting provides insights into feature importance, which can help in feature selection and understanding the underlying patterns in the data.

## Presentation video
https://github.com/SaranyaR-btech/Healthyish-Fitness-partner/assets/143238930/a277f37f-cd16-445a-8c3d-84cbfd395698

## Output 
https://github.com/SaranyaR-btech/JDBC-FILES/assets/143238930/a1e476e0-8f61-4f79-8c4e-d1f24afca1bc


## Setup

import pandas as pd

pip install scikit-learn

pip install gradio

from sklearnex import patch_sklearn

patch_sklearn()


## Results and Discussion

## Feature Importance Plot
![WhatsApp Image 2024-01-27 at 8 31 42 PM (1)](https://github.com/SaranyaR-btech/JDBC-FILES/assets/143238930/d4595b57-eb56-4efe-a021-f01e2d34f815)

## Scatter Plot for Selected Features

![WhatsApp Image 2024-01-27 at 8 31 42 PM](https://github.com/SaranyaR-btech/JDBC-FILES/assets/143238930/b698e493-bf72-4043-af77-269d2b459086)

From the above bar chart its evident that Gradient boosting  is much better than other models for this dataset as Gradient boosting  gives the good accuracy .The ONEAPI reduced the overall runtime and GPU usage significantly compared to normal platforms.
