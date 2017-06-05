
SET(BUILD_TESTS ON CACHE BOOL "Toggle tests generation")
if (NOT BUILD_TESTS)
    return()
endif()


INCLUDE_DIRECTORIES(
    ${CMAKE_BINARY_DIR}/include
)

FILE(GLOB TEST_HEADER_FILES  *.h )

set(INCLUDE_TEST_HEADER_FILES_STR "")
foreach(H_FILE  ${TEST_HEADER_FILES})
    set(INCLUDE_TEST_HEADER_FILES_STR "${INCLUDE_TEST_HEADER_FILES_STR}#include \"${H_FILE}\"\n")
endforeach()

configure_file(run_tests.cpp.in ${CMAKE_CURRENT_BINARY_DIR}/run_tests.cpp @ONLY)

ADD_EXECUTABLE(run_tests
    ${CMAKE_CURRENT_BINARY_DIR}/run_tests.cpp
    ${TEST_HEADER_FILES}
)

TARGET_LINK_LIBRARIES(run_tests
    coreLib
    # libDep1
    # libDep2
)

add_test(run_all_tests run_tests)

add_custom_target(RUN_ALL_TESTS
    run_tests
    DEPENDS
        run_tests
    SOURCES run_tests.cpp.in  # To have access to the configurable file in the IDE
)



