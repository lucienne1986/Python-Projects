from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.counter = 0


    def init_ui(self):
        self.text_label = QLabel("There has been no name entered")
        self.label = QLabel("Name:" )
        self.name_input = QLineEdit()
        
        self.button = QPushButton("Clicked: ")
        self.button.setText("Set NAme: ")
        self.button.clicked.connect(self.alterName)
        
        h = QHBoxLayout() 
        h.addWidget(self.label)
        h.addWidget(self.name_input)

        v = QVBoxLayout()
        v.addWidget(self.text_label)
        v.addLayout(h)
        v.addWidget(self.button)

        self.setLayout(v)

        self.setWindowTitle("Nothing has been clicked")
        self.show()

    def alterName(self):
        inputted_text = self.name_input.text()
        our_string = "You have entered " + inputted_text
        self.text_label.setText(our_string)
        self.setWindowTitle(inputted_text + " Window")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
        

        
