# Hoopsmith

Fantasy basketball analytics: player rankings, roster analysis, and trade tools.

## Planned features
- Player rankings based on customizable scoring categories
- Roster strength and weakness analysis, with CSV roster import
- Trade analyzer and waiver recommendations
- AI assistant that answers questions using the app's own analytics

## Tech stack
Next.js and TypeScript, FastAPI (Python), PostgreSQL

## Run locally

**Backend**
```
cd backend
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Serves http://localhost:8000. API docs are at `/docs`.

**Frontend** (backend must be running)
```
cd frontend
npm install
npm run dev
```
Serves http://localhost:3000.

## Status
In early development. Done so far: player model, player API, and a player table.

See [docs/decisions.md](docs/decisions.md) for design decisions.
