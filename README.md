# Robotics Solutions for 3D Space Analysis

## Introduction

Scanning irregular terrains with today’s scanning technology is crucial for obtaining precise environmental models, optimizing planning and execution in architectural projects. Its high-resolution capture capability allows for mapping complex surfaces and detecting floor level variations imperceptible to the human eye, improving efficiency and reducing errors in design and construction.
![ws-01-2048x812](https://github.com/user-attachments/assets/928549f9-5802-425c-a85b-5851af0b366c)

## Why Using a Mobile Robot?

We chose to use the Go2 robot dog because of its exceptional mobility, allowing it to effortlessly adapt to uneven terrain, slopes, and obstacles. Its agility ensures efficient navigation in complex environments, outperforming manual and fixed tools. Additionally, its lightweight and cost-effective design enhances terrain exploration and operational flexibility.

![ws-02-2048x851](https://github.com/user-attachments/assets/6049ecad-95f6-4af6-a596-27e08fbbd38c)

It excels in real-time, high-precision scanning with LiDAR, depth cameras, and IMU sensors. It accurately detects slopes, uneven terrain, and obstacles, generating detailed 3D models. Its autonomy enables large-area mapping with minimal human intervention, optimizing surveying and construction planning.

![ws-03-2048x705](https://github.com/user-attachments/assets/1b05e03d-5c68-4648-8973-d56966eb2e84)

## Sensors Used During the Process

We used LiDAR sensors for precise floor scanning and terrain mapping. The Unitree Go2 (LiDAR 4D) provided real-time 3D mapping of height variations, while the iPhone 16 (LiDAR 3D) enhanced depth sensing.

![ws-04-2048x887](https://github.com/user-attachments/assets/463c7b67-ea4c-4396-98e2-6d2f632b9769)

## Proof of Concept

We selected the entrance of the new IAAC Ávila building as our scanning scenario due to its multiple height variations, slope changes, and obstacles. These challenges provided an ideal test environment to evaluate the Go2 robot’s mobility and LiDAR accuracy in mapping complex terrains.

![ws-05-2048x930](https://github.com/user-attachments/assets/86caa2df-3e37-49b7-a566-c6a2361c102e)

## Concept of Operations

Our workflow begins with robot positioning and software setup, initializing the ROS2 environment and checking sensors. LiDAR, odometry, and camera data are recorded and manually adjusted in real-time. The point cloud is extracted, processed using Open3D & Grasshopper, and analyzed to generate reports and insights.

![ws-06-2048x358](https://github.com/user-attachments/assets/01dbb039-14bd-40c2-a508-05c49e5a4379)

## Robot Preparation

The robot preparation involves positioning it in the designated scanning area, ensuring joints are correctly placed, and verifying a clear path. Additionally, the battery is charged, and joint and motor calibration is performed to prevent interruptions.

![Captura-de-pantalla-2025-03-08-152313](https://github.com/user-attachments/assets/3cc76853-cd0d-4960-8629-616b2c8b8479)
![ezgif com-video-to-gif-converter-3](https://github.com/user-attachments/assets/22bd2152-6f57-4758-8512-708b371947f5)

## Software Setup

The software setup involves cloning the repository, building and running a Docker image, and configuring the ROS2 environment via terminal. It enables robot activation, sensor visualization, teleoperation, map saving, and data recording for accurate terrain mapping.

![ws-08-2048x724](https://github.com/user-attachments/assets/62a9d890-4c18-4f5d-b8fc-94913239e16c)

## Data Recording

We initiate the scanning process, capturing and storing LiDAR point clouds, odometry measurements, and camera data in a ROS2 bag file. This ensures a structured dataset for precise terrain mapping, localization, and post-processing analysis.

![ws-09-2048x224](https://github.com/user-attachments/assets/19b27c9a-f2fc-4e9b-a632-504ea4046ff8)
![ezgif com-optimize-3-1024x576](https://github.com/user-attachments/assets/2eba61a2-1e08-4575-9878-171f03703ae1)

## Scan Running

The scan running process involves manual teleoperation via keyboard, with real-time path adjustments based on obstacles and scanning needs. The user monitors sensor feedback in RQT and RViz, making immediate corrections if unexpected movements occur. Future autonomous scanning will enable predefined path planning, obstacle avoidance, and adaptive resolution scanning without human intervention.

![ws-10-2048x350](https://github.com/user-attachments/assets/01fe866d-e70b-4748-abbf-b5c660ddddc8)
![ezgif com-video-to-gif-converter-2](https://github.com/user-attachments/assets/903f574f-3274-4d0d-9a7a-f7cc743a161c)

## Data Extraction

The data extraction process begins by playing the ROS2 bag file, running a Python script to extract PointCloud2 data, and accumulating up to 200 frames. The data is then converted into Open3D format, buffered, and saved in .pcl chunks for further processing.

![ws-11-2048x660](https://github.com/user-attachments/assets/c51d5d52-a6f4-48d6-a9f3-ba412b5cd639)

## Data Processing

The data processing phase refines the point cloud by merging chunks, cropping noise, and filtering unnecessary data using Open3D. The highest points are retained, and the cloud is gridded at 0.1 XY resolution, keeping the highest Z value per cell and producing a cleaned and structured .pcl file for further analysis.

![ws-12-2048x896](https://github.com/user-attachments/assets/ec77fcc6-aefd-42db-b5a0-fb92d1bda636)

## Lidar Data Comparison

During the process, we conducted a comparison between two scanning systems: the Go2 robot’s LiDAR and Polycam on a mobile phone. By analyzing point cloud data, mapping discrepancies, and resolution differences, we identified variations in scanning accuracy, point organization, and coverage limitations between both methods. The robot’s LiDAR provided higher precision and structured data but heavy pointcloud, while Polycam captured denser details but with less spatial limits accuracy. Both systems have strengths and weaknesses, and combining their data could enhance resolution and mapping reliability for more comprehensive results.

![ws-13-2048x870](https://github.com/user-attachments/assets/2f79566c-a893-41d3-8623-e5022c545ba5)

## Architectural Application

For the architectural application, we processed the point cloud data using Python, Open3D, and Grasshopper, deconstructing the XYZ coordinates to extract height variations. A gradient color mapping was applied to visualize elevation differences, categorizing the terrain into five distinct levels. The processed data was then converted into a mesh representation, allowing for precise floor height segmentation and facilitating architectural refurbishment planning based on existing topography.
![ws-14-2048x882](https://github.com/user-attachments/assets/dd549bbd-f178-4113-ae37-b1b0ce1bdc63)

## Limitations and further steps

The current scanning workflow is effective but limited by manual navigation, time-consuming point cloud processing, and low camera resolution. Future improvements include autonomous navigation, integration with BIM/CAD for large-scale projects, and automatic filtering algorithms to enhance efficiency. These advancements will streamline data processing, improve accuracy, and enable broader applications in construction and architectural refurbishment. A potential application improvement could be calculating the material volume needed to repair or level floors according to renovation requirements.

![ws-15-2048x882](https://github.com/user-attachments/assets/83d5ac2d-1577-4b8a-9873-a139a28fcf34)

