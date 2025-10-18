import numpy as np
from tqdm import tqdm

def train(agent, env, episodes=100000):
    rewards = []
    for ep in tqdm(range(episodes)):
        state = env.reset()
        total_reward = 0

        while True:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.update(state, action, reward, next_state, done)
            state = next_state
            total_reward += reward
            if done:
                break

        rewards.append(total_reward)

        # for logging
        if (ep + 1) % 10000000 == 0:
            avg_reward = np.mean(rewards[-10000:])
            tqdm.write(f"Episode {ep+1}, avg_reward={avg_reward:.3f}")

    return rewards


