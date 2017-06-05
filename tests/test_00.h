
#include "core/myClass.h"

using namespace coreLib;


SCENARIO( "first scenario", "[test_00]" ) {

    GIVEN("an instance of class myClass") {
        myClass c;
        WHEN("use methodReturnTrue") {
            CHECK( c.methodReturnTrue() == true );
        }
        WHEN("use ") {
            REQUIRE_THROWS(c.methodRuntimeError());
        }
    }
}


/*
// just some old test example with catch
// just to get an idea on how to do test scenario


SCENARIO( "check utils", "[miradUtils]" ) {

	GIVEN("The resources paths") {
		CHECK_NOTHROW( getMiradDirPath() );

		CHECK_NOTHROW( getResourceRootPath() );
		CHECK( getResourceRootPath() != "" );

		CHECK_NOTHROW( getResourcePath("dummyPath/", false) );
		CHECK_NOTHROW( getResourcePath("dummyPath/dummyFile.txt", false) );
		CHECK_NOTHROW( getResourcePath("records") );
		CHECK_NOTHROW( getResourcePath("records/") );
		CHECK_NOTHROW( getResourcePath("records/winRec.oni") );

		CHECK_NOTHROW( getIconPath("dummyPath/", false) );
		CHECK_NOTHROW( getIconPath("dummyPath/dummyFile.txt", false) );
		CHECK_NOTHROW( getIconPath("projectLogo.png") );
	}
}

SCENARIO( "check nite component with no tracker", "[miradNite][noTracker]" ) {
	REQUIRE_NOTHROW( NiteContexter::getNbConnectedDevices() );
	THEN("No nite tracker") {
		REQUIRE_NOTHROW( NiteContexter nitec; );
	}
	WHEN("create a nite tacker for replay recorded simulation") {
		NiteContexter nitec;
		THEN("try to load wrong recorded file") {
			REQUIRE_THROWS( nitec.replayRecordedDepthMap( miradUtils::getResourcePath("dummyFolder/dummyFile.oni", false) ) );
		}
#ifndef WIN32
		THEN("try to load wrong recorded file (linux version cannot accept windows version)") {
			REQUIRE_THROWS( nitec.replayRecordedDepthMap( miradUtils::getResourcePath("dummyFolder/winRec.oni") ) );
		}
#endif
		THEN("try to load recorded file") {
#if defined WIN32
			nitec.replayRecordedDepthMap( miradUtils::getResourcePath("records/winRec.oni") );
#else
			nitec.replayRecordedDepthMap( miradUtils::getResourcePath("records/linuxRec.oni") );
#endif
			REQUIRE ( nitec.getTracker().isValid(true, false) );
		}
	}
}
*/
