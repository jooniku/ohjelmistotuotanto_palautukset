class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_advantage(self):
        advantage = {1: "Advantage player1", -1: "Advantage player2", 2: "Win for player1", -2: "Win for player2"}
        diff = self.player1_score - self.player2_score
        score_diff = self.limit_value_to_range(diff, range(-2, 3))
        return advantage[score_diff]
    
    def limit_value_to_range(self, value, range):
        """Remember that range(-2, 2) means -2 -> 1.
        """
        if value < min(range): return min(range)
        if value > max(range): return max(range)
        return value

    def get_same_score(self):
        same_scores = {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All"}
        return same_scores.get(self.player1_score, "Deuce")

    def get_uneven_score(self, player):
        """Player is string of player1/player2
        """
        player_scores = {self.player1_name: self.player1_score, self.player2_name: self.player2_score}
        score_names = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        return score_names[player_scores[player]]


    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.get_same_score()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.get_advantage()
        
        else:
            player1 = self.get_uneven_score(self.player1_name)
            player2 = self.get_uneven_score(self.player2_name)
            return f"{player1}-{player2}"

