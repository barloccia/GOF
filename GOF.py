# The game of life
import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QMainWindow, QAction, qApp, QStyle, QComboBox, QLabel, QPushButton, QLineEdit, QSlider
from PyQt5.QtGui import *
from PyQt5.QtCore import QBasicTimer
from PyQt5 import QtCore
import qdarkstyle

from chess_board import Chess_Board as _board

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		# creo la tavola
		board = _board()
		self.stepByStep = False # serve per capire quale funzionalita e attiva
		# la imposto
		self.setCentralWidget(board)
		size_x = self.centralWidget().size_x
		size_y = self.centralWidget().size_y
		self.setGeometry(300, 300, 15*size_x, 15*size_y)
		# min e max size 
		self.setFixedSize(15*size_x, 15*size_y)
		self.setWindowTitle('The game of life')
		self.style = self.style()
		self.play_icon = self.style.standardIcon(QStyle.SP_MediaPlay)
		self.stop_icon = self.style.standardIcon(QStyle.SP_MediaStop)
		# costruisco il menu
		self.toolbar_1 = self.addToolBar('Main Window')
		self.buildToolbar_1()
		# toolbar per la velocita
		self.addToolBarBreak()
		self.toolbar_2 = self.addToolBar('Speed')
		self.buildToolbar_2()
		
		self.show()

	def buildToolbar_1(self): # main toolbar
		exit = QAction(QIcon('imgs/exit_icon.ico'), 'Exit', self)
		exit.setShortcut('Ctrl+Q')
		exit.triggered.connect(qApp.quit)
		self.toolbar_1.addAction(exit)

		# collego il tasto play al trigger del timer
		self.timer_toggle = QAction(QIcon(self.play_icon), 'Play', self)
		self.timer_toggle.setShortcut('Ctrl+S')
		self.timer_toggle.triggered.connect(self.timerSwitch)
		self.toolbar_1.addAction(self.timer_toggle)

		# Random Fill
		randomFill = QAction(QIcon('imgs/random_icon.png'), 'Random Fill', self)
		randomFill.setShortcut('Ctrl+R')
		randomFill.triggered.connect(self.centralWidget().randomFill)
		self.toolbar_1.addAction(randomFill)

		# upload pattern
		comboBox = QComboBox(self)
		comboBox.addItem("Clear")
		comboBox.addItem("Glider")
		comboBox.addItem("Small Exploder")
		comboBox.addItem("Exploder")
		comboBox.addItem("10 Cell Row")
		comboBox.addItem("Tumbler")
		comboBox.move(330, 10)
		comboBox.activated[str].connect(self.centralWidget().comboChanged)

		# able step by step functionality
		self.trigStepByStep = QAction(QIcon('imgs/abel_SbS.png'), 'Step by Step', self)
		self.trigStepByStep.setShortcut('Ctrl+Z')
		self.trigStepByStep.triggered.connect(self.triggerToolbar)
		self.toolbar_1.addAction(self.trigStepByStep)

		

	def buildToolbar_2(self): # speed toolbar
		default = str(150) # velocita di default
		# slider per cambiare la velocita
		self.slider = QSlider(QtCore.Qt.Horizontal)
		self.slider.setMinimum(50)
		self.slider.setMaximum(500)
		self.slider.setValue(int(default))
		self.slider.setTickPosition(QSlider.TicksBelow)
		self.slider.setTickInterval(50)
		self.toolbar_2.addWidget(self.slider)
		self.slider.valueChanged.connect(self.speedChanged)

		# label per indicare la velocita
		self.speedLabel = QLabel()
		self.speedLabel.setText(default)
		self.speedLabel.setContentsMargins(10, 10, 10, 10)
		self.toolbar_2.addWidget(self.speedLabel)
	
	def triggerToolbar(self):
		if self.stepByStep:
			self.toolbar_2.show()
			self.stepByStep = False
		else:
			self.toolbar_2.hide()
			self.stepByStep = True
		
	def timerSwitch(self):
		if self.stepByStep:
			self.centralWidget().singleEvent() 
		else:
			if self.centralWidget().running:
				# disabilito lo step by step
				self.trigStepByStep.setDisabled(False)
				self.timer_toggle.setIcon(self.play_icon)
				self.timer_toggle.setText('Play')
				self.centralWidget().timer.stop()
				self.centralWidget().running = False

			else:
				# riabilito lo step by step
				self.trigStepByStep.setDisabled(True)
				self.timer_toggle.setIcon(self.stop_icon)
				self.timer_toggle.setText('Stop')
				# richiama time_start della classe Chess_board
				self.centralWidget().time_start(int(self.slider.value()))
				self.centralWidget().running = True

	def speedChanged(self):
		if self.centralWidget().running:
			self.centralWidget().timer.stop()
			self.centralWidget().running = False
			self.centralWidget().time_start(int(self.slider.value()))
			self.centralWidget().running = True
		self.speedLabel.setText(str(self.slider.value()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ex = MainWindow()
    sys.exit(app.exec_())


