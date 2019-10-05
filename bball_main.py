from random import choice
from bball_class import BasketballIndex
from bball_scrape import scap_players
import os

url = 'https://www.basketball-reference.com'
bball = BasketballIndex(url)
csv_path = './all_bball_players.csv'

if not os.path.isfile(csv_path):
	scap_players(csv_path)

player_list = bball.make_list(csv_path)

user_name = input("What's your name? \n")
user_attempts = 6
def choose_player(players):
	return choice(players)


won = False
lost = False
new_player = True

while True:
	if won:
		replay = input("Would you like to play again? (y/n) \n")
		if replay.lower() == 'n':
			print("Thanks for playing!")
			break
		else:
			user_attempts = 5
	elif lost:
		print(f"Sorry, you failed to guess {player}!\n")
		replay = input("Would you like to play again? (y/n)")
		if replay.lower() == 'n':
			print("Thanks for playing!")
			break
		else:
			user_attempts = 5
	else:
		user_attempts = 5

	if new_player == True:
		print(f"{user_name}, you'll be tasked to guess the player...")
		print(f"You'll be given {user_attempts - 1} chances to guess said player...")
		print("If you are unable to guess, you lose...")
		print(f"Good luck, {user_name}!")
	else:
		print(f"Welcome back, {user_name}...")

	player_info = choose_player(player_list)
	url2 = player_info[1]

	player = player_info[0]
	plyr_pos = bball.player_position(url2)
	plyr_colg_team = bball.player_college_team(url2)
	plyr_nba = bball.player_nba_team(url2)
	plyr_height = bball.player_height(url2)
	plyr_num = bball.player_number(url2)

	user_guess = input(f"Who plays/played for {plyr_nba} as a {plyr_pos}? ... \n")


	while True:
		user_attempts -= 1
		if user_guess.lower() != player.lower():
			print(f"Sorry! {user_guess} is not the right answer!\n")
			if user_attempts == 4:
				user_guess = input("Try again.\n")
			elif user_attempts == 3:
				print(f"This player played for {plyr_colg_team}.\n")
				user_guess = input("Try again.\n")
			elif user_attempts == 2:
				print(f"This player is {plyr_height}in. tall.\n")
				user_guess = input("Try again.\n")
			elif user_attempts == 1:
				print(f"This players' number is {plyr_num}.\n")
				user_guess = input("Try again.\n")
			elif user_attempts == 0:
				lost = True
				new_player = False
				break
		else:
			print(f"Congratulations! Thats right!")
			won = True
			break
		



