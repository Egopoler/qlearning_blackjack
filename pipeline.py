import random
import numpy as np
import pickle
from collections import defaultdict
from Agents import QLearningAgent, DealerAgent
from blackjack import BlackjackEnv
from train import train
from eval import evaluate, display_game


def save_agent(agent, filename="q_blackjack1.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(dict(agent.Q), f)
    print(f"model save to {filename}")

def load_agent(filename="q_blackjack1.pkl"):
    with open(filename, "rb") as f:
        data = pickle.load(f)
    agent = QLearningAgent()
    agent.Q = defaultdict(lambda: [0.0, 0.0], data)
    print(f"model loaded from {filename}")
    return agent


def training_pipeline(episodes=100000):
    env = BlackjackEnv()
    agent = QLearningAgent(alpha=0.05, gamma=0.9, epsilon=0.1)
    rewards = train(agent, env, episodes)
    save_agent(agent)
    q_list = []
    for state, actions in agent.Q.items():
        q_list.append((state, actions))
    q_list.sort(key=lambda x: x[0][0])
    for state, actions in q_list:
        print(f"state: {state}, actions: {actions}")
    return rewards

def evaluation_pipeline(episodes=10000, filename="q_blackjack.pkl1"):
    env = BlackjackEnv()
    if filename is None:
        agent = DealerAgent()
    else:
        agent = load_agent(filename=filename)
    avg_reward = evaluate(agent, env, episodes)
    display_game(agent, env, 7)
    return avg_reward


if __name__ == "__main__":
    training_pipeline(300000000)
    qmodel_revard = evaluation_pipeline(100000)
    dealer_model_reward = evaluation_pipeline(100000, filename=None)
    print("qmodel_revard", qmodel_revard)
    print("dealer_model_reward", dealer_model_reward)
    print("qmodel_revard - dealer_model_reward", qmodel_revard - dealer_model_reward)
    
