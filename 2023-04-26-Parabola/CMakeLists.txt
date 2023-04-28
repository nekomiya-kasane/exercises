cmake_minimum_required(VERSION 3.12)

project(PikaPika CXX)

set(CXX_STANDARD_REQUIRED 17)

# collect sources
file(GLOB PROJSRC "*.h" "*.cpp")

add_executable(${PROJECT_NAME})
set_target_properties(${PROJECT_NAME} PROPERTIES LINKER_LANGUAGE CXX)


target_sources(${PROJECT_NAME} PRIVATE ${PROJSRC})

set(EASYX_DIR ${CMAKE_SOURCE_DIR}/easyx)
set(EASYX_LIB ${EASYX_DIR}/lib/VC2015/x64/EasyXw.lib)

# link easyx
target_include_directories(${PROJECT_NAME} PUBLIC ${EASYX_DIR}/include)

#target_link_libraries(${PROJECT_NAME} PUBLIC ${EASYX_LIB})