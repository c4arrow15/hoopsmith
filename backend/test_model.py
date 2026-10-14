from app.models import Player

p = Player(
    id=1, season="2025-26", name="Test", team="PHX", position="PG",
    games_played=70, pts=20, reb=5, ast=5, stl=1, blk=0.5, tov=2,
    three_pm=2, fgm=7, fga=0, ftm=4, fta=0
)

print(p.fg_pct, p.ft_pct)
print(p.model_dump())