from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class Button:
    def __init__(self, text, results):
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda: self.handleInput(self.text))

    def handleInput(self, v):
        if v== "=":
            res = eval(self.results.text())
            self.results.setText(str(res))
        elif v == "AC":
            self.results.setText("")
        elif v == "DEL":
            current_value = self.results.text()
            self.results.setText(current_value[:-1])
            
        else:
            current_value = self.results.text()
            new_value = current_value + str(v)
            self.results.setText(new_value)
            
        
        


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calc")
        self.CreateApp()
        self.show()



    def CreateApp(self):
        #create the grid layout
        grid = QGridLayout()
        results = QLineEdit()

##        button1 = QPushButton("One")
##        button2 = QPushButton("Two")
##        button3 = QPushButton("Three")
##        button4 = QPushButton("My last button")
##
##        grid.addWidget(button1, 0, 0, 1, 1)
##        grid.addWidget(button2, 0, 1, 1, 1)
##        grid.addWidget(button3, 0, 2, 1, 1)
##        grid.addWidget(button4, 1, 0, 1, 2)

        buttons=["AC", "C", "CE", "/",
                 7, 8, 9, "*",
                 4, 5, 6, "-",
                 1, 2, 3, "+",
                 0, ".", "=", "DEL"

            ]

        row = 1
        col = 0

        grid.addWidget(results, 0, 0, 1, 4)

        for button in buttons:
            if col > 3:
                col = 0
                row += 1

            buttonObj = Button(button, results)

            if button == 0:
                grid.addWidget(buttonObj.b, row, col, 1, 2)
                col += 1
            else:
                grid.addWidget(buttonObj.b, row, col, 1, 1)

            col += 1
            
        self.setLayout(grid)
        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Application()
    window.show()

    sys.exit(app.exec_())
        

        
