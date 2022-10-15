cmake_minimum_required(VERSION 3.4...3.18)
project(pybind11_rdp)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

include_directories(BEFORE ${PROJECT_SOURCE_DIR}/headers/include)

set(CMAKE_CXX_STANDARD 14)
set(PYBIND11_CPP_STANDARD -std=c++14)

add_subdirectory(pybind11)
pybind11_add_module(pybind11_rdp src/main.cpp)

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
target_compile_definitions(pybind11_rdp
                           PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
