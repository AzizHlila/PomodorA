from PyQt5.QtWidgets import QApplication,QPushButton,QFrame,QLabel
from PyQt5.QtGui import QPixmap

COLORS = {"color1":"#5800FF","color2":"#1C3879"}
PB_StyleSheet="QPushButton{border-style: outset\
                ;font: 87 12pt 'Segoe UI Black';color:rgb(255, 255, 255);padding-left: 10; text-align: left;;}\
                QPushButton::hover{ background-color:"+COLORS["color2"]+"}\
                "    

MLF_WIDTH = 100
MLF_HIGHT = 3000


class MainLeftBar(QFrame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.UV()
        self.SetHomeButton()
        self.SetStatButton()
    def UV(self):
        self.setGeometry(0,0,MLF_WIDTH,MLF_HIGHT)

        self.setStyleSheet(f"color: white; background-color: {COLORS['color1']};")
        

    def SetHomeButton(self):
        ## HomeButton
        self.BPHomeButton = QPushButton(self)
        self.BPHomeButton.setGeometry(0,50,MLF_WIDTH,40)
        self.BPHomeButton.setText("Home")
        self.BPHomeButton.setFlat(True)
        self.BPHomeButton.setStyleSheet(PB_StyleSheet)
        self.BPHomeButton.show()

    def SetStatButton(self):
        ## StatButton
        self.BPStatButton = QPushButton(self)
        self.BPStatButton.setGeometry(0,100,MLF_WIDTH,40)
        self.BPStatButton.setText("Stat")
        self.BPStatButton.setFlat(True)
        self.BPStatButton.setStyleSheet(PB_StyleSheet)
        self.BPStatButton.show()
