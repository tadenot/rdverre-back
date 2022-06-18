from google_api import *
from constants import *
from pprint import pprint


def main():
    pprint(
        distance_matrix(
            [team.distance_center()],
            [chay.location, ad.location],
        )
    )
    pass


if __name__ == "__main__":
    main()
