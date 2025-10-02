import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit, QCheckBox)
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        # self.setGeometry(100, 100, 250, 150)
        self.setGeometry(100, 100, 250, 150)
        self.setWindowTitle('QPushButton Example')
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        header_label = QLabel('Select all that apply', self)
        header_label.setWordWrap(True)
        header_label.move(20, 10)

        morning_cb = QCheckBox('Morning [8 AM - 2 PM]', self)
        morning_cb.move(40, 60)
        morning_cb.toggle()
        morning_cb.toggled.connect(self.printSelected)

        after_cb = QCheckBox('Afternoon [1 PM - 8 PM]', self)
        after_cb.move(40, 80)
        after_cb.toggled.connect(self.printSelected)

        night_cb = QCheckBox('Night [7 PM - 3 AM]', self)
        night_cb.move(40, 100)
        night_cb.toggled.connect(self.printSelected)

    def printSelected(self, checked):
        sender = self.sender()
        if checked:
            print(f'{sender.text()} Selected')
        else:
            print(f'{sender.text()} Deselected.')








if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())




