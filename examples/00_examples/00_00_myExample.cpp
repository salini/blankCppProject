
#include "core/myClass.h"

#include <iostream>

using namespace coreLib;


void myPause() {
    std::cout << "Press enter to continue ...";
    std::cin.get();
}


int main(int argc, char* argv[]) {

  myClass c;
  std::cout<<c.methodReturnTrue()<<std::endl;
  myPause();
  return 0;
}

