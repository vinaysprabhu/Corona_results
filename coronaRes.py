import cherrypy
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import os
import json
import os.path
import numpy as np 
import matplotlib.pyplot as plt
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

class HelloWorld(object):
	@cherrypy.expose
	def index(self):
		extract_contents = lambda row: [x.text.replace('\n','') for x in row]
		URL = 'https://www.mohfw.gov.in/'
		SHORT_HEADERS = ['SNo', 'State','Indian-confirmed','foriegn-confirmed', 'Cured', 'Death']
		response = requests.get(URL).content
		print(response)
		soup =BeautifulSoup(response, 'html.parser')
		print(soup)
		header = extract_contents(soup.tr.find_all('th'))

		stats= []
		all_rows = soup.find_all('tr')

		for row in all_rows:
			stat = extract_contents(row.find_all('td'))
			if stat:
				if len(stat) == 5:
					#last row
					stat = ['', *stat]
					stats.append(stat)
				elif len(stat) ==6:
					stats.append(stat)
		stats[-1][1] = "Total Cases"
		stats.remove(stats[-1])

		objects = []
		for row in stats:
			objects.append(row[1])

		y_pos = np.arange(len(objects))

		performance = []
		for row in stats:
			performance.append(int(row[2])+int(row[3]))
		table = tabulate(stats,headers = SHORT_HEADERS)
		print(table)
		tmpl = env.get_template('index.html')
		return tmpl.render(list=json.dumps(stats))
if __name__ == '__main__':
	configfile = os.path.join(os.path.dirname(__file__),'server.conf')
	cherrypy.config.update({
	    'server.socket_host':'0.0.0.0',
	    'server.socket_port': os.environ.get('PORT', '5000'), # default port is 8080 you can chage default port number here
	})
	cherrypy.quickstart(HelloWorld(),config=configfile)
