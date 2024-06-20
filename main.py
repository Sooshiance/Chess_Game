import sys

from PySide6.QtWidgets import QApplication, QWidget, QGridLayout
from PySide6.QtGui import QColor, QPainter, QFont
from PySide6.QtCore import QRect


class ChessBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Chess Board')
        self.setGeometry(300, 300, 1050, 1050)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = QRect(0, 0, self.width()//8, self.height()//8)
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    painter.fillRect(rect.translated(col * self.width()//8, row * self.height()//8), QColor('white'))
                else:
                    painter.fillRect(rect.translated(col * self.width()//8, row * self.height()//8), QColor('black'))
        # Draw labels on the sides of the board
        font = QFont("Arial", 12)
        painter.setFont(font)
        
        # Draw numbers on the left and right sides
        for i in range(1,9):
            painter.drawText(5, i*self.height()//8 - 10, str(i))
            painter.drawText(self.width()-15, i*self.height()//8 - 10, str(i))

        # Draw alphabets on the top and bottom sides
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        
        for i in range(8):
            painter.drawText(i*self.width()//8 + (self.width()//16) -5 ,self.height()-5 , alphabet[i])
            painter.drawText(i*self.width()//8 + (self.width()//16) -5 ,15 , alphabet[i])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ChessBoard()
    sys.exit(app.exec())
