import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Форма PyQt6")
        self.setGeometry(300, 300, 400, 200)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        label = QLabel("Добро пожаловать в PyQt6!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        label.setFont(font)
        
        layout.addWidget(label)

def main():
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()