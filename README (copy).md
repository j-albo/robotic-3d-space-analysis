# Robotics Solutions for 3D Space Analysis

## 📌 Index
- [Overview](#overview)
- [Why Using a Mobile Robot?](#why-using-a-mobile-robot)
- [Sensors Used](#sensors-used)
- [Proof of Concept](#proof-of-concept)
- [Concept of Operations](#concept-of-operations)
- [Robot Preparation](#robot-preparation)
- [Software Setup](#software-setup)
- [Data Recording](#data-recording)
- [Scan Running](#scan-running)
- [Data Extraction](#data-extraction)
- [Data Processing](#data-processing)
- [Lidar Data Comparison](#lidar-data-comparison)
- [Architectural Application](#architectural-application)
- [Limitations and Further Steps](#limitations-and-further-steps)
- [Getting Started](#getting-started)
- [Authors](#authors)
- [References](#references)

---

## **📌 Overview**
Modern scanning technologies play a critical role in obtaining accurate environmental models.  
This project focuses on **terrain scanning using a mobile robotic system**, optimizing mapping and construction planning with **high-resolution LiDAR sensors**.  
The generated **3D models** help detect floor level variations and enhance architectural workflows.

![ws-01](https://github.com/user-attachments/assets/928549f9-5802-425c-a85b-5851af0b366c)

---

## **📌 Why Using a Mobile Robot?**
The **Unitree Go2 robot dog** was chosen due to its:
- **Exceptional mobility**, adapting to irregular terrain, slopes, and obstacles.
- **Integrated LiDAR and IMU sensors**, providing **real-time**, high-precision mapping.
- **Autonomy and efficiency**, minimizing human intervention.

![ws-02](https://github.com/user-attachments/assets/6049ecad-95f6-4af6-a596-27e08fbbd38c)

---

## **📌 Sensors Used**
We utilized **multiple LiDAR sensors**:
- **Unitree Go2 (LiDAR 4D)** for real-time height mapping.
- **iPhone 16 (LiDAR 3D)** for enhanced depth perception.

![ws-04](https://github.com/user-attachments/assets/463c7b67-ea4c-4396-98e2-6d2f632b9769)

---

## **📌 Proof of Concept**
The entrance of the **IAAC Ávila building** was selected as a test site due to its **height variations, slopes, and obstacles**, providing an ideal scenario to evaluate **robot mobility and LiDAR accuracy**.

![ws-05](https://github.com/user-attachments/assets/86caa2df-3e37-49b7-a566-c6a2361c102e)

---

## **📌 Concept of Operations**
1️⃣ **Position the robot & initialize software**  
2️⃣ **Record sensor data (LiDAR, Odometry, Camera)**  
3️⃣ **Extract and process point cloud data**  
4️⃣ **Generate architectural insights & analysis**

![ws-06](https://github.com/user-attachments/assets/01dbb039-14bd-40c2-a508-05c49e5a4379)

---

## **📌 Robot Preparation**
Before scanning:
- **Check battery and sensor calibration**.
- **Ensure joints & motors are properly aligned**.

![Captura](https://github.com/user-attachments/assets/3cc76853-cd0d-4960-8629-616b2c8b8479)

---

## **📌 Software Setup**
### **System Requirements**
- Ubuntu **LTS 20.04+**
- Python **3.7+**
- Docker & ROS2

### **Installation**

´´´bash
git clone https://github.com/j-albo/robotic-3d-space-analysis.git
cd robotic-3d-space-analysis
source /opt/ros/humble/setup.bash
pip install -r requirements.txt

## **📌 Data Recording**
- **ROS2 Bag Recording** captures **LiDAR, Odometry, and Camera data**.
- Data is stored in **structured `.bag` files** for post-processing.

![ws-09](https://github.com/user-attachments/assets/19b27c9a-f2fc-4e9b-a632-504ea4046ff8)

---

## **📌 Scan Running**
- **Manual teleoperation** controls the robot while scanning.
- The **user monitors sensor feedback** in RQT and RViz.

![ws-10](https://github.com/user-attachments/assets/01fe866d-e70b-4748-abbf-b5c660ddddc8)

---

## **📌 Data Extraction**
1️⃣ **Play ROS2 bag file**  
2️⃣ **Extract PointCloud2 data**  
3️⃣ **Accumulate up to 200 frames**  
4️⃣ **Convert and store `.pcl` chunks**

![ws-11](https://github.com/user-attachments/assets/c51d5d52-a6f4-48d6-a9f3-ba412b5cd639)

---

## **📌 Data Processing**
Using **Open3D**, the point cloud is:
- **Merged** (`merged_cloud.pcd`)
- **Filtered** (Removing high-noise data)
- **Gridded** (0.1 XY resolution, keeping highest Z-value per cell)

![ws-12](https://github.com/user-attachments/assets/ec77fcc6-aefd-42db-b5a0-fb92d1bda636)

---

## **📌 Lidar Data Comparison**
### **Robot LiDAR vs. Mobile LiDAR**
- **Unitree Go2 LiDAR**: High-precision structured data.
- **Polycam (iPhone 16 LiDAR)**: Dense details but less accurate.

![ws-13](https://github.com/user-attachments/assets/2f79566c-a893-41d3-8623-e5022c545ba5)

---

## **📌 Architectural Application**
The **point cloud data** was processed using:
- **Python, Open3D, and Grasshopper**
- **Gradient color mapping** applied for height visualization
- **Conversion to mesh representation** for architectural modeling.

![ws-14](https://github.com/user-attachments/assets/dd549bbd-f178-4113-ae37-b1b0ce1bdc63)

---

## **📌 Limitations and Further Steps**
🔹 **Current Challenges**
- **Manual navigation limits efficiency**
- **Processing time could be optimized**
- **Low camera resolution impacts detail recognition**

🚀 **Future Improvements**
- **Autonomous robot scanning**
- **BIM/CAD integration for large-scale modeling**
- **Advanced filtering algorithms**

![ws-15](https://github.com/user-attachments/assets/83d5ac2d-1577-4b8a-9873-a139a28fcf34)

---

## **📌 Getting Started**
### **Running the Project**
```bash
ros2 bag play /path/to/bagfile
python3 scripts/save_pointcloud_frames.py
python3 scripts/final_scrip.py

## **📌 Authors**
- **[Javi Albo](https://github.com/j-albo)** 
- **[Mau Weber](https://github.com/j-albo)** 
- **[Charlie Larraín](https://github.com/j-albo)**   
- **[Vasili ](https://github.com/j-albo)** 

## **📌 References**
- [Unitree Go2 Robot](https://www.unitree.com/products/go2/)
- [Open3D Documentation](http://www.open3d.org/docs/)
- [ROS2 Bag Documentation](https://docs.ros.org/en/rolling/Tutorials/Recording-And-Playing-Back-Data.html)
- [Python Open3D Library](http://www.open3d.org/docs/release/python_api/open3d.html)

---

## **📌 License**
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## **📌 Acknowledgments**
Special thanks to:
- **[IAAC](https://iaac.net/)** for providing the testing environment.
- **The Open Source Robotics Foundation (OSRF)** for maintaining ROS2.
- **The Open3D community** for continuous improvements in 3D point cloud processing.

---

### 🚀 **If you find this project useful, feel free to ⭐ star the repository and contribute!**
