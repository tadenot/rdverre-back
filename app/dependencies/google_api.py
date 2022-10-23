from dotenv import load_dotenv
import os
import requests

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def distance_matrix(destinations, origins):
    if len(destinations) == 0 or len(origins) == 0:
        return None

    destinations_str = f"{destinations[0].to_string()}"
    for i in range(1, len(destinations)):
        destinations_str += f"|{destinations[i].to_string()}"

    origins_str = f"{origins[0].to_string()}"
    for j in range(1, len(origins)):
        origins_str += f"|{origins[j].to_string()}"

    response = requests.get(
        url="https://maps.googleapis.com/maps/api/distancematrix/json",
        params={
            "destinations": destinations_str,
            "origins": origins_str,
            "mode": "transit",
            "key": GOOGLE_API_KEY,
        },
    )
    if response.status_code != 200:
        print(f"Error {response.status_code}{response.json()}")
    return response.json()
