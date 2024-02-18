# CMakeList.txt: Job 的 CMake 项目，在此处包括源代码并定义
# 项目特定的逻辑。
#
cmake_minimum_required (VERSION 3.8)

project ("Job" C)

# 将源代码添加到此项目的可执行文件。
add_executable (Job "Job.c")
add_executable (Q2 "Q2.c")

if (CMAKE_VERSION VERSION_GREATER 3.12)
  set_property(TARGET Job PROPERTY C_STANDARD 99)
  set_property(TARGET Q2 PROPERTY C_STANDARD 99)
endif()

# TODO: 如有需要，请添加测试并安装目标。
