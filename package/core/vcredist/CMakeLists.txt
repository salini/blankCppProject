

if (WIN32)

    ##### GET VISUAL STUDIO REDISTRIBUABLE
    if (EXISTS ${OPENSIM_BIN_DIR}/vcredist_x86.exe)
        install(FILES ${OPENSIM_BIN_DIR}/vcredist_x86.exe   DESTINATION bin   COMPONENT vcredist_x86)
    else()
        if(NOT EXISTS ${CMAKE_CURRENT_BINARY_DIR}/vcredist_x86.exe)
            message(STATUS "Downloading vcredist_x86.exe once, for packaging purpose")
            file(DOWNLOAD http://download.microsoft.com/download/5/B/C/5BC5DBB3-652D-4DCE-B14A-475AB85EEF6E/vcredist_x86.exe 
                ${CMAKE_CURRENT_BINARY_DIR}/vcredist_x86.exe
                SHOW_PROGRESS
            )
        endif()
        install(FILES ${CMAKE_CURRENT_BINARY_DIR}/vcredist_x86.exe   DESTINATION bin   COMPONENT vcredist_x86)
    endif()
    set(CPACK_COMPONENT_VCREDIST_X86_HIDDEN ON)
    
    
    set(EXTRA_INSTALL_COMMANDS
"ExecWait '\\\"$INSTDIR\\\\bin\\\\vcredist_x86.exe\\\" /q:a'
Delete \\\"$INSTDIR\\\\bin\\\\vcredist_x86.exe\\\"
"
    )

    set(CPACK_NSIS_EXTRA_INSTALL_COMMANDS "${CPACK_NSIS_EXTRA_INSTALL_COMMANDS}
${EXTRA_INSTALL_COMMANDS}
"
    PARENT_SCOPE)

endif()