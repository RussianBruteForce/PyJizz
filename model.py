from youtube_dl import YoutubeDL


class Porn:
	def __init__(self):
		self.porn = []
		#self.categories = []
		self.categories_url = []
		self.categories_image_path = 'images/category'
		self.videos_preview_image_path = 'images/preview'
		self.site = 'http://www.pornhub.com'
		self.site_categories = '{site}/categories'.format(site = self.site)
		self.site_video_template = '{site}'.format(site = self.site)
		self.ydl = YoutubeDL()
		self.ydl.add_default_info_extractors()
		info = self.ydl.extract_info('http://www.pornhub.com/view_video.php?viewkey=ph55d4ade3ea891', download=False)
		print(info)

	def addPornVideo(self, vid, category_id, page_url):
		self.porn[category_id]["videos"].append(vid)
		if len(page_url) != 0:
			self.porn[category_id]["page_url"] = page_url

	def addCategory(self, cat):
		#self.categories.append(cat)
		self.porn.append({'category':cat, 'videos':[], 'page_url':''})

	def addCategoryUrl(self, url):
		self.categories_url.append(url)
		#print(self.categories_url)
