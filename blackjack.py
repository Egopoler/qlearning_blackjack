import random


class BlackjackEnv:
    def __init__(self):
        self.deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
        self.reset()
        

    def draw_card(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

    def reset(self):
        self.deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
        # player and dealer get two cards
        self.player = [self.draw_card(), self.draw_card()]
        self.dealer = [self.draw_card(), self.draw_card()]
        return self._get_obs()

    def _get_obs(self):
        player_sum = sum(self.player)
        dealer_card = self.dealer[0]  # visible dealer card (at start first card)
        if 1 in self.player:
            usable_ace = 1
        else:
            usable_ace = 0
        last_card = self.player[-1]
        return (player_sum, dealer_card, usable_ace, last_card)

    def step(self, action):
        """
        action = 0 -> stand (stop)
        action = 1 -> hit (take card)
        return: next_state, reward, done
        """
        if action == 1:  # hit card
            self.player.append(self.draw_card())
            
            if 1 in self.player:
                usable_ace = 1
            else:
                usable_ace = 0
                
            last_card = self.player[-1]
            
            if sum(self.player) > 21:  # over 21
                return (sum(self.player), self.dealer[0], usable_ace, last_card), -1, True
            else:
                return (sum(self.player), self.dealer[0], usable_ace, last_card), 0, False

        elif action == 0:  # stop
            # dealer hits until 17
            while sum(self.dealer) < 17:
                self.dealer.append(self.draw_card())

            player_sum = sum(self.player)
            dealer_sum = sum(self.dealer)
            
            if 1 in self.player:
                usable_ace = 1
                if player_sum + 10 <= 21:
                    player_sum += 10
            else:
                usable_ace = 0
                
            last_card = self.player[-1]

            # calculate result
            if dealer_sum > 21 or player_sum > dealer_sum:
                reward = 1
            elif player_sum == dealer_sum:
                reward = 0
            else:
                reward = -1

            return (player_sum, self.dealer[0], usable_ace, last_card), reward, True
        
    def visual_step(self, action):
        """
        this is helper function for display game, technically it is the same as step
        action = 0 -> stand (stop)
        action = 1 -> hit (take card)
        return: next_state, reward, done
        """
        if action == 1:  # take card
            self.player.append(self.draw_card())
            
            if 1 in self.player:
                usable_ace = 1
            else:
                usable_ace = 0
                
            last_card = self.player[-1]
            
            if sum(self.player) > 21:  # over 21
                return (sum(self.player), self.dealer[0], usable_ace, last_card), -1, True, self.player, self.dealer
            else:
                return (sum(self.player), self.dealer[0], usable_ace, last_card), 0, False, self.player, self.dealer

        elif action == 0:  # stop
            # dealer hits until 17
            while sum(self.dealer) < 17:
                self.dealer.append(self.draw_card())

            player_sum = sum(self.player)
            dealer_sum = sum(self.dealer)
            
            if 1 in self.player:
                usable_ace = 1
                if player_sum + 10 <= 21:
                    player_sum += 10
            else:
                usable_ace = 0
                
            last_card = self.player[-1]

            # calculate result
            if dealer_sum > 21 or player_sum > dealer_sum:
                reward = 1
            elif player_sum == dealer_sum:
                reward = 0
            else:
                reward = -1

            return (player_sum, self.dealer[0], usable_ace, last_card), reward, True, self.player, self.dealer
        
