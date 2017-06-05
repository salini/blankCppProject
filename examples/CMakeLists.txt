#!/usr/bin cmake

##### TEST IF EXAMPLES SHOULD BE GENERATED
SET(BUILD_EXAMPLES ON CACHE BOOL "Toggle examples generation")
if (NOT BUILD_EXAMPLES)
    return()
endif()

ADD_ALL_SUBDIRECTORIES()

