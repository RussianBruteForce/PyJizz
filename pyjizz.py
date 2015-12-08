import sys
import os
from model import Porn
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QUrl
from parser import PyJizzParser

from PyQt5.QtWidgets import QApplication
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from mainwindow import PyJizzMainWindow

class PyJizz(QObject):
	def __init__(self, mainwindow, model):
		super(PyJizz, self).__init__()
		self.mainwindow = mainwindow
		self.model = model
		self.parser = PyJizzParser(self.model)
		self.player = QMediaPlayer()
		self.player.setVideoOutput(self.mainwindow.player)
		self.player.setMedia(QMediaContent(QUrl("http://cdn2b.video.pornhub.phncdn.com/videos/201508/19/55394221/vl_720P_1591.0k_55394221.mp4?rs=200&ri=2900&ipa=2.94.184.41&s=1448912461&e=1448919661&h=db084a1408809a2b48c814156f2c30a6")))
		self.player.setVolume(100)
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
		self.player.play()
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
