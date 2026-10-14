from fastapi import FastAPI, HTTPException

from .models import Player
from .sources import MockPlayerSource, PlayerSource


app = FastAPI(title = "HoopsmithAPI")


source: PlayerSource = MockPlayerSource()

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/players/{player_id}", response_model=Player)
def get_player(player_id: int):

    players = source.get_players()
    for player in players:
        if player.id == player_id:
            return player

    raise HTTPException(status_code = 404, detail = "Player not found")


@app.get("/api/players", response_model=list[Player])
def list_players():
    return source.get_players()

    
