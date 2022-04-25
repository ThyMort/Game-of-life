from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem, QWidget
from PyQt5.QtGui import QPen, QBrush, QPainter, QColor, QFont
from PyQt5.Qt import Qt

from collections import Counter
import math

cellList = Counter()
show_info = False
display_info = ['','',-1]

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1100, 785)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")

		self.mainFrame = _mainFrame(self.centralwidget)
		self.mainFrame.setGeometry(QtCore.QRect(40, 30, 650, 650))
		self.mainFrame.setAutoFillBackground(True)
		self.mainFrame.setObjectName("widget1")
		p = self.mainFrame.palette()
		p.setColor(self.mainFrame.backgroundRole(), Qt.white)
		self.mainFrame.setPalette(p)
		self.mainFrame.setMouseTracking(True)
		self.mainFrame.setFocus()

		self.sideFrame = _displayFrame(self.centralwidget)
		self.sideFrame.setGeometry(QtCore.QRect(720, 30, 350, 350))
		self.sideFrame.setAutoFillBackground(True)
		self.sideFrame.setObjectName("widget2")
		p = self.sideFrame.palette()
		p.setColor(self.sideFrame.backgroundRole(), Qt.white)
		self.sideFrame.setPalette(p)
		self.mainFrame.setDisplayFrame(self.sideFrame)
		
		self.Button2 = QtWidgets.QPushButton(self.centralwidget)
		self.Button2.setGeometry(QtCore.QRect(380, 690, 121, 31))
		self.Button2.setAutoRepeat(False)
		self.Button2.setObjectName("Button2")
		self.Button1 = QtWidgets.QPushButton(self.centralwidget)
		self.Button1.setGeometry(QtCore.QRect(240, 690, 113, 32))
		self.Button1.setObjectName("Button1")

		MainWindow.setCentralWidget(self.centralwidget)

		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 24))
		self.menubar.setObjectName("menubar")
		self.menuFile = QtWidgets.QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.actionOpen_File = QtWidgets.QAction(MainWindow)
		self.actionOpen_File.setObjectName("actionOpen_File")
		self.menuFile.addAction(self.actionOpen_File)
		self.menubar.addAction(self.menuFile.menuAction())

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		self.Button1.clicked.connect(self.Button1Pressed)
		self.Button2.clicked.connect(self.Button2Pressed)

		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.lifeLoop)
		
		MainWindow.keyPressEvent = self.keyPressEvent

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.Button1.setText(_translate("MainWindow", "Next Iteration"))
		self.Button2.setText(_translate("MainWindow", "Pause/Resume"))
		self.menuFile.setTitle(_translate("MainWindow", "File"))
		self.actionOpen_File.setText(_translate("MainWindow", "Open File"))

	def Button1Pressed(self):
		global cellList
		cellList = life(cellList)
		self.mainFrame.update()

	def Button2Pressed(self):
		if(self.timer.isActive()):
			self.timer.stop()
		else:
			self.timer.start(1)

	def keyPressEvent(self, event):
		if event.key() == QtCore.Qt.Key_N:
			global cellList
			cellList = life(cellList)
			self.mainFrame.update()
		
		if event.key() == QtCore.Qt.Key_P:
			if(self.timer.isActive()):
				self.timer.stop()
			else:
				self.timer.start(15)

	def lifeLoop(self):
		global cellList
		cellList = life(cellList)
		self.mainFrame.update()

class _mainFrame(QWidget): #le stuff
	def __init__(self, container):
		super().__init__(container)
		self.panx = 0
		self.pany = 0
		self.zoom = 1
		self.init_size = 50
		self.info_coor = (0, 0)
	
	def setDisplayFrame(self, frame):
		self.sideFrame = frame

	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self)

		painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))

		painter.scale(self.zoom, self.zoom)
		painter.translate(-self.panx / self.zoom, -self.pany / self.zoom)

		ins = self.init_size
		for x,y in cellList:
			painter.drawRect(ins * x, ins * y, ins, ins)


		# if self.zoom < 0.3:
		# 	return

		# painter.setPen(QColor(180,180,180))

		# w = self.frameGeometry().width()
		# l = self.frameGeometry().height()
		# shiftx = ins * (self.panx // (ins * self.zoom))
		# shifty = ins * (self.pany // (ins * self.zoom))

		# for i in range(int(l/ins/self.zoom) +2):
		# 	x = int(shiftx + i*ins)
		# 	y = int(shifty)
		# 	_y = int(shifty + (l+ins)/self.zoom + self.pany % (ins * self.zoom))
		# 	painter.drawLine(x, y, x, _y)
		# for j in range(int(w/ins/self.zoom) +2):
		# 	x = int(shiftx)
		# 	_x = int(shiftx + (w+ins)/self.zoom + self.panx % (ins * self.zoom))
		# 	y = int(shifty + j*ins)
		# 	painter.drawLine(x, y, _x, y)

		# if show_info:
		# 	painter.setBrush(QColor(150, 150, 150, 50))
		# 	painter.setPen(QColor(Qt.blue))

		# 	for x,y in self.info_list:
		# 		painter.drawRect(ins * x, ins * y, ins, ins)

	def mousePressEvent(self, event): #spawn cells
		if event.button() == Qt.RightButton:
			self.panPos = event.pos()
		elif event.button() == Qt.LeftButton:
			gridx = math.floor(self.mouseToGridX(event.x()))
			gridy = math.floor(self.mouseToGridY(event.y()))
			coord = (gridx, gridy)

			global cellList #radera eller placera celler
			if(cellList[coord] == 0):
				cellList[coord] = 1
			else:
				del cellList[coord]
			
			self.cal_info_coor() #uppdatera animation
			self.cal_display_info()
			self.update()
			self.sideFrame.update()
	
	def keyPressEvent(self, event):
		global show_info
		if event.key() == QtCore.Qt.Key_I:
			show_info = True if show_info == False else False
			self.cal_info_coor()
			self.cal_display_info()
			self.update()
			self.sideFrame.update()
		else:
			self.parentWidget().keyPressEvent(event)
	
	def mouseMoveEvent(self, event):
		if event.buttons() & Qt.RightButton:
			dx = event.x() - self.panPos.x()
			dy = event.y() - self.panPos.y()
			self.panx -= dx
			self.pany -= dy
			self.panPos = event.pos()
			self.update()

		self.mouse_coor = (event.x(), event.y())
		if show_info:
			self.cal_info_coor()
			self.cal_display_info()
			self.update()
			self.sideFrame.update()

	def cal_info_coor(self):
		x = math.floor(self.mouseToGridX(self.mouse_coor[0]))
		y = math.floor(self.mouseToGridY(self.mouse_coor[1]))
		if(self.info_coor[0] == x and self.info_coor[1] == y):
			return
		self.info_coor = (x, y)

	def cal_display_info(self):
		self.info_list = [(self.info_coor[0]+a, self.info_coor[1]+b) for a in [-1,0,1] for b in [-1,0,1]]
		if self.info_coor in cellList:
			display_info[0] = "Alive"
			i = -1
		else:
			display_info[0] = "Dead"
			i = 0
	
		for coor in self.info_list:
			if cellList[coor] == 1:
				i += 1
		display_info[1] = str(i)

		if display_info[0] == "Alive":
			if i < 2:
				x = 0
			elif i <= 3:
				x = 1
			else:
				x = 2
		else:
			if i == 3:
				x = 3
			else:
				x = -1
		display_info[2] = x

	def wheelEvent(self, event): #zoom
		steps = event.angleDelta().y() / 100
		if(steps > 0):
			self.toZoom(event.x(), event.y(), True, abs(steps) + 1)
		elif(steps < 0):
			self.toZoom(event.x(), event.y(), False, abs(steps) + 1)

		self.update()

	def mouseToGridX(self, x): #cell x cordinate
		return (x + self.panx) / (self.zoom * self.init_size)
	
	def mouseToGridY(self, y): #cell y cordinate
		return (y + self.pany) / (self.zoom * self.init_size)
	
	def toZoom(self, mousex, mousey, direction, intensity):
		pre_zoom = self.zoom

		if(direction):
			self.zoom *= intensity
		else:
			self.zoom /= intensity

		self.panx = (mousex + self.panx)/pre_zoom * self.zoom - mousex
		self.pany = (mousey + self.pany)/pre_zoom * self.zoom - mousey

class _displayFrame(QWidget):
	def __init__(self, container):
		super().__init__(container)
		self.pic = QtGui.QPixmap('pic1.png')
		self.rule_list = ((150,QColor(150, 10, 10, 50)),(200,QColor(10, 150, 10, 50)),(250,QColor(150, 10, 10, 50)),(300,QColor(10, 150, 10, 50)))
	
	def paintEvent(self, event):
		painter = QPainter()
		painter.begin(self)

		painter.setFont(QFont("Helvetica Neue", 20, 40))
		painter.drawText(10, 30, "Current State:")
		painter.drawText(10, 90, "Neighbor Count:")
		painter.drawPixmap(0, 150, 350, 200, self.pic)

		if show_info:
			state = display_info[0]
			if state == "Alive":
				painter.setPen(QColor(10, 150, 10))
			else:
				painter.setPen(QColor(150, 10, 10))
			painter.drawText(140, 30, state)

			painter.setPen(Qt.black)
			painter.drawText(165, 90, display_info[1])

			i = display_info[2]
			painter.setBrush(self.rule_list[i][1])
			if i != -1 :
				painter.drawRect(0, self.rule_list[i][0], 350, 50)

def life(pts): #nästa frame
	ns = Counter([(x+a, y+b) for x,y in pts for a in [-1,0,1] for b in [-1,0,1]])
	return Counter([p for p in ns if ns[p]==3 or (ns[p]==4 and p in pts)])

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())