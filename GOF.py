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
		# from the class board re-call the initializer for the chess board
		board = _board()
		self.stepByStep = False # Wich functionality is active 
		# set the board in the main window and set the shape
		self.setCentralWidget(board)
		size_x = self.centralWidget().size_x
		size_y = self.centralWidget().size_y
		self.setGeometry(300, 300, 15*size_x, 15*size_y)
		self.setFixedSize(15*size_x, 15*size_y)
		self.setWindowTitle('The game of life')
		self.style = self.style()
		# set the two icons for start and end the game
		self.play_icon = self.style.standardIcon(QStyle.SP_MediaPlay)
		self.stop_icon = self.style.standardIcon(QStyle.SP_MediaStop)

		# build the first toolbar 
		self.toolbar_1 = self.addToolBar('Main Window')
		self.buildToolbar_1()
		# build the second toolbar
		self.addToolBarBreak()
		self.toolbar_2 = self.addToolBar('Speed')
		self.buildToolbar_2()
		# see below fot the build toolbar functions
		
		self.show()

	def buildToolbar_1(self): 
		# add action to exit from the game
		exit = QAction(QIcon('imgs/exit_icon.ico'), 'Exit', self)
		exit.setShortcut('Ctrl+Q')
		exit.triggered.connect(qApp.quit)
		self.toolbar_1.addAction(exit)

		# link the play button to the triggered timer
		self.timer_toggle = QAction(QIcon(self.play_icon), 'Play', self)
		self.timer_toggle.setShortcut('Ctrl+S')
		self.timer_toggle.triggered.connect(self.timerSwitch) # interrupt the trigger timer and stop the game
		self.toolbar_1.addAction(self.timer_toggle)

		# random fill action
		randomFill = QAction(QIcon('imgs/random_icon.png'), 'Random Fill', self)
		randomFill.setShortcut('Ctrl+R')
		randomFill.triggered.connect(self.centralWidget().randomFill)
		self.toolbar_1.addAction(randomFill)

		# build slide fo upload pre-built patterns
		# looking for the pattern class
		comboBox = QComboBox(self)
		comboBox.addItem("Clear")
		comboBox.addItem("Glider")
		comboBox.addItem("Small Exploder")
		comboBox.addItem("Exploder")
		comboBox.addItem("10 Cell Row")
		comboBox.addItem("Tumbler")
		comboBox.move(330, 10)
		comboBox.activated[str].connect(self.centralWidget().comboChanged)

		# step by step action
		self.trigStepByStep = QAction(QIcon('imgs/abel_SbS.png'), 'Step by Step', self)
		self.trigStepByStep.setShortcut('Ctrl+Z')
		self.trigStepByStep.triggered.connect(self.triggerToolbar)
		self.toolbar_1.addAction(self.trigStepByStep)

		
	def buildToolbar_2(self): # toolbar only for speed manage
		default = str(150) # default speed

		# sset the slider to change speed
		self.slider = QSlider(QtCore.Qt.Horizontal)
		self.slider.setMinimum(50)
		self.slider.setMaximum(500)
		self.slider.setValue(int(default))
		self.slider.setTickPosition(QSlider.TicksBelow)
		self.slider.setTickInterval(50)
		self.toolbar_2.addWidget(self.slider)
		self.slider.valueChanged.connect(self.speedChanged)

		# set label to see the speed to the user
		self.speedLabel = QLabel()
		self.speedLabel.setText(default)
		self.speedLabel.setContentsMargins(10, 10, 10, 10)
		self.toolbar_2.addWidget(self.speedLabel)
	
	def triggerToolbar(self):
		# change the toolbar when step-by-step is active
		# only the normal main toolbar otherwise
		if self.stepByStep:
			self.toolbar_2.show()
			self.stepByStep = False
		else:
			self.toolbar_2.hide()
			self.stepByStep = True
		
	def timerSwitch(self):
		# single action to do if step-by-step is active
		if self.stepByStep:
			self.centralWidget().singleEvent() 
		else:
			if self.centralWidget().running: # if stop is pressed
				# disable step-by-step action
				self.trigStepByStep.setDisabled(False)
				self.timer_toggle.setIcon(self.play_icon)
				self.timer_toggle.setText('Play')
				self.centralWidget().timer.stop()
				self.centralWidget().running = False

			else:
				# able the step-by-step
				self.trigStepByStep.setDisabled(True)
				self.timer_toggle.setIcon(self.stop_icon)
				self.timer_toggle.setText('Stop')
				# call time_start from the chess_board class
				self.centralWidget().time_start(int(self.slider.value()))
				self.centralWidget().running = True

	def speedChanged(self): # obviuous from the name
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


