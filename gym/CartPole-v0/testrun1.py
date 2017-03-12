import gym

env = gym.make('CartPole-v0')

for i_episode in range(20):
	observation = env.reset()  #get that first observation
	for t in range(100):
		env.render()
		print(observation)
		action = env.action_space.sample()
		observation, reward, done, info = env.step(action)  #step func completes an action returns four variables
		if done:
			print("episod finished after {} timesteps" )
			break	
