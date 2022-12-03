class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_points += 1
        else:
            self.p2_points += 1

    def get_player_score(self, points):
        player_score = ""
        if points == 0:
            player_score = "Love"
        if points == 1:
            player_score = "Fifteen"
        if points == 2:
            player_score = "Thirty"
        if points == 3:
            player_score = "Forty"
        return player_score

    def check_tie(self):
        if self.p1_points == self.p2_points:
            return True
        return False

    def check_win_condition(self):
        minus_result = self.p1_points - self.p2_points
        advantage = ""

        if minus_result == 1:
            advantage = "Advantage player1"
        elif minus_result == -1:
            advantage = "Advantage player2"
        elif minus_result >= 2:
            advantage = "Win for player1"
        elif minus_result <= -2:
            advantage = "Win for player2"
        else:
            advantage = "Deuce"

        return advantage

    def get_score(self):
        score = ""
        if self.p1_points >= 4 or self.p2_points >= 4:
            score = self.check_win_condition()

        else:
            tie = self.check_tie()
            if tie == True:
                score = self.get_player_score(self.p1_points) + "-" + "All"
            else:
                score = self.get_player_score(self.p1_points) + "-" + self.get_player_score(self.p2_points)

        return score