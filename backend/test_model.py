from app.models import Player

p = Player(
    id=1, season="2025-26", name="Test", team="PHX", position="PG",
    games_played=70, pts=1687, reb=315, ast=574, stl=98, blk=21, tov=217,
    three_pm=224, fgm=602, fga=1302, ftm=259, fta=294
)

print(round(p.fg_pct,1), round(p.ft_pct,1))
print(round(p.pts_per_game, 1), round(p.reb_per_game, 1), round(p.ast_per_game, 1), round(p.three_pm_per_game, 1))
#print(p.model_dump())