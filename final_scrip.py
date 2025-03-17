import open3d as o3d
import numpy as np
import os

# Define file paths
input_folder = "/home/charlie/Desktop/pointcloud_chunks/"
merged_cloud_path = "/home/charlie/Desktop/workshop2.2/bag/final/merged_cloud.pcd"
filtered_cloud_path = "/home/charlie/Desktop/workshop2.2/bag/final/filtered_cloud.pcd"
clean_ground_path = "/home/charlie/Desktop/workshop2.2/bag/final/clean_ground.pcd"

def visualize_point_cloud(point_cloud, title):
    """
    Displays a point cloud with a fixed isometric SW view.
    """
    vis = o3d.visualization.Visualizer()
    vis.create_window(window_name=title)
    vis.add_geometry(point_cloud)

    # Set camera parameters for a consistent viewpoint
    view_control = vis.get_view_control()
    view_control.set_front([-1, -1, 1])  # Isometric SW direction
    view_control.set_lookat([0, 0, 0])   # Look-at point
    view_control.set_up([0, 0, 1])       # Up direction
    view_control.set_zoom(0.8)           # Adjust zoom

    vis.run()
    vis.destroy_window()

# Step 1: Merge point cloud fragments
print("Merging point cloud fragments...")
files = sorted([f for f in os.listdir(input_folder) if f.endswith(".pcd")])

if not files:
    print("Error: No .pcd files found in the directory.")
    exit()

merged_cloud = o3d.geometry.PointCloud()

for file in files:
    print(f"Adding {file}...")
    cloud = o3d.io.read_point_cloud(os.path.join(input_folder, file))
    merged_cloud += cloud  # Merge point clouds

o3d.io.write_point_cloud(merged_cloud_path, merged_cloud)
print(f"Point cloud successfully merged and saved at: {merged_cloud_path}")

# Visualization
print("Displaying merged point cloud. Close the window to proceed.")
visualize_point_cloud(merged_cloud, "Merged Point Cloud")

# Step 2: Remove the upper 30% of the points
print("Filtering the upper 30% of points...")
points = np.asarray(merged_cloud.points)

# Compute height threshold and remove upper points
height_threshold = np.percentile(points[:, 2], 70)
filtered_points = points[points[:, 2] < height_threshold]

filtered_cloud = o3d.geometry.PointCloud()
filtered_cloud.points = o3d.utility.Vector3dVector(filtered_points)

o3d.io.write_point_cloud(filtered_cloud_path, filtered_cloud)
print(f"Filtered point cloud saved at: {filtered_cloud_path}")

# Visualization
print("Displaying filtered point cloud. Close the window to proceed.")
visualize_point_cloud(filtered_cloud, "Filtered Point Cloud")

# Step 3: Extract ground surface using grid-based filtering
print("Extracting ground surface using grid-based Z-max filtering...")
points = np.asarray(filtered_cloud.points)

# Define grid resolution and create a spatial grid
grid_resolution = 0.1  # Cell size
grid = {}

for p in points:
    key = (round(p[0] / grid_resolution), round(p[1] / grid_resolution))  # Grid cell (X, Y)
    if key in grid:
        if p[2] > grid[key][2]:  # Keep only the highest Z value per grid cell
            grid[key] = p
    else:
        grid[key] = p

# Convert grid data into a new point cloud
ground_points = np.array(list(grid.values()))
clean_ground = o3d.geometry.PointCloud()
clean_ground.points = o3d.utility.Vector3dVector(ground_points)

# Downsample the final ground cloud
clean_ground = clean_ground.voxel_down_sample(voxel_size=0.05)

o3d.io.write_point_cloud(clean_ground_path, clean_ground)
print(f"Final clean ground point cloud saved at: {clean_ground_path}")

# Visualization
print("Displaying final ground point cloud. Close the window to finish.")
visualize_point_cloud(clean_ground, "Final Ground Point Cloud")

print("\nProcessing complete. The point cloud is ready for further analysis.")
