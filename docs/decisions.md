# Design Decisions


## Stored season totals, derived per-game stats
The `Player` model stores season totals (points, rebounds, made and attempted shots). Per-game stats and shooting percentages are computed fields.
Per-game averages are rounded, so storing them loses precision permanently. Totals are exact and per-game can be recomputed at any precision.
Every per-game value needs a computed field, and the API response is larger.

## Shooting percentages are 0-100
FG% and FT% are computed from made and attempted shots on a 0-100 scale, so any data source that reports fractions needs a conversion in its mapping step.

## Stats are keyed by player id plus season
A player keeps one id across seasons, and each season's stats are a separate row keyed by id plus season, so last season's and this season's numbers can sit side by side without overwriting each other.

## Age is optional
Not every stats source provides age and it doesn't affect category rankings, so it defaults to null and nothing breaks without it.

## PlayerSource is a Protocol
The API depends only on a `get_players()` contract, so I can swap the mock file for a CSV, Postgres, or `nba_api` source by changing one line.

## Server-side fetch inside Suspense
The frontend fetches players on the server and wraps that in `<Suspense>`, because Next.js 16 Cache Components rejects uncached data outside a Suspense boundary.

## Availability is a separate record
Whether a player is free, on my team, or taken belongs to my league and changes weekly, so it lives apart from the season stats rows that ingestion rewrites.
