cmake_minimum_required(VERSION 3.8)
project(tr_robot_bringup)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# 1. find dependencies
find_package(ament_cmake REQUIRED)

# 2. Install the launch directory
install(DIRECTORY
  launch config
  DESTINATION share/${PROJECT_NAME}
)

# 3. Export the package
ament_package()