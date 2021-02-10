import numpy as np
from dungeon.dungeon import Dungeon


# # Exercise 1 - Modifying the environment
# 
# We will make the problem slightly more complicated.
# 
# The floor is now covered in ice! 
# When an agent makes a movement, it might slip and end up in another cell close to it.
# The probability to arrive in the intended cell is 0.6, and the probability to end up in one of the 4 adjacent cells is 0.1.
# 
# Similar as for Lab 02, you should create a new Dungeon by inheriting from the original Dungeon environment.
# Again, the step method will return the state instead of observations.
# And the step function should incorportate these slippery dynamics.
# 
# When the agent slips, rewards accumulate! You could bang your head on the wall twice...
# 
class IceDungeon(Dungeon):
    
    def __init__(self, N):
        
        super().__init__(N)
        
        # In order to explicitely show that the way you represent states doesn't matter, 
        # we will assign a random index for each coordinate of the grid        
        index_states = np.arange(0, N*N)
        np.random.shuffle(index_states)
        self.actions_dict = {0:"up", 1:"down", 2:"left", 3:"right"}
        self.coord_to_index_state = index_states.reshape(N,N)    
        
    def step(self, action):
        _, reward, done = super().step(action)
        # There is a 40% chance the agent will slip, 
        # and an equal 10% chance for each direction
        # So get a random number 0 - 9 for each possibility
        rnd_no = randrange(0, 9)
        if rnd_no < 4:
            _, reward_slip, done = super().step(self.actions_dict.get(rnd_no))
            reward += reward_slip
        
        state = self.coord_to_index_state[ self.position_agent[0], self.position_agent[1]]
        
        return state, reward, done
    
    def reset(self):
        
        super().reset()
        
        state = self.coord_to_index_state[ self.position_agent[0], self.position_agent[1]]
        
        return state
        