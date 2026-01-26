import rclpy
from rclpy.node import Node

class MycustomNode(Node):
    def init (self):
        super().__init__("nome_node")


def main(args=None):
    rclpy.init(args=args)
    node = MycustomNode()
    rclpy.spin(node)
    rclpy.shutdown() 

if __name__ == "__main__":
    main()           