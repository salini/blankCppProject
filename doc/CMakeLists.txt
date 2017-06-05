
##### Find Doxygen #####
find_package(Doxygen QUIET)
if(NOT DOXYGEN_FOUND)
    message(STATUS "Cannot find optional package Doxygen")
endif()


if(DOXYGEN_FOUND)
    SET(BUILD_DOCUMENTATION OFF CACHE BOOL "Toggle documentation generation")
endif()


if(DOXYGEN_FOUND AND BUILD_DOCUMENTATION)

    if (WIN32)
        set(DOC_BUILD_PROJ_NAME "BUILD_DOCUMENTATION")
    else()
        set(DOC_BUILD_PROJ_NAME "build_doc")
    endif()
    
    configure_file(Doxyfile.in ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile @ONLY)
    add_custom_target(${DOC_BUILD_PROJ_NAME}
        ALL
        ${DOXYGEN_EXECUTABLE} ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
        COMMENT "Generating API documentation with Doxygen"
        VERBATIM
    )

    install(
        DIRECTORY   ${CMAKE_CURRENT_BINARY_DIR}/html
        DESTINATION documentation
        COMPONENT   documentation
    )
    
    set(CPACK_COMPONENT_DOCUMENTATION_DISPLAY_NAME "Documentation" PARENT_SCOPE)
    set(CPACK_COMPONENT_DOCUMENTATION_DESCRIPTION "API documentation of ${PROJECT_NAME}" PARENT_SCOPE)

endif()

