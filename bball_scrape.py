from bs4 import BeautifulSoup
from csv import writer
from time import sleep
from string import ascii_lowercase
import requests
from unidecode import unidecode

def scap_players(file_to_save):

	with open(file_to_save, 'w', newline='') as f:
		csv_writer = writer(f)
		csv_writer.writerow(["Player, Position, Link"])


	for letter in ascii_lowercase:
		print(f"Now scraping players with last name '{letter.upper()}' ...")
		url = 'https://www.basketball-reference.com/players/' + letter
		page = requests.get(url)
		
		if page.status_code == 404:
			continue
		
		soup = BeautifulSoup(page.text.encode('utf-8'), "html.parser")
		table_row = soup.find("tbody")

		with open(file_to_save, 'a', newline='') as file:
			csv_writer = writer(file)
			
			for tr in table_row.find_all("tr"):
				player = unidecode(tr.find("th").get_text())
				player_url = tr.find("a")['href']
				position = tr.find("td", {"data-stat":"pos"}).get_text()
				csv_writer.writerow([player, player_url, position])

		sleep(3)
