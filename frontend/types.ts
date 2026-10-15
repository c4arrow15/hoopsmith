export type Player = {
  id: number;
  season: string;
  name: string;
  age: number | null;
  team: string;
  position: string;
  games_played: number;

  // season totals
  pts: number;
  reb: number;
  ast: number;
  stl: number;
  blk: number;
  tov: number;
  three_pm: number;
  fgm: number;
  fga: number;
  ftm: number;
  fta: number;

  // computed by the backend
  fg_pct: number;
  ft_pct: number;
  pts_per_game: number;
  reb_per_game: number;
  ast_per_game: number;
  stl_per_game: number;
  blk_per_game: number;
  tov_per_game: number;
  three_pm_per_game: number;
};