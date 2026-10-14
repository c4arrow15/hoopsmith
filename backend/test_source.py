from app.sources import MockPlayerSource

players = MockPlayerSource().get_players()
print(len(players), players[0].name, round(players[0].fg_pct, 1))
