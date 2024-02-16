import sys
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from ui_main import Ui_MainWindow

class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())
