class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1
    
    def get_score(self):
        if self.score_tied():
            return self.get_tied_score()
        elif self.score_in_advanced_stage():
            return self.get_advanced_stage_score()
        else:
            return self.get_regular_score()
        
    def score_tied(self):
        return self.player1_score == self.player2_score

    def get_tied_score(self):
        score_names = {0: "Love-All",
                        1: "Fifteen-All",
                        2: "Thirty-All",
                        3: "Forty-All"}
        return score_names.get(self.player1_score, "Deuce")
    
    def score_in_advanced_stage(self):
        return self.player1_score >= 4 or self.player2_score >= 4

    def get_advanced_stage_score(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def get_regular_score(self):
        return f"{self.score_to_call(self.player1_score)}-{self.score_to_call(self.player2_score)}"

    def score_to_call(self, score):
        score_calls = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        return score_calls.get(score, "Unknown")