from PyQt5.QtWidgets import QApplication,QPushButton,QMainWindow
from Interface.MainLeftBar import MainLeftBar
from sys import argv,exit


def main():
    App = QApplication(argv)
    MWin = QMainWindow()
    MWin.setGeometry(100,100,1000,700)

    Window = MainLeftBar(MWin)
    MWin.show()
    Window.show()

    exit(App.exec())

if __name__=="__main__":
    main()