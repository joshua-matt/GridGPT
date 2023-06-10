from agent import Agent
from environment import Environment

env = Environment(10, agent_start=[0,0])
agent = Agent(goal_state=(4,3))


for i in range(10):
    action = agent.policy(env.get_state())
    env.step(action.lower())
    print(action.strip().lower(), env.get_state())
