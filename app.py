import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self):
        super(). __init__()
        self.title = 'This is my title'

        self.width = 480
        self.height = 640
        self.right = 10
        self.left = 10
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.right, self.height, self.width)
        self.statusBar().showMessage('Message in statusBar.')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = MainWindow()
    sys.exit(app.exec_())







