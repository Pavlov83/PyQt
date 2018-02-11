import sys
from PyQt5.QtWidgets import QApplication, QWidget

class App(QWidget):

    def __init__(self):
        super(). __init__()
        self.title = 'This is my app window'
        self.initUI()

    
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.show()
        

if __name__ == '__main__':
    app  = QApplication(sys.argv)
    start = App()
    sys.exit(app.exec_())
    
