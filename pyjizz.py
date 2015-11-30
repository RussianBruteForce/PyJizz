import sys
from model import Porn
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from parser import PyJizzParser

from PyQt5.QtWidgets import QApplication
from PyQt5.QtMultimedia import Qt
from mainwindow import PyJizzMainWindow

class PyJizz(QObject):
	def __init__(self, mainwindow, model):
		super(PyJizz, self).__init__()
		self.mainwindow = mainwindow
		self.model = model
		self.parser = PyJizzParser(self.model)
		

		self.connections()
		
		self.showCategories()
		
		self.block(False)

	def connections(self):
		self.mainwindow.categoryClicked.connect(self.onCategoryClicked)
		self.mainwindow.page.connect(self.onPageChanged)
		
	def block(self, blocked):
		self.mainwindow.setEnabled(not blocked)

	def showCategories(self):
		self.mainwindow.addCategory(0,"0", self.model.categories_image_path + "/0.jpg")
		self.mainwindow.addCategory(1,"1", self.model.categories_image_path + "/1.jpg")
		self.mainwindow.addCategory(2,"2", self.model.categories_image_path + "/2.jpg")
		self.mainwindow.addCategory(3,"3", self.model.categories_image_path + "/3.jpg")
	
	def pageHandler(self, page):
		print(page)
		if page == 1:
			self.mainwindow.ui.pagePrevButton.setEnabled(False)
		elif not self.mainwindow.ui.pagePrevButton.isEnabled():
			self.mainwindow.ui.pagePrevButton.setEnabled(True)
	
	@pyqtSlot(int)
	def onCategoryClicked(self, _id):
		print(_id)
		
	@pyqtSlot(int)
	def onPageChanged(self, page):
		self.pageHandler(page)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = PyJizzMainWindow()
	window.setEnabled(False)
	window.show()
	porn = Porn()
	jizz = PyJizz(window, porn)
	
	sys.exit(app.exec_())
