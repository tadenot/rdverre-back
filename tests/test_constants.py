import sys

sys.path.append("..")

from dependencies.function import *

chay = Gadjo("Chay", Location(48.861838, 2.278190))
ad = Gadjo("Ad", Location(48.856222, 2.364736))
team = GadjosTeam([chay, ad])
