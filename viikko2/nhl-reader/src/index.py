import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()
        self.players = []

    def get_players(self):
        """Return a list of player objects.
        """
        for player_dict in self.response:
            player = Player(player_dict)
            self.players.append(player)

        return self.players


class PlayerStats:
    def __init__(self, players):
        self.players = players

    def top_scores_by_nationality(self, nationality):
        """Return a ranked list of players
        from given nationality.
        """

        is_nat = lambda player : player.nationality == nationality
        player_points = lambda player : player.goals + player.assists

        players = filter(is_nat, self.players)
        players = sorted(players, key=player_points, reverse=True)

        return players


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url).get_players()
    stats = PlayerStats(reader)

    nationality = "FIN"
    players = stats.top_scores_by_nationality(nationality)

    print(f"Players from {nationality}", end="\n\n")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
