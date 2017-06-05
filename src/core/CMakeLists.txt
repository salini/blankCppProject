
ADD_VERSION_HEADER_FILE()  # this will add a Version.h file based on the cmake inputs. Should be done once in the source tree folder

FILE(GLOB H_FILES      *.h)
FILE(GLOB CPP_FILES    *.cpp)

SETUP_LIBRARY(coreLib   H_FILES   CPP_FILES)

TARGET_LINK_LIBRARIES(coreLib  # a DllExport.h file will be created automatically
    #libDep1
    #libDep2
)