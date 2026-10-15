import { Suspense } from "react";
import PlayerTable from "./PlayerTable";
import type { Player } from "../lib/types";

async function getPlayers(): Promise<Player[]> {
  const res = await fetch("http://localhost:8000/api/players", {
    cache: "no-store",
  });

  if (!res.ok) {
    throw new Error(`Failed to fetch players (status ${res.status})`);
  }

  return res.json();
}

async function Players() {
  const players = await getPlayers();
  return <PlayerTable players={players} />;
}

export default function Home() {
  return (
    <main className="mx-auto max-w-6xl px-6 py-12">
      <h1 className="text-3xl font-semibold tracking-tight text-zinc-900 dark:text-zinc-50">
        Hoopsmith
      </h1>
      <p className="mb-8 mt-1 text-zinc-500 dark:text-zinc-400">
        2025-26 season · per-game stats
      </p>
      <Suspense
        fallback={<p className="text-zinc-500 dark:text-zinc-400">Loading players…</p>}
      >
        <Players />
      </Suspense>
    </main>
  );
}