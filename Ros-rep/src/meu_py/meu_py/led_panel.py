import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import LedStateArray
from my_robot_interfaces.srv import SetLed

class LEDPanelNode(Node):
    def __init__(self):
        super().__init__("led_panel")
        self.led_states_ = [0, 0, 0]
        
        self.led_states_pub_ = self.create_publisher(LedStateArray, "led_panel_state", 10)
        
        self.led_states_timer = self.create_timer(4.0, self.publish_led_states)
        self.get_logger().info("O LED do painel foi iniciado!")
        self.set_led_service = self.create_service(SetLed, "set_led", self.callback_set_led)

    def publish_led_states(self):
        msg = LedStateArray()
        msg.led_states = self.led_states_
        self.led_states_pub_.publish(msg)
        
    def callback_set_led(self, request: SetLed.Request, response: SetLed.Response):
        led_number = request.led_number
        state = request.state
        
        if led_number >= len(self.led_states_) or led_number < 0:
            response.success = False 
            return response
        
        if state not in [0, 1]:
            response.success = False 
            return response
           
        self.led_states_[led_number] = state
        self.publish_led_states() 
        response.success = True
        return response

def main(args=None):
    rclpy.init(args=args)
    node = LEDPanelNode()
    rclpy.spin(node)
    rclpy.shutdown() 

if __name__ == "__main__":
    main()