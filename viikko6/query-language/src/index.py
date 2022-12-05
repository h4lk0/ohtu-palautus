from statistics import Statistics
from player_reader import PlayerReader
from matchers import All, And, HasFewerThan, HasAtLeast, Not, Or, PlaysIn

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )

    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
