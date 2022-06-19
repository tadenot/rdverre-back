from function import *
from test_constants import *


def main():
    # Test distance_center
    distance_center = team.distance_center()
    print(distance_center.lat)
    print(distance_center.lng)

    # Test score meet up
    score = team.score_meet_up(distance_center)
    print(score)

    # Test find best meet up
    best_meet_up, avg_transit_time = team.find_best_meet_up2()
    print(best_meet_up.lat)
    print(best_meet_up.lng)
    print(avg_transit_time / 60)


if __name__ == "__main__":
    main()
