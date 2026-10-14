from pydantic import BaseModel, computed_field


class Player(BaseModel):
    id: int
    season: str
    name: str
    age: int | None = None
    team: str
    position: str
    games_played: int
    pts: int
    reb: int
    ast: int
    stl: int
    blk: int
    tov: int
    three_pm: int
    fgm: int
    fga: int
    ftm: int
    fta: int



    @computed_field
    @property
    def fg_pct(self) -> float:
        return (self.fgm/self.fga) * 100 if self.fga else 0.0

    @computed_field
    @property
    def ft_pct(self) -> float:
        return (self.ftm/self.fta) * 100 if self.fta else 0.0

    @computed_field
    @property
    def pts_per_game(self) -> float:
        return self.pts / self.games_played if self.games_played else 0.0

    @computed_field
    @property
    def reb_per_game(self) -> float:
        return self.reb / self.games_played if self.games_played else 0.0

    @computed_field
    @property
    def ast_per_game(self) -> float:
        return self.ast / self.games_played if self.games_played else 0.0

    @computed_field
    @property
    def stl_per_game(self) -> float:
        return self.stl / self.games_played if self.games_played else 0.0

    @computed_field
    @property
    def blk_per_game(self) -> float:
        return self.blk / self.games_played if self.games_played else 0.0

    @computed_field
    @property
    def tov_per_game(self) -> float:
        return self.tov / self.games_played if self.games_played else 0.0

    @computed_field
    @property
    def three_pm_per_game(self) -> float:
        return self.three_pm / self.games_played if self.games_played else 0.0

