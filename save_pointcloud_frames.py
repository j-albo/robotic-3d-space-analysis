import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
import numpy as np
import struct
import open3d as o3d
import os

class PointCloudSaver(Node):
    def __init__(self):
        super().__init__('pointcloud_saver')

        self.subscription = self.create_subscription(
            PointCloud2,
            '/voxel_point_cloud',  # Tópico donde se reciben los datos
            self.callback,
            10)

        self.frames = 0
        self.chunk_size = 200  # Guardar cada 200 frames
        self.pcd_data = []
        self.output_dir = "/home/charlie/Desktop/pointcloud_chunks"

        # Crear la carpeta si no existe
        os.makedirs(self.output_dir, exist_ok=True)

        self.get_logger().info("✅ Nodo iniciado: esperando datos de la nube de puntos...")

    def callback(self, msg):
        """Recibe la nube de puntos y guarda cada `X` frames"""
        self.frames += 1
        self.get_logger().info(f'Recibiendo frame {self.frames}...')

        points = []
        for i in range(0, len(msg.data), msg.point_step):
            x, y, z = struct.unpack_from('fff', msg.data, offset=i)
            points.append([x, y, z])

        self.pcd_data.extend(points)  # Acumular puntos

        # Guardar cada 200 frames
        if self.frames % self.chunk_size == 0:
            self.save_partial_pcd()

    def save_partial_pcd(self):
        """Guarda una nube parcial y libera memoria"""
        if not self.pcd_data:
            self.get_logger().warning("⚠️ No hay suficientes datos para guardar.")
            return

        filename = os.path.join(self.output_dir, f"nube_voxel_{self.frames}.pcd")
        cloud = o3d.geometry.PointCloud()
        cloud.points = o3d.utility.Vector3dVector(np.array(self.pcd_data, dtype=np.float32))
        o3d.io.write_point_cloud(filename, cloud)

        self.get_logger().info(f"✅ Guardado fragmento: {filename}")

        self.pcd_data.clear()  # Liberar memoria

def main():
    rclpy.init()
    node = PointCloudSaver()
    try:
        rclpy.spin(node)  # Mantener el nodo corriendo
    except KeyboardInterrupt:
        node.get_logger().info("🛑 Interrupción detectada. Cerrando nodo...")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
