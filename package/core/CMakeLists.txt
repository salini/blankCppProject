
set(CMAKE_MODULE_PATH "${CMAKE_MODULE_PATH};${CMAKE_SOURCE_DIR}/cmake/cpack")           #To have access to the nsis .nsh and .dll files
set(CMAKE_MODULE_PATH "${CMAKE_MODULE_PATH};${CMAKE_SOURCE_DIR}/cmake/cpack/templates") #To have access to the nsis template

# Set components properties
set(CPACK_COMPONENT_HEADERS_DISPLAY_NAME "Headers")
set(CPACK_COMPONENT_HEADERS_DESCRIPTION  "C/C++ header files for developing with ${PROJECT_NAME}")
set(CPACK_COMPONENT_HEADERS_GROUP        "Development")
set(CPACK_COMPONENT_HEADERS_DEPENDS      libraries)

set(CPACK_COMPONENT_LIBRARIES_DISPLAY_NAME "Libraries")
set(CPACK_COMPONENT_LIBRARIES_DESCRIPTION  "C/C++ static library files for developing with ${PROJECT_NAME}")
set(CPACK_COMPONENT_LIBRARIES_GROUP        "Development")

set(CPACK_COMPONENT_GROUP_DEVELOPMENT_DESCRIPTION "Files needed to develop applications using ${PROJECT_NAME} components")


CONFIGURE_CPACK_APPLICATION_VERSION(${MIRAD_VERSION_MAJOR}   ${MIRAD_VERSION_MINOR}   ${MIRAD_VERSION_PATCH})

CONFIGURE_CPACK_GENERATION("${PROJECT_NAME}"
    "${PROJECT_NAME}"
    "${CMAKE_SOURCE_DIR}/README.txt"
    "${CMAKE_SOURCE_DIR}/LICENSE.txt"
    "${CMAKE_SOURCE_DIR}\\\\\\\\resources\\\\\\\\icons\\\\\\\\projectLogo.png"
    "${CMAKE_SOURCE_DIR}\\\\\\\\resources\\\\\\\\icons\\\\\\\\projectLogo.ico"
)


if (WIN32)

    set(CPACK_NSIS_MODIFY_PATH  ON)
    
    #set(CPACK_NSIS_EXTRA_INSTALL_COMMANDS   "WriteRegStr    HKCU \\\"Environment\\\" \\\"PROJECT_DIR\\\" \\\"$INSTDIR\\\" ")  # TODO: PROJECT_DIR should be replace by the correct value
    #set(CPACK_NSIS_EXTRA_UNINSTALL_COMMANDS "DeleteRegValue HKCU \\\"Environment\\\" \\\"PROJECT_DIR\\\" ")

    file(GLOB CMAKE_FIND_FILES  ${CMAKE_SOURCE_DIR}/cmake/*.cmake )
    install(FILES ${CMAKE_FIND_FILES}   DESTINATION cmake  COMPONENT  cmake_files) # give all cmake files used for dev users

    install(FILES ${CMAKE_SOURCE_DIR}/LICENSE.txt DESTINATION .  COMPONENT license_file)
    install(FILES ${CMAKE_SOURCE_DIR}/README.txt  DESTINATION .)
endif()


add_subdirectory(vcredist)



APPEND_CPACK_NSIS_PROPERTY(UNINSTALLEXE_POSTFIX   "_${PROJECT_NAME}")
INCLUDE(PROJECTCPack) #SHOULD BE LAST CMD FOR PACKAGING
