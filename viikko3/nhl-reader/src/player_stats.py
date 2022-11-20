class PlayerStats:
    def __init__(self, reader):
        self.reader = reader.players

    def top_scorers_by_nationality(self, nationality):
        filteredList = list(filter(lambda player: player.nationality == nationality, self.reader))
        sortedList = sorted(filteredList, key=lambda player: player.points, reverse=True)
        return sortedList

