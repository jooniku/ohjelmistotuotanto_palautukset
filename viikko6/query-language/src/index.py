from statistics import Statistics
from player_reader import PlayerReader
from querybuilder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    m = query.playsIn("CHI").build()

    for player in stats.matches(m):
        print(player)

if __name__ == "__main__":
    main()
