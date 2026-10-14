from pydantic import BaseModel, computed_field


class Player(BaseModel):
    id: int
    season: str
    name: str
    age: int | None = None
    team: str
    position: str
    games_played: int
    pts: float
    reb: float
    ast: float
    stl: float
    blk: float
    tov: float
    three_pm: float
    fgm: float
    fga: float
    ftm: float
    fta: float



    @computed_field
    @property
    def fg_pct(self) -> float:
        return (self.fgm/self.fga) * 100 if self.fga else 0.0

    @computed_field
    @property
    def ft_pct(self) -> float:
        return (self.ftm/self.fta) * 100 if self.fta else 0.0