import type { Player } from "../lib/types";

const columns: { label: string; value: (p: Player) => string }[] = [
  { label: "GP", value: (p) => String(p.games_played) },
  { label: "PTS", value: (p) => p.pts_per_game.toFixed(1) },
  { label: "REB", value: (p) => p.reb_per_game.toFixed(1) },
  { label: "AST", value: (p) => p.ast_per_game.toFixed(1) },
  { label: "STL", value: (p) => p.stl_per_game.toFixed(1) },
  { label: "BLK", value: (p) => p.blk_per_game.toFixed(1) },
  { label: "TO", value: (p) => p.tov_per_game.toFixed(1) },
  { label: "3PM", value: (p) => p.three_pm_per_game.toFixed(1) },
  { label: "FG%", value: (p) => p.fg_pct.toFixed(1) },
  { label: "FT%", value: (p) => p.ft_pct.toFixed(1) },
];

export default function PlayerTable({ players }: { players: Player[] }) {
  return (
    <div className="overflow-x-auto rounded-xl border border-zinc-200 bg-white shadow-sm dark:border-zinc-800 dark:bg-zinc-950">
      <table className="w-full text-sm">
        <thead>
          <tr className="border-b border-zinc-200 bg-zinc-50 text-xs uppercase tracking-wide text-zinc-500 dark:border-zinc-800 dark:bg-zinc-900 dark:text-zinc-400">
            <th className="px-4 py-3 text-left font-medium">Player</th>
            {columns.map((c) => (
              <th key={c.label} className="px-3 py-3 text-right font-medium">
                {c.label}
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="divide-y divide-zinc-100 dark:divide-zinc-900">
          {players.map((p) => (
            <tr
              key={p.id}
              className="transition-colors hover:bg-zinc-50 dark:hover:bg-zinc-900"
            >
              <td className="px-4 py-3">
                <div className="font-medium text-zinc-900 dark:text-zinc-50">
                  {p.name}
                </div>
                <div className="text-xs text-zinc-500 dark:text-zinc-400">
                  {p.team} · {p.position}
                </div>
              </td>
              {columns.map((c) => (
                <td
                  key={c.label}
                  className="px-3 py-3 text-right tabular-nums text-zinc-700 dark:text-zinc-300"
                >
                  {c.value(p)}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}