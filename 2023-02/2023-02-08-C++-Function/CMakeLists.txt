cmake_minimum_required (VERSION 3.8)

project ("calculate")

add_executable (calculate "calculate.cpp" )

if (CMAKE_VERSION VERSION_GREATER 3.12)
  set_property(TARGET calculate PROPERTY CXX_STANDARD 20)
endif()

