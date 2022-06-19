from typing import Tuple
from fastapi import FastAPI
import sys

sys.path.append("..")

from dependencies.function import GadjosTeam, Location

app = FastAPI()


@app.get("/best-meet-up/")
async def best_meet_up(team: GadjosTeam) -> Tuple[Location, float]:
    return team.find_best_meet_up1()
