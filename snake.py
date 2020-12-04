import parameters
import cube
import pygame
import brain_sk
import time
class snake:
    def __init__(self,pos=(parameters.snake_start_pos_x,parameters.snake_start_pos_y),set_random_para = True):
        self.body = []
        self.turns = {}
        self.head = cube.cube(pos,parameters.snake_color,eyes=True)
        self.body.append(self.head)
        self.is_alive = True
        self.add_cube()
        self.add_cube()
        self.steps_taken = 0
        self.mind = brain_sk.brain(set_random_para)

		
    def turn_left(self):
        to_move_dir_x = -1
        to_move_dir_y = 0
        self.turns[self.head.pos] = [to_move_dir_x,to_move_dir_y]

    def turn_right(self):
        to_move_dir_x = 1
        to_move_dir_y = 0
        self.turns[self.head.pos] = [to_move_dir_x,to_move_dir_y]

    def turn_up(self):
        to_move_dir_x = 0
        to_move_dir_y = -1
        self.turns[self.head.pos] = [to_move_dir_x,to_move_dir_y]

    def turn_down(self):
        to_move_dir_x = 0
        to_move_dir_y = 1
        self.turns[self.head.pos] = [to_move_dir_x,to_move_dir_y]
    

    def check_and_do_body_crash(self):
        for x in range(len(self.body)):
            if self.body[x].pos in list(map(lambda z:z.pos,self.body[x+1:])):
                #print("body crash")
                #print('Score: ',len(self.body)-3)
                self.is_alive = False
                return True
        return False


    def check_and_do_wall_crash(self):
        for body_cube in self.body:
            if (body_cube.dir_x == -1 and body_cube.pos[0] <= 0)or(body_cube.dir_x == 1 and body_cube.pos[0] > parameters.num_cols-2)or(body_cube.dir_y == 1 and body_cube.pos[1] > parameters.num_rows-2)or(body_cube.dir_y == -1 and body_cube.pos[1] <= 0):
                #print("wall crash")
                #print('Score: ',len(self.body)-3)
                self.is_alive = False
                return True
        return False

    def move(self):	
        for i,body_cube in enumerate(self.body):
            p = body_cube.pos
            if p in self.turns:
                turn  = self.turns[p]
                body_cube.move(turn[0],turn[1])
                self.steps_taken += 1
                if i == len(self.body)-1:
                    self.turns.pop(p)
					


            else:
                body_cube.move(body_cube.dir_x,body_cube.dir_y)
            
            self.steps_taken +=1
            if (self.check_and_do_wall_crash() or self.check_and_do_body_crash()):
                self.kill()
                break
            



		
    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.dir_x, tail.dir_y
 
        if dx == 1 and dy == 0:
            self.body.append(cube.cube((tail.pos[0]-1,tail.pos[1]),parameters.snake_color))
        elif dx == -1 and dy == 0:
            self.body.append(cube.cube((tail.pos[0]+1,tail.pos[1]),parameters.snake_color))
        elif dx == 0 and dy == 1:
            self.body.append(cube.cube((tail.pos[0],tail.pos[1]-1),parameters.snake_color))
        elif dx == 0 and dy == -1:
            self.body.append(cube.cube((tail.pos[0],tail.pos[1]+1),parameters.snake_color))
 
        self.body[-1].dir_x = dx
        self.body[-1].dir_y = dy
		
		
    def draw(self,win):
        new_win = win
        for cube in(self.body):
            new_win = cube.draw(new_win)
        return new_win

    def kill(self):
        self.is_alive = False

        
    def reset(self):
        self.body = []
        self.turns = {}
        pos = (parameters.snake_start_pos_x,parameters.snake_start_pos_y)
        self.head = cube.cube(pos,parameters.snake_color,eyes=True)
        self.body.append(self.head)
        self.is_alive = True
        self.add_cube()
        self.add_cube()
        self.steps_taken = 0


    def four_to_three_ip_turn(self,result):
        # 1 is left
        # 2 is straight
        # 3 is right
        if self.head.dir_x==-1 and self.head.dir_y==0:
            if result==1:
                self.turn_down()
            elif result==2:
                self.turn_left()
            else:
                self.turn_up()
        elif self.head.dir_x==0 and self.head.dir_y==1:
            if result==1:
                self.turn_right()
            elif result==2:
                self.turn_down()
            else:
                self.turn_left()
        elif self.head.dir_x==1 and self.head.dir_y==0:
            if result==1:
                self.turn_up()
            elif result==2:
                self.turn_right()
            else:
                self.turn_down()
        else:
            if result==1:
                self.turn_left()
            elif result==2:
                self.turn_up()
            else:
                self.turn_right()


