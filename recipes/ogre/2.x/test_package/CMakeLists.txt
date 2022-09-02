cmake_minimum_required(VERSION 3.8)
project(test_package)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(KEEP_RPATHS)


find_package(OGRE ${OGRE_VERSION} COMPONENTS OgreMain REQUIRED)
add_executable(test_package test_package.cpp)
target_link_libraries(test_package OGRE::OgreMain)

set_target_properties(test_package PROPERTIES
CXX_STANDARD 11
CXX_STANDARD_REQUIRED ON
CXX_EXTENSIONS ON)
