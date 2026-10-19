cmake_minimum_required(VERSION 3.15)

project(cuas)

set(CMAKE_CXX_STANDARD 17)

find_package(OpenCV REQUIRED)

add_executable(app comp_vis.cpp)
add_executable(app lidar.cpp)

target_link_libraries(app PRIVATE ${OpenCV_LIBS})