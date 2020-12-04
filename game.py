import random
import parameters
import other
import board
import pygame
import snake
import cube
import other
import sys
import brain_sk
import genetic_algo
import pickle
import time

def main():
	while True:
		print("1. Train Snake")
		print("2. Test Snake")
		print("9. End Game")

		opt = int(input())
		if(opt==1):
			genetic_algo.main()
		if(opt==2):
			play_game()
		if(opt==9):
			print("\033c", end="\n")
			break
	sys.exit()


def play_game():


	
	#Loding trained snakes from file
	file = open('top_snakes','rb')
	snakes = pickle.load(file)
	s = snakes[-1]
	file.close()
	
	#initialising board,food and clock
	game_board = board.board()
	food = cube.cube(other.gen_ran_pos(s),parameters.food_color)
	clock = pygame.time.Clock()

	# setup window
	pygame.init()
	win = pygame.display.set_mode((parameters.board_width,parameters.board_height))
	

	# make window
	other.redraw_win(win,s,food,game_board)
	
	while s.is_alive:
		pygame.time.delay(50)
		clock.tick(10)
		
		other.key_pressed()
			
		decision = s.mind.give_decision(s,food)
		s.four_to_three_ip_turn(decision)

		s.move()
		if s.body[0].pos == food.pos:
			s.add_cube()
			food = cube.cube(other.gen_ran_pos(s),parameters.food_color)
			
		other.redraw_win(win,s,food,game_board)

	pygame.display.quit()
	pygame.quit()
	input("press enter to continue..")
main()
