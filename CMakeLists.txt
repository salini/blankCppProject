cmake_minimum_required(VERSION 2.8.7)
project (blankCppProject  CXX)

set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake" "${CMAKE_SOURCE_DIR}/cmake/macro")
include(macroUtils)

SET_VERSION(0 1 0)


#####################
#                   #
# FIND DEPENDENCIES #
#                   #
#####################
# example to find dependencies
#set(OpenSceneGraph_MARK_AS_ADVANCED TRUE)
#find_package(OpenSceneGraph  QUIET  COMPONENTS  osgViewer osgDB osgGA osgShadow)

#include_directories(${OPENSCENEGRAPH_INCLUDE_DIR})


##############################
#                            #
# CONFIGURE BUILD PROPERTIES #
#                            #
##############################
# Dynamic vs Static Linking
SET_BUILD_DYNAMIC_OPTION(DYNAMIC_LIB)
SET_CMAKE_RUNTIME_OUTPUT_DIRECTORIES()

## To get access to external configuration / data files during development
add_definitions(-DDEV_RESOURCES_DATA_PATH="${CMAKE_SOURCE_DIR}/resources")  


#################
#               #
# PARSE SOURCES #
#               #
#################
include_directories(src)                    #headers are in the same place as sources
include_directories(externalLibs/include)

add_subdirectory(doc)
add_subdirectory(examples)
add_subdirectory(externalLibs)
add_subdirectory(resources)
add_subdirectory(src)


################################
#                              #
# CONFIGURE TESTING WITH CPACK #
#                              #
################################
enable_testing()  # this call must be here, in the root source directory, before any call of add_test
add_subdirectory(tests)


##################################
#                                #
# CONFIGURE PACKAGING WITH CPACK #
#                                #
##################################
add_subdirectory(package)


##### END of CMakeLists.txt

