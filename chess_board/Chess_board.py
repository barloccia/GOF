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
		# imposto il Grid Layout
		self.grid = QGridLayout()
		self.grid.setSpacing(0)
		self.setLayout(self.grid)
		# grandezza della matrice
		self.size_x = 30
		self.size_y = 30
		# Posizione le celle nelle posizioni
		board = [(i,j) for i in range(self.size_x) for j in range(self.size_y)]
		for pos in board:
			# le pos son del tipo (0,0) - (0,1) - (0,2) ... 
			curr_cell = _cell()
			self.grid.addWidget(curr_cell, *pos)
		self.timer = QBasicTimer()
		self.running = False

	def timerEvent(self, e): # funzione di default richiamata in automatico in relazione al timer event (start e stop timer)
		for i in range(self.grid.count()): # numero totale di celle
			layoutItem = self.grid.itemAt(i) # prendo il layout alla posizione i
			position = self.grid.getItemPosition(i) # prendo la posizione matriciale dell'elemento
			x, y = position[0], position[1]
			cell = layoutItem.widget() # ricavo la cella 
			self.countNeighbors(x, y, cell)

		for i in range(self.grid.count()):
			layoutItem = self.grid.itemAt(i)
			cell = layoutItem.widget()
			cell.checkStatus()

	def singleEvent(self): # funzione di default richiamata in automatico in relazione al timer event (start e stop timer)
		for i in range(self.grid.count()): # numero totale di celle
			layoutItem = self.grid.itemAt(i) # prendo il layout alla posizione i
			position = self.grid.getItemPosition(i) # prendo la posizione matriciale dell'elemento
			x, y = position[0], position[1]
			cell = layoutItem.widget() # ricavo la cella 
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
		# clear della board
		self.clearBoard()
		patternSetter = Pattern(self.grid)
		# Glider Layout
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
		# Essendo 1 oppure 0 le vado a sommare e trovo il totale dei vicini vivi o morti
		cell.liveNeighbors = destro + sinistro + sopra + sotto + sopra_destro + sotto_destro + sotto_sinistro + sopra_sinistro
		
	def time_start(self, speed):
		# richiama la funzione timerEvent nativa della classe QWidget, passandogli la velocità 
		self.timer.start(speed, self)

	
    