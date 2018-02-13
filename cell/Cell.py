import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QMainWindow, QAction, qApp, QStyle
from PyQt5.QtGui import QPainter, QColor, QIcon
from PyQt5.QtCore import QBasicTimer


class Cell(QWidget):
	def __init__(self):
		super().__init__()
		self.color = 'white'
		self.live = 0
		self.liveNeighbors = 0 

	def paintEvent(self, color): # qWidget default fuction, call on the update
		qp = QPainter()
		qp.begin(self) 
		self.drawRectangle(qp)
		qp.end()

	def drawRectangle(self, qp):
		# grey color for a default cell
		col = QColor(205, 205, 205)
		col.setNamedColor('#cdcdcd')
		qp.setPen(col)
		qp.setBrush(QColor(self.color))
		qp.drawRect(0, 0, 15, 15)

	def mousePressEvent(self, event): # the cell has been clicked, change color
		self.changeState()

	def changeState(self):
		if self.live:
			self.color = 'white'
			self.live = 0
		else:
			self.color = 'black'
			self.live = 1
		self.update() # by QWidgets, upload the rectangle

	def checkStatus(self):
		# GAME RULES
		# il controllo sulla vita/morte viene affidato alla singola cella 
		# Qualsiasi cella viva con meno di due celle vive adiacenti muore, come per effetto d'isolamento;
		# Qualsiasi cella viva con due o tre celle vive adiacenti sopravvive alla generazione successiva;
		# Qualsiasi cella viva con più di tre celle vive adiacenti muore, come per effetto di sovrappopolazione;
		# Qualsiasi cella morta con esattamente tre celle vive adiacenti diventa una cella viva, come per effetto di riproduzione.
		if self.live and self.liveNeighbors < 2:
			self.changeState()
		elif self.live and self.liveNeighbors in range(2,3):
			pass
		elif self.live and self.liveNeighbors > 3:
			self.changeState()
		if not self.live and self.liveNeighbors == 3:
			self.changeState()




