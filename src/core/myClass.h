#ifndef _CORELIB_MYCLASS_H_
#define _CORELIB_MYCLASS_H_

#include "DllExport.h"


namespace coreLib {

class CORELIB_EXPORT myClass {
    
public:
    myClass();
    virtual ~myClass();

    bool methodReturnTrue();
    void methodRuntimeError();


private:
    struct Pimpl;
    Pimpl* pimpl;

	//prevent class copy
    myClass(const myClass& other);

};

} // namespace coreLib


#endif
