import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QMainWindow, QAction, qApp, QStyle, QFileDialog
from PyQt5.QtGui import QPainter, QColor, QIcon
from PyQt5.QtCore import QBasicTimer

class Pattern():
	def __init__(self, grid):
		self.grid = grid


	def Glider(self):
		layoutItem = self.grid.itemAtPosition(15,15)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(15,16)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(15,14)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(14,16)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(13,15)
		cell = layoutItem.widget()
		cell.changeState()

	def smallExploder(self):
		layoutItem = self.grid.itemAtPosition(15,14)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(15,16)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(16,15)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(14,14)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(14,15)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(14,16)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(13,15)
		cell = layoutItem.widget()
		cell.changeState()

	def exploder(self):
		layoutItem = self.grid.itemAtPosition(13,13)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(14,13)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(15,13)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(16,13)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(17,13)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(13,15)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(17,15)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(13,17)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(14,17)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(15,17)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(16,17)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(17,17)
		cell = layoutItem.widget()
		cell.changeState()

	def cellRow(self):
		for i in range(11,21):
			layoutItem = self.grid.itemAtPosition(15,i)
			cell = layoutItem.widget()
			cell.changeState()
		

	def tumbler(self):
		layoutItem = self.grid.itemAtPosition(16,12)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(17,12)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(18,12)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(18,13)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(14,13)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(13,13)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(13,14)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(14,14)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(16,14)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(17,14)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(15,14)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(15,15)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(15,16)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(14,16)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(13,16)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(16,16)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(17,16)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(13,17)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(14,17)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(18,17)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(18,18)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(17,18)
		cell = layoutItem.widget()
		cell.changeState()
		layoutItem = self.grid.itemAtPosition(16,18)
		cell = layoutItem.widget()
		cell.changeState()




		



























		