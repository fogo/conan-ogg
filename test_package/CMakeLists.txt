cmake_minimum_required(VERSION 2.8)
project(ogg-test-package)

set(CMAKE_VERBOSE_MAKEFILE ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${CMAKE_PROJECT_NAME} main.cpp)
target_link_libraries(${CMAKE_PROJECT_NAME} ${CONAN_LIBS})

enable_testing()
add_test(NAME ogg-test
         COMMAND ${CMAKE_PROJECT_NAME}
WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
