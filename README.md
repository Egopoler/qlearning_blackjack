# Q-Learning Blackjack Agent 🎲🤖

This project demonstrates **Reinforcement Learning (RL)** applied to the classic **Blackjack** game using the **Q-Learning algorithm**.  
It compares a self-learning Q-agent against a traditional **dealer-type strategy** and shows how RL can outperform static decision rules.

---

## 🎯 Project Goal

To train an RL agent capable of learning **optimal Blackjack strategies** by interacting with the environment — making decisions (hit or stick), observing rewards, and improving through experience.

---

## 🧠 Why Reinforcement Learning?

Blackjack is an **environment with stochastic outcomes** — every decision depends on both visible and hidden cards.  
RL is ideal for such problems because it:
- Learns **from interaction** with the environment;
- Adapts to **probabilistic rewards** and uncertain outcomes;
- Finds **policies** that maximize long-term reward, not just short-term gain.

---

## 📘 Q-Learning Overview

**Q-Learning** is an off-policy reinforcement learning algorithm.  
It learns a value function **Q(s, a)** — the expected return of taking action *a* in state *s* and following the optimal policy thereafter.

### 🔢 Update Rule:
$$
Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s, a)]
$$

Where:
- \( $\alpha$ \): Learning rate  
- \( $\gamma$ \): Discount factor  
- \( $r$ \): Reward received after action  
- \( $s'$ \): Next state

---

## ♠️ Blackjack Environment

Each episode simulates one game of Blackjack between the **agent (player)** and the **dealer (environment)**.

### **State Representation**
The state is represented as a tuple:
```
(player_sum, dealer_visible_card, usable_ace, last_card)
```

### **Actions**
- `0`: Stand (stop taking cards)
- `1`: Hit (take one more card)

### **Rewards**
- `+1`: Win  
- `0`: Draw  
- `-1`: Lose

---

## ⚙️ Training Pipeline

```python
def training_pipeline(episodes=300000):
    env = BlackjackEnv()
    agent = QLearningAgent(alpha=0.05, gamma=0.9, epsilon=0.1)
    rewards = train(agent, env, episodes)
    save_agent(agent)
```
The model gradually updates its Q-table based on rewards and transitions observed during play.

---

## 🧩 Evaluation

We compare two strategies:

| Strategy | Description | Avg Reward (example) | Win rate |
|-----------|--------------|---------------------|-----------|
| Dealer-type | Hits until 17 | -0.099 | 44.5 % |
| Q-Learning | Learns optimal play | **-0.007** | 49.6 % |

Over thousands of episodes, the RL agent achieves **~5% improvement** in win rate.

---

## 💾 Saving and Loading the Model

You can save and reuse the learned Q-table:

```python
save_agent(agent, "q_blackjack.pkl")
agent = load_agent("q_blackjack.pkl")
```

This allows resuming training or evaluation without starting over.

---

## 🎮 Visualization Example

```python
display_game(agent, env, episodes=1)
```

This function shows the game progress step-by-step: player cards, dealer’s actions, and final result.

---

## 🧩 File Structure

```
blackjack_rl/
├── blackjack.py        # Environment (BlackjackEnv)
├── agents.py           # QLearningAgent & DealerAgent
├── train.py            # Training loop
├── eval.py             # Evaluation and visualization
├── main.py             # Pipeline orchestration
└── q_blackjack.pkl     # Saved Q-table
```

---

## 🚀 How to Run

1. **Train the agent:**
   ```bash
   python main.py
   ```

2. **Evaluate performance:**
   ```bash
   python pipeline.py
   ```


---

## 🧭 Key Takeaways

✅ Q-Learning allows an agent to learn from trial and error.  
✅ The agent **outperforms heuristic dealer strategies**.  
✅ Even in probabilistic games, RL finds stable strategies over time.  
✅ The model can be saved, reloaded, and extended for larger state spaces.

---

## 🧑‍💻 Author

**Egor Poliakov**  
*Reinforcement Learning Project (2025)*  
AI Researcher / Computer Vision & Machine Learning Engineer

---
