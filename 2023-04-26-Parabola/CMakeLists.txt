cmake_minimum_required(VERSION 3.12)

project(PikaPika C)

set(C_STANDARD_REQUIRED 11)

file(GLOB PROJSRC "*.h" "*.c")

add_executable(${PROJECT_NAME})

target_sources(${PROJECT_NAME} PRIVATE ${PROJSRC})

