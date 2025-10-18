import numpy as np
from tqdm import tqdm

def evaluate(agent, env, episodes=10000):
    win_games = 0
    lose_games = 0
    draw_games = 0
    total_reward = 0
    for _ in tqdm(range(episodes)):
        state = env.reset()
        while True:
            action = agent.choose_action(state, explore=False)  # always best weights for evaluation
            next_state, reward, done = env.step(action)
            state = next_state
            if done:
                total_reward += reward
                if reward == 1:
                    win_games += 1
                elif reward == -1:
                    lose_games += 1
                else:
                    draw_games += 1
                break
            
            
    avg_reward = total_reward / episodes
    print("statistic with draft: ")
    print(f"win games in %: {win_games/(win_games + lose_games + draw_games)}, lose games in %: {lose_games/(win_games + lose_games + draw_games)}, draw games in %: {draw_games/(win_games + lose_games + draw_games)}")
    print("statistic without draft: ")
    print(f"win games in %: {win_games/(win_games + lose_games)}, lose games in %: {lose_games/(win_games + lose_games)}")
    print(f"======================")
    print(f"avg_reward for {episodes} games: {avg_reward:.3f}")
    
    return avg_reward


def display_game(agent, env, episodes=1):
    for _ in range(episodes):
        state = env.reset()
        
        while True:
            action = agent.choose_action(state, explore=False)
            next_state, reward, done, player, dealer = env.visual_step(action)
            state = next_state
            if done:
                vis_player_score = player[0] + player[1]
                vis_dealer_score = dealer[0]
                print("=== Game Start ===\n")
                print(f"Player cards: {player[0]}, {player[1]}\nscore: {vis_player_score}")
                print("------------------")
                print(f"Dealer visible card: {dealer[0]}\n")
                print("------------------")
                for card in player[2:]:
                    print(f"Player hit one more card: {card}")
                    vis_player_score += card
                    print(f"player score: {vis_player_score}\n")
                if sum(player) > 21:
                    print("LOSE, player over 21")
                    break
                else:
                    print("Player standed")
                    print(f"player score: {sum(player)}\n")
                    
                print("=== Dealer turn ===")
                print(f"Dealer second card: {dealer[1]}")
                vis_dealer_score += dealer[1]
                print(f"dealer score: {vis_dealer_score}\n")
                for card in dealer[2:]:
                    print(f"Dealer hit one more card: {card}")
                    vis_dealer_score += card
                    print(f"dealer score: {vis_dealer_score}\n")
                    
                if reward == 1:
                    print("WIN!")
                elif reward == -1:
                    print("LOSE")
                else:
                    print("DRAW")
                print("\n==================")
                break
