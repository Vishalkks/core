from bs4 import BeautifulSoup
import urllib.request
import glob
import json
import datetime
import os

from stringUtil import is_ascii, punctuate

files = glob.glob('Genre/*')
genre_list = list(map(lambda x:(x.split('/')[1]),files))
error_file = open('error_logs.txt','w+')
artist_file = open('artists_done.txt','w+')
for genre in genre_list:
	artists = glob.glob('Genre/'+genre+'/*')
	artist_list = list(map(lambda x:' '.join((x.split('/')[2]).split('_')),artists))
	for artist in artists:
		if is_ascii(artist):
			for dirpath, dirnames, files in os.walk(artist):
				if not files:		
					artist_new = punctuate(artist.split('/')[2])
					url = "http://lyrics.wikia.com/wiki/"+artist_new
					url = (url.encode('utf-8')).decode()
					
					print(url)
					try:
						content = urllib.request.urlopen(url).read()
						soup = BeautifulSoup(content, 'html.parser')
						lists = soup.find_all("ol")
						for each_list in lists:
							songs = each_list.find_all('a')
							for link in songs:
								song = link.get('title')
								if is_ascii(song):
									print(str(datetime.datetime.now().time()) + "Scraping song "+song)
									(actual_artist,actual_song) = song.split(':')
									lyr = urllib.request.urlopen('https://lorem-ipsum95.herokuapp.com/api/find/'+actual_artist.replace(' ','%20')+'/'+(actual_song.replace('%','%25')).replace(' ','%20')).read()
									data = json.loads(lyr.decode('utf-8'))
									if(data['lyric']):
										new_song_file = open(artist+'/'+actual_song+'.txt','w+')
										new_song_file.write(data['lyric'])
										new_song_file.close()
						
						artist_file.write('Done with '+genre+' '+artist_new)
					except Exception as e: 
						print(str(datetime.datetime.now().time()) + ' : URL '+ url+' gave error ' +str(e))
						error_file.write(str(datetime.datetime.now().time()) + ' : URL '+url+' gave error ' +str(e) )
						
	
error_file.close()
artist_file.close()		
