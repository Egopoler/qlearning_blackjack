import random
import numpy as np
import pickle
from collections import defaultdict
from Agents import QLearningAgent, DealerAgent
from blackjack import BlackjackEnv
from train import train
from eval import evaluate, display_game
from pipeline import load_agent

if __name__ == "__main__":
    env = BlackjackEnv()
    agent = load_agent(filename="q_blackjack.pkl")
    display_game(agent, env, 10)
    print("=====")
    print("q agent")
    evaluate(agent, env, 100000)
    print("=====")
    print("dealer agent")
    dealer_agent = DealerAgent()
    evaluate(dealer_agent, env, 100000)