cmake_minimum_required(VERSION 3.12)

project(PikaPika C)

set(C_STANDARD_REQUIRED 11)

file(GLOB PROJSRC "*.h" "*.c")

add_executable(${PROJECT_NAME})

# detect architecture
if (CMAKE_SIZEOF_VOID_P EQUAL 8)
    message(STATUS "Building 64-bit version...")
    set(ARCH "x64/EasyXw.lib")
else()
    message(STATUS "Building 32-bit version...")
    set(ARCH "x86/EasyXa.lib")
endif()

target_sources(${PROJECT_NAME} PRIVATE ${PROJSRC})

set(EASYX_DIR ${CMAKE_SOURCE_DIR}/easyx)

target_include_directories(${PROJECT_NAME} PUBLIC ${EASYX_DIR}/include)

target_link_libraries(${PROJECT_NAME} PUBLIC ${EASYX_DIR}/lib/VC2015/${ARCH})