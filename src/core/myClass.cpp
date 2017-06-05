
#include "myClass.h"

#include <stdexcept>


using namespace coreLib;


struct myClass::Pimpl {


    Pimpl() {
    }

	~Pimpl() {
    }


};


myClass::myClass()
    : pimpl( new Pimpl() )
{
}

myClass::~myClass() {
    delete pimpl;
}

bool myClass::methodReturnTrue() {
    return true;
}

void myClass::methodRuntimeError() {
    throw std::runtime_error("this is a runtime exception error");
}
