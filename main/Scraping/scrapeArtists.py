from bs4 import BeautifulSoup
import pickle
import urllib.request
import os

from stringUtil import unpunctuate

with open('data.pkl', 'rb') as fp:
	data = pickle.load(fp)
	genre_list = data['genre_list']


def create_dirs(soup):
	for page in soup.find_all("div", {"id" : ["mw-pages"]}):
		for link in page.find_all('a'):
			page_name = link.get('title')
				
			#print(page_name)
			directory = genre.replace(" ", "_") +"/" + unpunctuate(page_name)
			#if not os.path.exists(directory):
			#	os.makedirs(directory)

error_count = 0
			
for genre in genre_list:
	print(genre)
	"""
	directory = genre.replace(" ", "_") +"\" + page_name
	if not os.path.exists(directory):
		os.mkdir(dir)#os.makedirs(directory)
	"""
	genre = genre.replace(" ", "_")
	url = "http://lyrics.wikia.com/wiki/Category:" + genre
	url = (url.encode('utf-8')).decode()
	
	pg_no = 1
	cond = True

	while cond:
		print(url)
		try:
			content = urllib.request.urlopen(url).read()
			soup = BeautifulSoup(content, 'html.parser')
			pages = soup.find_all("div", {"id" : ["mw-pages"]})
			
			for page in pages:
				for link in page.find_all('a'):
					page_name = link.get('title')
						
					if page_name:
						directory = genre.replace(" ", "_") +"/" + unpunctuate(page_name.replace(" ", "_"))
						if not os.path.exists(directory):
							os.makedirs(directory)
			
			pg_no += 1
			if pg_no == 2:
				url += "?page=2"
			elif pg_no > 9:
				temp = list(url)
				if temp[-2] == "=":
					temp = temp[:-1]
					temp += str(pg_no)
					url = "".join(temp)
				else:
					temp[-2:] = str(pg_no)
					url = "".join(temp)				
			else:
				temp = list(url)
				temp[-1] = str(pg_no)
				url = "".join(temp)
			cond = page.find("a", {"class" : "paginator-next button secondary"})
		except:
			error_count += 1
			print("Error for ", url)
			cond = False
			
print("Number of errors: ", error_count)
