#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class Mynode(Node):
    
    def __init__(self):
        super().__init__("meu_teste")
        self.get_logger().info("Oi mundo")
        self.create_timer(1.0, self.timer_call)
        
    def timer_call(self):
        self.get_logger().info("Oi mundo" + str(self.counter_))
        self.counter_ +=1
        
def main(args=None):
    rclpy.init(args=args)
   
    node = Mynode() 
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
       
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()