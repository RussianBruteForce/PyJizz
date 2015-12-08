import sys
import os
from model import Porn
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QUrl, QModelIndex
from parser import PyJizzParser

from PyQt5.QtWidgets import QApplication
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from mainwindow import PyJizzMainWindow
from model import PageModel

class PyJizz(QObject):
	def __init__(self, mainwindow, model):
		super(PyJizz, self).__init__()
		self.mainwindow = mainwindow
		self.model = model
		self.parser = PyJizzParser(self.model)
		self.tableModel = PageModel(self.model)
		self.mainwindow.ui.tableView.setModel(self.tableModel)
		self.currentCategory = None
		#self.player = QMediaPlayer()
		#self.player.setVideoOutput(self.mainwindow.player)
		#self.player.setMedia(QMediaContent(QUrl("http://cdn2b.video.pornhub.phncdn.com/videos/201508/19/55394221/vl_720P_1591.0k_55394221.mp4?rs=200&ri=2900&ipa=2.94.184.41&s=1448912461&e=1448919661&h=db084a1408809a2b48c814156f2c30a6")))
		#self.player.setVolume(100)
		
		self.connections()
		
		self.showCategories()
		
		self.block(False)

	def connections(self):
		self.mainwindow.categoryClicked.connect(self.onCategoryClicked)
		self.mainwindow.page.connect(self.onPageChanged)
		
	def block(self, blocked):
		self.mainwindow.setEnabled(not blocked)

	def showCategories(self):
		#if not os.path.isdir(self.model.categories_image_path):
		self.parser.parseCategories()
		id = 0
		for x in self.model.porn:
			path = '{ip}/{i}.jpg'.format(ip = self.model.categories_image_path, i = id)
			name = x['category']
			self.mainwindow.addCategory(id, name, path)
			id += 1
		#self.mainwindow.addCategory(0,"0", self.model.categories_image_path + "/0.jpg")
		#self.mainwindow.addCategory(1,"1", self.model.categories_image_path + "/1.jpg")
		#self.mainwindow.addCategory(2,"2", self.model.categories_image_path + "/2.jpg")
		#self.mainwindow.addCategory(3,"3", self.model.categories_image_path + "/3.jpg")
	
	def pageHandler(self, page):
		print(page)
		if page == 1:
			self.mainwindow.ui.pagePrevButton.setEnabled(False)
		elif not self.mainwindow.ui.pagePrevButton.isEnabled():
			self.mainwindow.ui.pagePrevButton.setEnabled(True)
			
		#last_index = self.tableModel.rowCount()
		#print("last ", last_index)
		#self.tableModel.beginInsertRows(QModelIndex(),last_index,3)
		self.tableModel.beginResetModel()
		
		if self.currentCategory != None:
			self.parser.parseCategoryPage(self.currentCategory, page)
			
		self.tableModel.upd()
		#self.tableModel.endInsertRows()
		self.tableModel.endResetModel()
		
		self.mainwindow.ui.tableView.resizeColumnsToContents() 
	
	@pyqtSlot(int)
	def onCategoryClicked(self, _id):
		print("cat ", _id)
		#self.parser.parseCategoryPage(_id)
		self.currentCategory  = _id
		self.tableModel.setCategory(_id)
		self.mainwindow.resetPages()
		
	@pyqtSlot(int)
	def onPageChanged(self, page):
		print("page changed")
		self.block(True)
		self.pageHandler(page)
		self.block(False)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = PyJizzMainWindow()
	window.setEnabled(False)
	window.show()
	porn = Porn()
	jizz = PyJizz(window, porn)
	
	sys.exit(app.exec_())
