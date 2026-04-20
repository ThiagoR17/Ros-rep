import math
import rclpy
from functools import partial
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from my_robot_interfaces.msg import Turtle
from my_robot_interfaces.msg import TurtleArray
from my_robot_interfaces.srv import CatchTurtle


class Turtlecontroller(Node):
    def __init__(self):
        
        super().__init__("turtle_controller")
        self.turtle_to_catch: Turtle = None
        self.pose = None 
        self.target_x = 8.0
        self.target_y = 4.0
        
        self.cmd_vel_publisher = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.pose_subscriber = self.create_subscription(Pose, "turtle1/pose", self.callback_pose, 10)
        self.alive_turtle_subscriber = self.create_subscription(TurtleArray, "turtle_viva", self.callback_alive_turtles, 10)
       
        self.control_loop_timer = self.create_timer(0.01, self.control_loop)
        
    def callback_pose(self, pose: Pose):
        self.pose = pose
    
def callback_alive_turtles(self, msg: TurtleArray):
        if len(msg.turtles) > 0:
            if self.catch_closest_turtle_first_:
                closest_turtle = None
                closest_turtle_distance = None

                for turtle in msg.turtles:
                    dist_x = turtle.x - self.pose_.x
                    dist_y = turtle.y - self.pose_.y
                    distance = math.sqrt(dist_x * dist_x + dist_y * dist_y)
                    if closest_turtle == None or distance < closest_turtle_distance:
                        closest_turtle = turtle
                        closest_turtle_distance = distance
                self.turtle_to_catch_ = closest_turtle
            else:
                self.turtle_to_catch_ = msg.turtles[0]
                
def control_loop(self):
    if self.pose is None or self.turtle_to_catch == None:
        return
            
        dist_x = self.turtle_to_catch .x - self.pose.x
        dist_y = self.turtle_to_catch.y - self.pose.y
        distancia = math.sqrt(dist_x**2 + dist_y**2)
        
        cmd = Twist()
        
        if distancia > 0.1: 
            #posição
            cmd.linear.x = 1.5 * distancia
            
            #Orientação
            target_theta = math.atan2(dist_y, dist_x)
            diff = target_theta - self.pose.theta
            
            # normaliza angulo
            if diff > math.pi:
                diff -= 2*math.pi
            elif diff < -math.pi:
                diff += 2*math.pi
                    
            cmd.angular.z = 6.0 * diff
        else:
            cmd.linear.x = 0.0
            cmd.angular.z = 0.0
            self.call_catch_turtle_service(self.turtle_to_catch.name)
            self.turtle_to_catch = None
        self.cmd_vel_publisher.publish(cmd)
        
def call_catch_turtle_service(self, turtle_name):
        while not self.catch_turtle_client_.wait_for_service(1.0):
            self.get_logger().warn("Aguardando o turtle_catch service")
        
        request = CatchTurtle.Request()
        request.name = turtle_name

        future = self.catch_turtle_client_.call_async(request)
        future.add_done_callback(
            partial(self.callback_call_catch_turtle_service, turtle_name=turtle_name))  
        
def callback_call_catch_turtle_service(self, future, turtle_name):
    response: CatchTurtle.Response = future.result()
    if not response.success:
        self.get_logger().error("Turtle " + turtle_name + " Não pode ser removido")
    
def main(args=None):
    rclpy.init(args=args)
    node = Turtlecontroller()
    rclpy.spin(node)
    rclpy.shutdown() 

if __name__ == "__main__":
    main()