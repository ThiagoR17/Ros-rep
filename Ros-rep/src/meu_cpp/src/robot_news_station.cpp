#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class RobotNewsStation : public rclcpp::Node // Convenção: PascalCase para classes
{
public:
    RobotNewsStation() : Node("robot_news_station")
    {
        // Inicializa o publicador
        publisher_ = this->create_publisher<example_interfaces::msg::String>("robot_news", 10);

        // Cria um timer para publicar a cada 500ms
        timer_ = this->create_wall_timer(
            std::chrono::milliseconds(500),
            std::bind(&RobotNewsStation::publishNews, this));
            
        RCLCPP_INFO(this->get_logger(), "Robot News Station foi iniciado.");
    }

private:
    void publishNews()
    {
        auto msg = example_interfaces::msg::String();
        msg.data = "Ola, esta e uma noticia do robo!";
        publisher_->publish(msg);
    }

    rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_; 
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<RobotNewsStation>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}