import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QMessageBox, QPushButton, QLineEdit, QCheckBox)
from PyQt6.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 500, 500)
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        catalogue_label = QLabel('Author catalogue', self)
        catalogue_label.move(100, 10)
        catalogue_label.setFont(QFont('Arial', 18))

        # search_label = QLabel('Search the index for an author:', self)
        # search_label.move(20, 40)

        author_label = QLabel('Name: ', self)
        author_label.move(20 ,74)

        self.author_edit = QLineEdit(self)
        self.author_edit.move(70, 70)
        self.author_edit.resize(240, 24)
        self.author_edit.setPlaceholderText('Enter names as: First Last')

        search_button = QPushButton('Search', self)
        search_button.move(140, 100)
        search_button.clicked.connect(self.searchAuthors)

        self.header_label = QLabel('', self)
        self.header_label.move(250, 40)
        self.header_label.resize(100, 100)

    def searchAuthors(self):
        # QMessageBox.information(self, 'My Example Header', 'My Example Message', QMessageBox.StandardButton.Ok)

        answer = QMessageBox.question(self, 'My Question Header', 
                             'Do you wish to continue?',
                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if answer == QMessageBox.StandardButton.Yes:
            self.header_label.setText('You clicked yes')
        elif answer == QMessageBox.StandardButton.No:
            self.header_label.setText('You clicked no')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

