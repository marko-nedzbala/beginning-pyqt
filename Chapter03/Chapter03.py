import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit)
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        # self.setGeometry(100, 100, 250, 150)
        self.setMaximumSize(310, 130)
        self.setWindowTitle('QPushButton Example')
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.times_pressed = 0
        
        self.name_label = QLabel('Dont push the button', self)
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.button = QPushButton('Push me', self)
        self.button.move(80, 70)
        self.button.clicked.connect(self.buttonClicked)

    def setUpMainWindow(self):
        QLabel('Please enter your name below.', self).move(70, 10)
        
        name_label = QLabel('Name:', self)
        name_label.move(20, 50)

        self.name_edit = QLineEdit(self)
        self.name_edit.resize(210, 20)
        self.name_edit.move(70, 50)

        clear_button = QPushButton('Clear', self)
        clear_button.move(140, 90)
        clear_button.clicked.connect(self.clearText)

        accept_button = QPushButton('Ok', self)
        accept_button.move(210, 90)
        accept_button.clicked.connect(self.acceptText)


    def buttonClicked(self):
        self.times_pressed += 1
        if self.times_pressed == 1:
            self.name_label.setText('Why did you press me?')
        if self.times_pressed == 2:
            self.name_label.setText('Warning')
            self.button.setText('Feeling lucky')
            self.button.adjustSize()
            self.button.move(70, 70)
        if self.times_pressed == 3:
            print('The window has been closed')
            self.close()

    def clearText(self):
        self.name_edit.clear()

    def acceptText(self):
        print(self.name_edit.text())
        self.close()

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

















































































