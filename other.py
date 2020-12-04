import sys
import pygame
import parameters
import random
def key_pressed():

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			


def gen_ran_pos(snake):
	pos_occ = snake.body
	while True:
		x = random.randrange(parameters.num_cols-1)
		y = random.randrange(parameters.num_rows-1)
		if len(list(filter(lambda z:z.pos == (x,y),pos_occ))) > 0:
			continue
		if (x==0 or x==parameters.num_cols-1 or y==0 or y==parameters.num_rows-1):
			continue
		else:
			break
	return (x,y)

def redraw_win(win,snake,food,board):
	new_win = board.board_draw(win)
	new_win = snake.draw(new_win)
	new_win = food.draw(new_win)
	pygame.display.update()

