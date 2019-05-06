from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
from PyQt5.Qt import *
import os, sys

if __name__ == "__main__":
    import sys

    app = QGuiApplication(sys.argv)
    #create an engine to be able to use qml in the application
    engine = QQmlApplicationEngine()
    engine.load(QUrl.fromLocalFile("main.qml"))


    sys.exit(app.exec_())
        

        
