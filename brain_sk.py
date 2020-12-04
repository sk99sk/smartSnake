import parameters
import numpy as np

class brain:
    def __init__(self,set_random_para = True):

        self.outputs = []
        self.weights = []
        self.bias = []
        if set_random_para:
            for i in range(len(parameters.nn_structure) - 1):
                theta = np.random.uniform(low=-0.5, high=0.5, size=(parameters.nn_structure[i], parameters.nn_structure[i+1]))
                self.weights.append(theta)

            for i in range(len(parameters.nn_structure) - 1):
                base = np.random.uniform(low=-0.5, high=0.5, size=(1, parameters.nn_structure[i+1]))
                self.bias.append(base)
                

    def look_up_in_dir(self,snake,food,dir_x,dir_y,):
        food_x= food.pos[0]
        food_y=food.pos[1]
        head_x=snake.head.pos[0]
        head_y=snake.head.pos[1]
        #food, body and boundary distance
        input = [0,0,0]
        food_found = False
        body_found = False
        distance = 0
        while (head_x>0 and head_x<parameters.num_cols and head_y>0 and head_y<parameters.num_rows):
            head_x = head_x + dir_x
            head_y = head_y + dir_y
            distance+=1
            if (not food_found and food_x==head_x and food_y==head_y):
                food_found = True
                input[0] = 1

            if not body_found:
                for cube in self.snake.body:
                    if cube.pos[0] == head_x and cube.pos[1]== head_y:
                        body_found == True
                        input[1] = 1/distance

        input[2] = 1/distance
        return input



    def four_to_three_dir(self,snake,food,i):
        if snake.head.dir_x==0 and snake.head.dir_y==-1:
            # 0 deg
            if i==0:
                return 0,-1
            # 45 deg rt
            elif i==1:
                return 1,-1
            # 90 deg rt
            elif i==2:
                return 1,0
            #135 deg rt
            elif i==3:
                return 1,1
            #180 deg
            elif i==4:
                return 0,1
            # 135 deg lt
            elif i==5:
                return -1,1
            #90 deg lt
            elif i==6:
                return -1,0
            #45 deg lt
            elif i==7:
                return -1,-1
        elif snake.head.dir_x==1 and snake.head.dir_y==0:
            # 0 deg
            if i==0:
                return 1,0
            # 45 deg rt
            elif i==1:
                return 1,1
            # 90 deg rt
            elif i==2:
                return 0,1
            #135 deg rt
            elif i==3:
                return -1,-1
            #180 deg
            elif i==4:
                return -1,0
            # 135 deg lt
            elif i==5:
                return -1,-1
            #90 deg lt
            elif i==6:
                return 0,-1
            #45 deg lt
            elif i==7:
                return 1,-1

        elif snake.head.dir_x==0 and snake.head.dir_y==1:
            # 0 deg
            if i==0:
                return 0,1
            # 45 deg rt
            elif i==1:
                return -1,1
            # 90 deg rt
            elif i==2:
                return -1,0
            #135 deg rt
            elif i==3:
                return -1,-1
            #180 deg
            elif i==4:
                return 0,-1
            # 135 deg lt
            elif i==5:
                return 1,-1
            #90 deg lt
            elif i==6:
                return 1,0
            #45 deg lt
            elif i==7:
                return 1,1

        elif snake.head.dir_x==-1 and snake.head.dir_y==0:
            # 0 deg
            if i==0:
                return -1,0
            # 45 deg rt
            elif i==1:
                return -1,-1
            # 90 deg rt
            elif i==2:
                return 0,-1
            #135 deg rt
            elif i==3:
                return 1,-1
            #180 deg
            elif i==4:
                return 1,0
            # 135 deg lt
            elif i==5:
                return 1,1
            #90 deg lt
            elif i==6:
                return 0,1
            #45 deg lt
            elif i==7:
                return -1,1


# direction in input are in clockwise order

    def make_input(self,snake,food):
        input = []

        for i in range(8):
            dirx,diry = self.four_to_three_dir(snake,food,i)
            temp = self.look_up_in_dir(snake,food,dirx,diry)
            input.extend(temp)
        return input



    def relu(self,arr):
        return arr*(arr>0)

    def softmax(self,mat):
        mat = mat - np.max(mat)
        return np.exp(mat) / np.sum(np.exp(mat), axis=1)      


    def give_decision(self,snake,food):
        self.snake = snake
        self.food = food
        ip = self.make_input(snake,food)
        input = np.array(ip)
        #print("input is ",ip)
        temp_pre_op = input
        for i in range(len(self.weights)-1):
            temp_intermediate_op = self.relu(np.dot(temp_pre_op,self.weights[i])+self.bias[i])
            self.outputs.append(temp_intermediate_op)
            temp_pre_op = temp_intermediate_op
        self.outputs.append(self.softmax(np.dot(temp_pre_op, self.weights[i+1]) + self.bias[i+1]))
        return np.argmax(self.outputs[-1]) + 1
