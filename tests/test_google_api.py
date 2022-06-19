from pprint import pprint
import sys

sys.path.append("..")

from dependencies.google_api import *
from .test_constants import *


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
