import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image
import cv2
import numpy as np

class VideoDecoder(Node):
    def __init__(self):
        super().__init__('video_decoder')
        self.get_logger().info('Initializing VideoDecoder Node')
        self.subscription = self.create_subscription(CompressedImage,'image',self.camera_callback,10)
        self.np_arr = CompressedImage()
        self.get_logger().info('Subscription to /image topic created')
        self.publisher = self.create_publisher(Image,'/decompressed_img',10)

    def camera_callback(self, msg):
        #self.get_logger().info('Received a CompressedImage message')
        
        try:
            # Convert the ROS CompressedImage message to a numpy array
            self.np_arr.data = np.asarray(bytearray(msg.data))
            self.get_logger().info(f'Image data converted to numpy array of shape: {self.np_arr.shape}')
            
            # Decode the numpy array into an OpenCV image
            image = cv2.imdecode(self.np_arr.data, cv2.IMREAD_COLOR)
            self.publisher.publish(image)
            if image is not None:
                self.get_logger().info('Image successfully decoded')
                # Display the image
                cv2.imshow('Video Stream', image)
                cv2.waitKey(1)
            else:
                self.get_logger().error('Failed to decode image')
        except Exception as e:
            self.get_logger().error(f'Error in decode_and_display: {e}')

def main(args=None):
    rclpy.init(args=args)
    video_decoder = VideoDecoder()
    rclpy.spin(video_decoder)
    video_decoder.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
