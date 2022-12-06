from typing import Tuple, List
from fastapi import FastAPI

from app.dependencies.function import GadjosTeam, LatLng, Location
import app.dependencies.google_api as gg

app = FastAPI()


@app.post("/best-meet-up1/")
async def best_meet_up1(team: GadjosTeam) -> Tuple[LatLng, float]:
    return team.find_best_meet_up1()

@app.post("/best-meet-up2/")
async def best_meet_up2(team: GadjosTeam) -> Tuple[LatLng, float]:
    return team.find_best_meet_up2()

@app.post("/best-meet-up3/")
async def best_meet_up3(team: GadjosTeam) -> Tuple[LatLng, float]:
    return team.find_best_meet_up3()

@app.post("/location-autocomplete/")
async def location_autocomplete(address: str) -> List[str]:
    return gg.places_autocomplete(address)
