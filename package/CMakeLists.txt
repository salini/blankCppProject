
SET(BUILD_PACKAGE OFF CACHE BOOL "Toggle packaging of the whole project, with libraries, headers,etc...")
if (NOT BUILD_PACKAGE) 
    return()
endif()

##########################################################################
add_subdirectory(core)

