import gym
import matplotlib.pyplot as plt

env = gym.make("FMUEnv-v0")
observation = env.reset()

observations = []
for _ in range(100):
  action = env.action_space.sample() # your agent here (this takes random actions)
  observation, reward, done, info = env.step(action)
  observations.append(observation)

plt.plot(observations)
plt.show()