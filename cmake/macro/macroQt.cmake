

MACRO(SETUP_QT_LIBRARY   LIB_NAME   LIB_H_FILES   LIB_CPP_FILES   LIB_H_UI_FILES   LIB_H_MOC_FILES)

    QT4_WRAP_UI(GENERATED_LIB_H_UI
        ${${LIB_H_UI_FILES}}
    )
    
    QT4_WRAP_CPP(GENERATED_LIB_H_MOC
        ${${LIB_H_MOC_FILES}}
    )
    
    INCLUDE_DIRECTORIES(${CMAKE_CURRENT_BINARY_DIR}) #To get access to ui_header created by wrap_ui
    
    CONFIGURE_LIBRARY_GENERAL_HEADER(${LIB_NAME}   ${LIB_H_FILES})
    
    ADD_LIBRARY( ${LIB_NAME}
        ${${LIB_H_FILES}}
        ${${LIB_CPP_FILES}}
        ${GENERATED_LIB_H_UI}
        ${GENERATED_LIB_H_MOC}
    )
    
    ADD_STATIC_POSTFIX_IF_NEEDED(${LIB_NAME})
    
    INSTALL_LIBRARY(${LIB_NAME}   ${LIB_H_FILES})
    
ENDMACRO()