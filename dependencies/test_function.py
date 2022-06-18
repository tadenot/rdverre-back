from function import *


def main():
    chay = Gadjo("Chay", Location(48.861838, 2.278190))
    ad = Gadjo("Ad", Location(48.856222, 2.364736))

    team = GadjosTeam([chay, ad])
    print(team.distance_center().lat)
    print(team.distance_center().lng)


if __name__ == "__main__":
    main()
