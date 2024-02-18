cmake_minimum_required (VERSION 3.8)

project ("MaxProduct")

add_executable (MaxProduct "main.cpp" "test.h" "array.h")

if (CMAKE_VERSION VERSION_GREATER 3.12)
  set_property(TARGET MaxProduct PROPERTY CXX_STANDARD 20)
endif()

