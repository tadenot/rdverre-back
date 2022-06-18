from function import *
from constants import *


def main():
    # Test distance_center
    distance_center = team.distance_center()
    print(distance_center.lat)
    print(distance_center.lng)

    # Test score meet up
    score = team.score_meet_up(distance_center)
    print(score)


if __name__ == "__main__":
    main()
