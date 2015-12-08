class Porn(object):
	def __init__(self):
		self.porn = []
		#self.categories = []
		self.categories_url = []
		self.categories_image_path = 'images/category'
		self.videos_preview_image_path = 'images/preview'
		self.site = 'http://www.pornhub.com'
		self.site_categories = '{site}/categories'.format(site = self.site)
		self.site_video_template = '{site}'.format(site = self.site)

	def addPornVideo(self, vid, category_id, page_url):
		info = self.parser.getInfo(vid['vkey'])
		vid['url'] = info['url']
		vid['title'] = info['title']
		vid['thumbnail'] = info['thumbnail']
		vid['view_count'] = info['view_count']
		
		self.porn[category_id]["videos"].append(vid)
		#print (vid)
		if len(page_url) != 0:
			self.porn[category_id]["page_url"] = page_url

	def addCategory(self, cat):
		#self.categories.append(cat)
		self.porn.append({'category':cat, 'videos':[], 'page_url':''})

	def addCategoryUrl(self, url):
		self.categories_url.append(url)
		#print(url)
		#print(self.categories_url)


from PyQt5.QtCore import *

class PageModel(QAbstractTableModel):
	def __init__(self, model):
		super(PageModel, self).__init__()
		self.model = model
		self.currentCategory = None
		
	def setCategory(self, cat):
		self.currentCategory = cat
		
	def upd(self):
		#left = self.createIndex(0,0)
		#left.setRow(0)
		
		#right = self.createIndex(self.rowCount()-1,3)
		#self.dataChanged.emit(left,right)
		self.dataChanged.emit(self.index(0, 0), self.index(self.rowCount()-1, 3))
		print("updated!")
	
	def rowCount (self, parent = QModelIndex()):
		#print("rows ", self.currentCategory)
		if self.currentCategory == None:
			return 0
		else:
			#print("count: ", len(self.model.porn[self.currentCategory]['videos']))
			return len(self.model.porn[self.currentCategory]['videos'])
		
	def columnCount (self, parent = QModelIndex()):
		#print("cols")
		return 4
	
	def data(self, index, role=Qt.DisplayRole):
		if role == Qt.DisplayRole:
			i = index.row()
			j = index.column()
			# 0 thimbnail
			if j == 1:
				return QVariant(self.model.porn[self.currentCategory]['videos'][i]['title'])
			elif j == 2:
				return QVariant(self.model.porn[self.currentCategory]['videos'][i]['view_count'])
			elif j == 3:
				return QVariant(QUrl(self.model.porn[self.currentCategory]['videos'][i]['url']))
			return QVariant("666")
		else:
			return QVariant()