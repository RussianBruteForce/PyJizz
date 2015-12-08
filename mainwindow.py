import sys
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QSize
from PyQt5.QtGui import QIcon, QPixmap
#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtMultimediaWidgets import *
from mainwindow_ui import Ui_MainWindow
from idbutton import IDButton

class PyJizzMainWindow(QMainWindow):
	categoryClicked = pyqtSignal(int)
	page = pyqtSignal(int)
	
	def __init__(self):
		super(PyJizzMainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pageSpinBox.setMinimum(1)
		#self.ui.pag
		
		self.player = QVideoWidget()
		self.ui.playerLayout.addWidget(self.player)
		
		self.ui.pageNextButton.clicked.connect(self.onNextPageButton)
		self.ui.pagePrevButton.clicked.connect(self.onPrevPageButton)
		self.ui.pageSpinBox.valueChanged.connect(self.onPageSpinBox)

	def addCategory(self,_id, text, icon_path):
		b = IDButton(_id, icon_path, self)
		b.setText(text)
		img = QPixmap(icon_path)
		b.setIcon(QIcon(img))
		b.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
		b.setIconSize(img.size()/3)
		b.idSignal.connect(self.onCategoryButtonClicked)
		#self.ui.categoriesLayout.addWidget(b)
		self.ui.scrollAreaWidgetContents.layout().addWidget(b)
	
	@pyqtSlot(int)
	def onCategoryButtonClicked(self, _id):
		self.categoryClicked.emit(_id)
		
	
	@pyqtSlot()
	def onNextPageButton(self):
		page = self.ui.pageSpinBox.value() + 1
		self.ui.pageSpinBox.setValue(page)
		#self.page.emit(page)

	@pyqtSlot()
	def onPrevPageButton(self):
		page = self.ui.pageSpinBox.value() - 1
		self.ui.pageSpinBox.setValue(page)
		#self.page.emit(page)
	
	@pyqtSlot(int)
	def onPageSpinBox(self, page):
		print("spinbox page now is ", page)
		self.page.emit(page)
		
	def resetPages(self):
		self.ui.pageSpinBox.setValue(1)
		self.page.emit(1)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = PyJizzMainWindow()
	window.show()
	sys.exit(app.exec_())
