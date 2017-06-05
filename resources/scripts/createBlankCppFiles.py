#!/usr/bin/env python


# this file is intended to create quickly a void file for a cpp project



import sys
import os
from PyQt4.QtGui import *



class OverWriteDialog(QDialog):
    def __init__(self, fileName):
        QDialog.__init__(self)

        self.setWindowTitle("WARNING: Overwrite file?")
        label =QLabel("WARNING: the file {0} already exist. Overwrite?".format(fileName))
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        layout = QVBoxLayout()
        layout.addWidget( label )
        layout.addWidget( buttonBox )
        self.setLayout(layout)

        buttonBox.accepted.connect( self.accept )
        buttonBox.rejected.connect( self.reject )


    def accept(self):
        self.done(0)

    def reject(self):
        self.done(-1)




def createH(dom, name, qtclass):
    if os.path.exists(name+".h"):
        res = OverWriteDialog(name+".h").exec_()

        if res == 0:
            print "OK overwirte {0}.h".format(name)
        else:
            print "CANCEL {0}.h".format(name)
            return False

    if qtclass:
        qtinclude, QOBJECT, qtslots = "#include <QtGui/QWidget>", "\nQ_OBJECT\n","\nprivate slots:\n"
        herit = " : public QWidget"
    else:
        qtinclude, QOBJECT, qtslots = "", "", ""
        herit = ""


    with open( name+".h" , "w") as f:
        f.write("""#ifndef _{DOM}_{NAME}_H_
#define _{DOM}_{NAME}_H_

#include "DllExport.h"
{qtinclude}

namespace {dom} {{

class {DOM}_EXPORT {name}{herit} {{
    {QOBJECT}
public:
    {name}();
    virtual ~{name}();


private:
    struct Pimpl;
    Pimpl* pimpl;

	//prevent class copy
    {name}(const {name}& other);
{qtslots}
}};

}} // namespace {dom}


#endif
""".format( DOM=dom.upper(), NAME=name.upper(), dom=dom, name=name, qtinclude=qtinclude, QOBJECT=QOBJECT, qtslots=qtslots, herit=herit)
)
    return True


def createCPP(dom, name, qtclass):
    if os.path.exists(name+".cpp"):
        res = OverWriteDialog(name+".cpp").exec_()

        if res == 0:
            print "OK overwirte {0}.cpp".format(name)
        else:
            print "CANCEL {0}.cpp".format(name)
            return False

    if qtclass:
        includeui = '#include "ui_{0}.h"'.format(name)
        UIclass   = "Ui_{0} ui;\n\n".format(name)
        setup     = "void setup() {\n    }"
        init      = "\n    pimpl->ui.setupUi(this);\n    pimpl->setup();"
    else:
        includeui = ""
        UIclass   = ""
        setup     = ""
        init      = ""



    with open( name+".cpp" , "w") as f:
        f.write("""
#include "{name}.h"
{includeui}

using namespace {dom};


struct {name}::Pimpl {{

    {UIclass}
    Pimpl() {{
    }}

	~Pimpl() {{
    }}

    {setup}
}};


{name}::{name}()
    : pimpl( new Pimpl() )
{{ {init}
}}

{name}::~{name}() {{
    delete pimpl;
}}


""".format(dom=dom, name=name, includeui=includeui, UIclass=UIclass, setup=setup, init=init)
)
    return True




class CreateVoidCPPDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.setWindowTitle("Create void files for c++ project")
        buttonBox = QDialogButtonBox(QDialogButtonBox.Close | QDialogButtonBox.Apply)

        formLayout = QFormLayout()
        self.inDomain = QLineEdit()
        self.inClass  = QLineEdit()
        currentDir = QLabel( os.path.dirname(os.path.realpath(__file__)) )
        self.QtChk = QCheckBox("create Qt class")

        formLayout.addRow("domain name:", self.inDomain)
        formLayout.addRow("class name:", self.inClass)

        self.inDomain.setText(str(os.path.split(os.getcwd())[-1]))
        self.inDomain.setMinimumWidth(400)
        layout = QVBoxLayout()
        layout.addWidget( currentDir )
        layout.addSpacing(10)
        layout.addLayout( formLayout )
        layout.addWidget( self.QtChk )
        layout.addWidget( buttonBox )
        self.setLayout(layout)
        buttonBox.button(QDialogButtonBox.Apply).setAutoDefault(True)
        buttonBox.button(QDialogButtonBox.Apply).setDefault(True)

        buttonBox.button(QDialogButtonBox.Apply).clicked.connect( self.apply )
        buttonBox.rejected.connect( self.reject )

        self.inClass.setFocus()


    def apply(self):
        self.createFiles()


    def reject(self):
        self.done(-1)


    def createFiles(self):
        _dom   = str(self.inDomain.text())
        _class = str(self.inClass.text())

        qtclass = self.QtChk.isChecked()

        res = True
        res &= createH(_dom, _class, qtclass)
        res &= createCPP(_dom, _class, qtclass)

        msgBox = QMessageBox()
        if res:
            msgBox.setText("'{0}.h/.cpp' files of {1}::{2} {3}class have been created".format(_class, _dom, _class, "Qt " if qtclass else ""))
        else:
            msgBox.setText("FAILED creating '{0}.h/.cpp' files of {1}::{2} {3}class".format(_class, _dom, _class, "Qt " if qtclass else ""))
        msgBox.exec_()




if __name__ == "__main__":
    app = QApplication(sys.argv)

    diag = CreateVoidCPPDialog()

    diag.exec_()


