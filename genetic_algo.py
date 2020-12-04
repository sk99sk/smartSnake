import snake
import parameters
import board
import cube
import brain_sk
import time
import other
import random
import pickle

def run(snakes,arena):
    seed = random.random()
    for s in snakes:
        temp_start_time = time.time()
        temp_loop_check = False
        random.seed(seed)
        food = cube.cube(other.gen_ran_pos(s),parameters.food_color)
        while s.is_alive:
            result = s.mind.give_decision(s,food)
            s.four_to_three_ip_turn(result)
            s.move()
        
########## Check if to kill snake as time or steps exceeded############
            #check for loop
            if s.steps_taken > 250:
                if not temp_loop_check:
                    temp_loop_check = True
                    any_point_in_path = s.head.pos
                    times = 0
                elif s.head.pos==any_point_in_path:
                    times+=1
                if times>2:
                    s.kill()


            #check if time exceeded
            if time.time()-temp_start_time > 0.1:
                s.kill()

##############################################################


            #if snake ate food
            if (s.head.pos==food.pos):
                s.add_cube()
                s.steps_taken = 0
                food = cube.cube(other.gen_ran_pos(s),parameters.food_color)
                temp_start_time = time.time()






# mutating the children
def mutate_children(children):
    for child in children:
        for weight in child.mind.weights:
            for ele in range(int(weight.shape[0]*weight.shape[1]*parameters.mutation_percent/100)):
                row = random.randint(0, weight.shape[0]-1)
                col = random.randint(0, weight.shape[1]-1)
                weight[row, col] += random.uniform(-parameters.mutation_intensity, parameters.mutation_intensity)
    return children


# generating children based on the parents passed
def generate_children(parents, no_of_children):
    all_children = []
    for count in range(no_of_children):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        child = snake.snake()
        for i in range(len(parent1.mind.weights)):
            for j in range(parent1.mind.weights[i].shape[0]):
                for k in range(parent1.mind.weights[i].shape[1]):
                    child.mind.weights[i][j, k] = random.choice(
                        [parent1.mind.weights[i][j, k], parent2.mind.weights[i][j, k]])
            for j in range(parent1.mind.bias[i].shape[1]):
                child.mind.bias[i][0, j] = random.choice(
                    [parent1.mind.bias[i][0, j], parent2.mind.bias[i][0, j]])
        all_children.append(child)
    return all_children





def create_new_population(snakes):
    parents = []
    top_old_parents = int(parameters.population_size * parameters.per_of_best_old_pop / 100)
    bottom_old_parents = int(parameters.population_size * parameters.per_of_worst_old_pop / 100)
    #print("top old parents are: ",top_old_parents,"bottom old parents are: ",bottom_old_parents)
    for i in range(top_old_parents):
        #print("Running loop to select top snakes")
        parent = snake.snake(set_random_para=False)
        parent.mind.weights = snakes[i].mind.weights
        parent.mind.bias = snakes[i].mind.bias
        parents.append(parent)
    for i in range(parameters.population_size - 1, parameters.population_size - bottom_old_parents - 1, -1):
        #print("running loop to select bottom snakes")
        parent = snake.snake(set_random_para=False)
        parent.mind.weights = snakes[i].mind.weights
        parent.mind.bias = snakes[i].mind.bias
        parents.append(parent)
    # generating children of top x% and bottom y%
    children = generate_children(parents, parameters.population_size - (top_old_parents + bottom_old_parents))
    # mutating children
    children = mutate_children(children)
    # joining parents and children to make new population
    parents.extend(children)
    return parents



def save_top_snakes(top_snakes):
    file_name = "top_snakes"
    f = open(file_name,'wb')
    pickle.dump(top_snakes,f)
    f.close()



def main():

    top_snakes = []
    snakes = []
    for i in range(parameters.population_size):
        snakes.append(snake.snake())


    arena = board.board()
    for i in range(parameters.num_gen):

        
        print("Generation :",i+1)
        run(snakes,arena)
        snakes.sort(key=lambda x:(len(x.body),-x.steps_taken),reverse=True)
        top_snakes.append(snakes[0])
        print("best snake of gen is: ",len(snakes[0].body)-3)


        snakes = create_new_population(snakes)
    
    for snake_ in top_snakes:
        snake_.reset()
    save_top_snakes(top_snakes)
    
    
#main()    
    
    
