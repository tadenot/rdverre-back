from typing import List, Tuple
import h3
import numpy as np
from pprint import pprint
from tqdm import tqdm
import json

from parameters import *
import google_api as google


class Location:
    def __init__(self, lat: float, lng: float) -> None:
        self.lat = lat
        self.lng = lng

    def to_string(self):
        return f"{self.lat},{self.lng}"


class Gadjo:
    def __init__(self, name: str, location: Location) -> None:
        self.name = name
        self.location = location


class GadjosTeam:
    def __init__(self, gadjos: List[Gadjo]) -> None:
        self.gadjos = gadjos

    def distance_center(self) -> Location:
        x_avg = 0
        y_avg = 0
        z_avg = 0
        for gadjo in self.gadjos:
            lat_rad = gadjo.location.lat * np.pi / 180
            lng_rad = gadjo.location.lng * np.pi / 180
            x_avg += np.cos(lat_rad) * np.cos(lng_rad)
            y_avg += np.cos(lat_rad) * np.sin(lng_rad)
            z_avg += np.sin(lat_rad)

        x_avg /= len(self.gadjos)
        y_avg /= len(self.gadjos)
        z_avg /= len(self.gadjos)

        lng_avg = np.arctan2(y_avg, x_avg)
        hyp_avg = np.sqrt(x_avg * x_avg + y_avg * y_avg)
        lat_avg = np.arctan2(z_avg, hyp_avg)

        return Location(lat_avg * 180 / np.pi, lng_avg * 180 / np.pi)

    def score_meet_up(self, meet_up: Location) -> float:
        distance_matrix = google.distance_matrix(
            [meet_up], [gadjo.location for gadjo in self.gadjos]
        )
        scores = []
        for row in distance_matrix["rows"]:
            try:
                scores.append(int(row["elements"][0]["duration"]["value"]))
            except KeyError:
                print(row)
                pass
        if len(scores) == 0:
            return np.inf
        return sum(scores) / len(self.gadjos) + ALPHA * (max(scores) - min(scores))

    def find_best_meet_up1(self) -> Tuple[Location, float]:
        distance_center = self.distance_center()
        best_hex = h3.geo_to_h3(
            distance_center.lat, distance_center.lng, H3_RESOLUTION_END
        )
        viewed_hexagons = {best_hex: self.score_meet_up(distance_center)}

        local_minimum_found = False
        while not local_minimum_found:
            local_minimum_found = True
            hex_ring = h3.k_ring(best_hex, 3)
            for hex in hex_ring:
                hex_score = viewed_hexagons.get(hex)
                if not hex_score:
                    hex_score = self.score_meet_up(Location(*h3.h3_to_geo(hex)))
                    viewed_hexagons[hex] = hex_score
                if hex_score < viewed_hexagons[best_hex]:
                    best_hex = hex
                    local_minimum_found = False

        with open("rdverre_scores.json", "w") as f:
            json.dump(viewed_hexagons, f)
        return Location(*h3.h3_to_geo(best_hex)), viewed_hexagons[best_hex]

    def find_best_meet_up2(self) -> Tuple[Location, float]:
        distance_center = self.distance_center()
        center_hex = h3.geo_to_h3(
            distance_center.lat, distance_center.lng, H3_RESOLUTION_END
        )
        viewed_hexagons = {}
        for hex in tqdm(h3.k_ring(center_hex, 20)):
            viewed_hexagons[hex] = self.score_meet_up(Location(*h3.h3_to_geo(hex)))
        with open("rdverre_scores.json", "w") as f:
            json.dump(viewed_hexagons, f)
        best_hex = min(viewed_hexagons, key=viewed_hexagons.get)
        return Location(*h3.h3_to_geo(best_hex)), viewed_hexagons[best_hex]

    def find_best_meet_up3(self) -> Tuple[Location, float]:
        distance_center = self.distance_center()
        center_hex = h3.geo_to_h3(
            distance_center.lat, distance_center.lng, H3_RESOLUTION_START
        )
        viewed_hexagons = {}
        for res in tqdm(range(H3_RESOLUTION_START + 1, H3_RESOLUTION_END + 1)):
            hexagons_to_explore = h3.h3_to_children(center_hex, res)
            best_score = np.inf
            best_hex = next(iter(hexagons_to_explore))
            for hex in hexagons_to_explore:
                hex_score = self.score_meet_up(Location(*h3.h3_to_geo(hex)))
                viewed_hexagons[hex] = hex_score
                if hex_score < best_score:
                    best_score = hex_score
                    best_hex = hex
            center_hex = best_hex

        with open("rdverre_scores.json", "w") as f:
            json.dump(viewed_hexagons, f)
        return Location(*h3.h3_to_geo(best_hex)), best_score
