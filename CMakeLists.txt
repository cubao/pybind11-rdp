# Require CMake 3.15+ (matching scikit-build-core) Use new versions of all
# policies up to CMake 3.27
cmake_minimum_required(VERSION 3.15...3.27)

# set(CMAKE_BUILD_TYPE "Debug")
if(NOT CMAKE_BUILD_TYPE OR CMAKE_BUILD_TYPE STREQUAL "")
  set(CMAKE_BUILD_TYPE
      "Release"
      CACHE STRING "" FORCE)
  message(STATUS "Set build type to default: ${CMAKE_BUILD_TYPE}")
else()
  message(STATUS "Your build type: ${CMAKE_BUILD_TYPE}")
endif()
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O0 -ggdb")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O0 -ggdb")
elseif(CMAKE_BUILD_TYPE STREQUAL "Release")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O3")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3")
endif()
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-pragma-once-outside-header")
endif()
add_definitions(-D_CRT_SECURE_NO_WARNINGS)
add_definitions(-DPROJECT_SOURCE_DIR="${PROJECT_SOURCE_DIR}")
add_definitions(-DPROJECT_BINARY_DIR="${PROJECT_BINARY_DIR}")

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

# Scikit-build-core sets these values for you, or you can just hard-code the
# name and version.
project(
  ${SKBUILD_PROJECT_NAME}
  VERSION ${SKBUILD_PROJECT_VERSION}
  LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14)
# Find the module development requirements (requires FindPython from 3.17 or
# scikit-build-core's built-in backport)
find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)
find_package(pybind11 CONFIG REQUIRED)
include_directories(SYSTEM ${PROJECT_SOURCE_DIR}/headers/include)

# Add a library using FindPython's tooling (pybind11 also provides a helper like
# this)
python_add_library(_core MODULE src/main.cpp WITH_SOABI)
target_link_libraries(_core PRIVATE pybind11::headers)

# This is passing in the version as a define just as an example
target_compile_definitions(_core PRIVATE VERSION_INFO=${PROJECT_VERSION})

# The install directory is the output (wheel) directory
install(TARGETS _core DESTINATION pybind11_rdp)
