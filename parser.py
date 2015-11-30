# coding: utf-8

from grab.spider import Spider, Task
import model

class PornHubCategoryParser(Spider):
	initial_urls = []
	#priority_mode='const'
	
	def __init__(self, model):
		super(PornHubCategoryParser, self).__init__()
		self.model = model
		self.cat_index = 0 # index of category, from 0
		PornHubCategoryParser.initial_urls.append(self.model.site_categories)
		

	def task_initial(self, grab, task):
		# find category url and add new category to the model
		for elem in grab.doc.select("//div[@class='category-wrapper']/a"):
			self.model.addCategoryUrl(self.model.site + elem.attr('href'))
		# download category previews
		for elem in grab.doc.select("//div[@class='category-wrapper']/a/img"):
			yield Task("image", url=elem.attr('src'), num=self.cat_index)
			self.cat_index += 1
			self.model.addCategory(elem.attr('alt'))
			#print(elem.attr('src'))

	def task_image(self, grab, task):
		path = '{path}/{i}.jpg'.format(i = task.num, path = self.model.categories_image_path)
		grab.response.save(path)

class PornHubPageParser(Spider):
	initial_urls = []
	#priority_mode='const'
	
	def __init__(self, model, page_url, category_id, page = 0):
		super(PornHubPageParser, self).__init__()
		self.model = model
		self.category_id = category_id # from 0
		self.page = page               # from 0 or 1
		PornHubPageParser.initial_urls.append(page_url)
		

	def task_initial(self, grab, task):
		porn = [] # list or porn videos from this page
		
		# get vkeys
		for elem in grab.doc.select("//li[@class='videoblock']"):
			porn.append({'vkey': elem.attr('_vkey')})
		
		# append names to vkeys
		i = 0;
		for elem in grab.doc.select("//li[@class='videoblock']/a[@class='img']"):
			porn[i]['name'] = elem.attr('_vkey')
			i += 1
			print(porn[i]['name'])
		
		# if this is category url (page == 0), we should detect page url
		page_url = str()
		if self.page == 0:
			for elem in grab.doc.select("//li[@class='page_number']/a[@class='greyButton']"):
				if elem.text() == '2':
					page_url = elem.attr('href')[0:-1]
		
		#print(page_url)
		# add porn videos to the model
		for x in porn:
			self.model.addPornVideo(x, self.category_id, page_url);
	
	
	def task_image(self, grab, task):
		path = '{path}/{vkey}.jpg'.format(vkey = task.vkey, path = self.model.videos_preview_image_path)
		grab.response.save(path)

class PyJizzParser(object):
	def __init__(self, model):
		self.model = model
		
	def parseCategories(self):
		c = PornHubCategoryParser(self.model)
		c.run()
	
	def parseCategoryPage(self, category, page = 1):
		if page == 0 or page == 1:
			url = self.model.categories_url[category]
		else:
			url = "{site}{page_url}{page}".format(
				site = self.model.site,
				page_url = self.model.porn[category]['page_url'],
				page = page)
		p = PornHubPageParser(m, url, category)
		p.run()
		

if __name__ == '__main__':
	m = model.Porn()
	p = PyJizzParser(m)
	p.parseCategories()
	p.parseCategoryPage(0)
	p.parseCategoryPage(0, 3)
	
	print(m.porn[0])