import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QMainWindow, QAction, qApp, QStyle, QFileDialog
from PyQt5.QtGui import QPainter, QColor, QIcon
from PyQt5.QtCore import QBasicTimer

from cell import Cell as _cell 
from pattern import Pattern 


class Chess_Board(QWidget):
	def __init__(self):
		super().__init__()
		# set the grid layout
		self.grid = QGridLayout()
		self.grid.setSpacing(0)
		self.setLayout(self.grid)
		# dimension of the matrix
		self.size_x = 30
		self.size_y = 30
		# set the cell into the matrix (widget into widget)
		board = [(i,j) for i in range(self.size_x) for j in range(self.size_y)]
		for pos in board:
			# so the positions are like: (0,0) - (0,1) ect..
			curr_cell = _cell()
			self.grid.addWidget(curr_cell, *pos)
		self.timer = QBasicTimer()
		self.running = False

	def timerEvent(self, e): # default function of wWidget. Called it automatically from sytart and stop timer
		for i in range(self.grid.count()): 
			layoutItem = self.grid.itemAt(i) # get the layout from the i position
			position = self.grid.getItemPosition(i) # get the matrix position
			x, y = position[0], position[1]
			cell = layoutItem.widget() # get the cell
			self.countNeighbors(x, y, cell)

		for i in range(self.grid.count()):
			layoutItem = self.grid.itemAt(i)
			cell = layoutItem.widget()
			cell.checkStatus()

	def singleEvent(self): # default function as above
		# the same system above
		for i in range(self.grid.count()): 
			layoutItem = self.grid.itemAt(i) 
			position = self.grid.getItemPosition(i) 
			x, y = position[0], position[1]
			cell = layoutItem.widget() 
			self.countNeighbors(x, y, cell)

		for i in range(self.grid.count()):
			layoutItem = self.grid.itemAt(i)
			cell = layoutItem.widget()
			cell.checkStatus()

	def randomFill(self):
			for i in range(self.grid.count()):
				rand = random.randint(0, 1)
				if rand:
					layoutItem = self.grid.itemAt(i)
					cell = layoutItem.widget()
					cell.changeState()

	def comboChanged(self, text):
		# First of all clear the board
		self.clearBoard()
		patternSetter = Pattern(self.grid)
		# lookign for pattern class
		if text == 'Glider':
			patternSetter.Glider()
		if text == 'Small Exploder':
			patternSetter.smallExploder()
		if text == 'Exploder':
			patternSetter.exploder()
		if text == '10 Cell Row':
			patternSetter.cellRow()
		if text == 'Tumbler':
			patternSetter.tumbler()

	def clearBoard(self):
		for i in range(self.grid.count()):
				layoutItem = self.grid.itemAt(i)
				cell = layoutItem.widget()
				if cell.live:
					cell.changeState()

	def countNeighbors(self, x, y, cell):
		# guardo la condizione di tutte le celle intorno
		destro = self.grid.itemAtPosition(x, (y + 1) % self.size_y).widget().live
		sinistro = self.grid.itemAtPosition(x, (y - 1) % self.size_y).widget().live
		sopra = self.grid.itemAtPosition((x - 1) % self.size_x, y).widget().live
		sotto = self.grid.itemAtPosition((x + 1) % self.size_x, y).widget().live
		sopra_destro = self.grid.itemAtPosition((x - 1) % self.size_x, (y + 1) % self.size_y).widget().live
		sotto_destro = self.grid.itemAtPosition((x + 1) % self.size_x, (y + 1) % self.size_y).widget().live
		sotto_sinistro = self.grid.itemAtPosition((x + 1) % self.size_x, (y - 1) % self.size_y).widget().live
		sopra_sinistro = self.grid.itemAtPosition((x - 1) % self.size_x, (y - 1) % self.size_y).widget().live
		# The results are 0 or 1. So sum for all results and get the alive neighbors for the selected cell
		cell.liveNeighbors = destro + sinistro + sopra + sotto + sopra_destro + sotto_destro + sotto_sinistro + sopra_sinistro
		
	def time_start(self, speed):
		# rcall the default function with the speed value
		self.timer.start(speed, self)

	
    