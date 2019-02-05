from csv import reader
from bs4 import BeautifulSoup
import requests

class BasketballIndex():
	def __init__(self, link):
		self.link = link

	def page_parser(self, url):
		link = self.link + ''.join(url)
		page = requests.get(link)
		soup = BeautifulSoup(page.text, "html.parser")

		return soup

	def make_list(self, file):
		player_list = []

		with open(file) as f:
			csv_reader = reader(f)
			for row in csv_reader:
				player_list.append(row)

		return player_list

	def player_college_team(self, url):
		soup = self.page_parser(url)
		item_type = soup.find(itemtype="https://schema.org/Person")
		a_tags = []
		for p in item_type.find_all("a"):
			if 'colleges' in p['href']:
				a_tags.append(p.get_text())
		if len(a_tags) > 1:
			return ' & the '.join(a_tags)
		elif len(a_tags) == 0:
			return "did not go to college"
		else:
			return ''.join(a_tags)

	def player_nba_team(self, url):
		soup = self.page_parser(url)
		item_type = soup.find(itemtype="https://schema.org/Person")
		a_tags = []
		for p in item_type.find_all("a"):
			if 'teams' in p['href']:
				a_tags.append(p.get_text())
		if len(a_tags) > 1:
			return ' & the '.join(a_tags)
		elif len(a_tags) == 0:
			return "no team currently"
		else:
			return ''.join(a_tags)

	def player_height(self, url):
		soup = self.page_parser(url)
		item_type = soup.find(itemtype="https://schema.org/Person")
		height_class = item_type.find("span", {"itemprop": "height"})
		height = height_class.get_text()
			
		return height

	def player_number(self, url):
		soup = self.page_parser(url)
		item_type = soup.find(class_="uni_holder bbr")
		number_class = item_type.find("text", {"x": "9", "y": "39", "fill": "#ffffff"})
		if number_class == None:
			number_class = item_type.find("text", {"x": "15", "y": "39", "fill": "#ffffff"})
		player_num = number_class.get_text()

		return player_num

	def player_position(self, url):
		soup = self.page_parser(url)
		item_type = soup.find(itemtype="https://schema.org/Person")
		player_position = ""
		player_team = ""
		sep = '▪'

		for p in item_type.find_all("p"):
			if 'position' in str(p).lower():
				player_position += str(p.text)

		return ' '.join(player_position.split()).split(sep, 1)[0].replace('Position: ', '')




