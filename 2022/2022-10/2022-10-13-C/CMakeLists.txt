cmake_minimum_required(VERSION 3.14)

project(COSC C)

add_executable(Problem1 problem1.c)
add_executable(Problem2 problem2.c)
add_executable(Problem3 problem3.c)

target_link_libraries(Problem3 PUBLIC m)