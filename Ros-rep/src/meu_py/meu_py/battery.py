import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLed

class BatteryNode(Node):
    def __init__(self): 
        super().__init__("battery")
        self.battery_state = "carregada"
        self.last_time_battery_state_changed_ = self.get_current_time_seconds()
        self.battery_timer = self.create_timer(0.1, self.check_battery_state)
        self.set_led_client_ = self.create_client(SetLed, "set_led")
        self.get_logger().info("A bateria do node foi iniciada!")
        self.get_logger().info("Nó da bateria iniciado.")
        
    def get_current_time_seconds(self):
       
        t = self.get_clock().now().seconds_nanoseconds()
        return t[0] + t[1] / 1e9
        
    def check_battery_state(self):
        timer_now = self.get_current_time_seconds()
        if self.battery_state == "carregada":
            if timer_now - self.last_time_battery_state_changed_ > 4.0:
                self.battery_state = "descarregada"
                self.get_logger().info("A bateria está fraca! carregando...")
                self.call_set_led(2, 1)
                self.last_time_battery_state_changed_ = timer_now
        elif self.battery_state == "descarregada":
            if timer_now - self.last_time_battery_state_changed_ > 6.0:
                self.battery_state = "carregada"
                self.get_logger().info("Bateria carregada")
                self.call_set_led(2, 0)
                self.last_time_battery_state_changed_ = timer_now
    
    def call_set_led(self, led_number, state):
        while not self.set_led_client_.wait_for_service(1.0):
            self.get_logger().warn("Esperando pelo set_led service")
        request = SetLed.Request()
        request.led_number = led_number
        request.state = state
        
        future = self.set_led_client_.call_async(request)
        future.add_done_callback(self.callback_call_set)
        
    def callback_call_set(self, future):
        response: SetLed.Response = future.result()
        if response.success:
            self.get_logger().info("LED ligado")
        else:
            self.get_logger().info("LED não ligado")    
            
         
def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode()
    rclpy.spin(node)
    rclpy.shutdown() 

if __name__ == "__main__":
    main()