from bs4 import BeautifulSoup
from csv import writer
from time import sleep
from string import ascii_lowercase
import requests

with open("all_bball_players.csv", 'w') as f:
	csv_writer = writer(f)
	csv_writer.writerow(["Player, Position, Link"])


for letter in ascii_lowercase:
	print(f"Now scraping players with last name '{letter.upper()}' ...")
	url = 'https://www.basketball-reference.com/players/' + letter
	page = requests.get(url)
	if page.status_code == 404:
		continue
	soup = BeautifulSoup(page.text, "html.parser")
	table_row = soup.find("tbody")


	with open("all_bball_players.csv", 'a') as file:
		csv_writer = writer(file)
		
		for bold in table_row.find_all("strong"):
			player_url = bold.find("a")["href"]
			player = bold.get_text()
			player_position = bold.find('td', {'td': 'pos'})
			csv_writer.writerow([player, player_position, player_url])
	sleep(3)
