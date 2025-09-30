import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self):
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle('QLabel Example')
        self.setUpMainWindow()
        self.show()

    def createImageLabels(self):
        hello_label = QLabel(self)
        hello_label.setText('Hello')
        hello_label.move(105, 15)
        image = 'images/world.png'

        try:
            with open(image):
                world_label = QLabel(self)
                pix_map = QPixmap(image)
                world_label.setPixmap(pix_map)
                world_label.move(25, 40)
        except FileNotFoundError as error:
            print(f'Image not found. \nError: {error}')


class MainWindow2(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(50, 50, 250, 400)
        self.setWindowTitle('2.1 - User Profile GUI')
        self.setUpMainWindow()
        self.show()

    def createImageLabels(self):
        images = ['images/skyblue.png', 'images/profile_image.png']
        for image in images:
            try:
                with open(image):
                    label = QLabel(self)
                    pix_map = QPixmap(image)
                    label.setPixmap(pix_map)
                    if image == 'images/profile_image.png':
                        label.move(80, 20)
            except FileNotFoundError as error:
                print(f'Image not found.\Error: {error}')

    def setUpMainWindow(self):
        self.createImageLabels()
        user_label = QLabel(self)
        user_label.setText('John Doe')
        user_label.setFont(QFont('Arial', 20))
        user_label.move(85, 140)
        
        bio_label = QLabel(self)
        bio_label.setFont(QFont('Arial', 17))
        bio_label.move(15, 170)
        
        about_label = QLabel(self)
        about_label.setText("I'm a Software Engineer with 10 years experience creating awesome code.")
        about_label.setWordWrap(True)
        about_label.move(15, 190)

        skills_label = QLabel(self)
        skills_label.setText("Skills")
        skills_label.setFont(QFont("Arial", 17))
        skills_label.move(15, 240)
        
        languages_label = QLabel(self)
        languages_label.setText("Python  |  PHP  |  SQL  |  JavaScript")
        languages_label.move(15, 260)

        experience_label = QLabel(self)
        experience_label.setText("Experience")
        experience_label.setFont(QFont("Arial", 17))
        experience_label.move(15, 290)

        developer_label = QLabel(self)
        developer_label.setText("Python Developer")
        developer_label.move(15, 310)
        
        dev_dates_label = QLabel(self)
        dev_dates_label.setText("Mar 2011 - Present")
        dev_dates_label.setFont(QFont("Arial", 10))
        dev_dates_label.move(15, 330)
        
        driver_label = QLabel(self)
        driver_label.setText("Pizza Delivery Driver")
        driver_label.move(15, 350)
        
        driver_dates_label = QLabel(self)
        driver_dates_label.setText("Aug 2015 - Dec 2017")
        driver_dates_label.setFont(QFont("Arial", 10))
        driver_dates_label.move(15, 370)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # window = MainWindow()
    window = MainWindow2()
    sys.exit(app.exec())



