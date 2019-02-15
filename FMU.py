import math
import gym
from gym import spaces, logger
from gym.utils import seeding
import numpy as np
from pyfmi import load_fmu

class FMUEnv(gym.Env):
    def __init__(self):
        # Init
        self.seed()
        self.timeStep = 0

        # Settings
        self.simulationTime = 500 #Total(maximum) simulation time [s]
        stepTime = 0.05 #Time for each step [s]
        self.ncp = self.simulationTime/stepTime #Calculate NCP for solver according to desired stepTime
        self.maxSteps = 1000
      
        # Loading of FMU file
        self.model = load_fmu('C:\\PathToYourFMU\\YourFMU.fmu')
        self.opts = self.model.simulate_options()

        # Gym interface
        self.action_space = spaces.Box(-10, 10, shape=(1,)) 
        self.observation_space = spaces.Box(np.array([-100, 5, -3.14, -100]),np.array([100, 5, 3.14, 100])) 
        self.state = np.zeros(self.observation_space.shape[0])

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        # Set action
        self.model.set('inputForce', action[0])

        # Step forward         
        self.model.do_step(self.grid[self.timeStep],self.h)
        self.timeStep +=1

        # Retrieve state
        self.state[0] = self.model.get('displacement')[0]
        self.state[1] = self.model.get('velocity')[0]
        self.state[2] = self.model.get('angle')[0] 
        self.state[3] = self.model.get('angularvelocity')[0] 

        # Set your reward function
        reward = 1 #Alternatively, a function of states/observations

        # Declare when environment should terminate
        done =  (self.timeStep == self.maxSteps) or (abs(self.state[2]) > 0.1)

        return np.array(self.state), reward, done, {}

    def reset(self):
        # Reset if model has stepped forward (else error)
        if self.timeStep > 0:
            self.model.reset()

        self.timeStep = 0

        # Inital values to FMU (if neccesary)
        #self.model.set('YourInput', 100)

        # Setup FMU expierment 
        start_time = 0
        self.model.setup_experiment(start_time=start_time, stop_time_defined=False, stop_time=self.simulationTime)
        self.model.initialize()
        self.h = (self.simulationTime-start_time)/self.ncp
        self.grid = np.linspace(start_time,self.simulationTime,self.ncp+1)[:-1]

        # Get your initial states
        self.state[0] = self.model.get('displacement')[0] #Add more states as neccesary
        self.state[1] = self.model.get('velocity')[0] #Add more states as neccesary
        self.state[2] = self.model.get('angle')[0] #Add more states as neccesary
        self.state[3] = self.model.get('angularvelocity')[0] #Add more states as neccesary

        return np.array(self.state,)

   
        