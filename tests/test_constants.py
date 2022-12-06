import sys

sys.path.append("..")

from dependencies.function import *

cs = Location(lat=48.706473, lng=2.192173)

acco = Gadjo(name="Acco", location=cs)
forget = Gadjo(name="Acco", location=cs)
lesbre = Gadjo(name="Acco", location=cs)
chay = Gadjo(name="Chay", location=Location(lat=48.861585, lng=2.278124))
ad = Gadjo(name="Ad", location=Location(lat=48.893686, lng=2.353941))  # urban lab
octax = Gadjo(name="Octax", location=Location(lat=48.845054, lng=2.428713))  # vincennes
alban = Gadjo(name="albanus", location=Location(lat=48.871552, lng=2.357616))
poups = Gadjo(name="poups", location=Location(lat=48.865576, lng=2.310270))
la_touille = Gadjo(name="Guigui", location=Location(lat=48.857701, lng=2.328003))
cz = Gadjo(
    name="Zagarriga", location=Location(lat=48.827840, lng=2.327778)
)  # 81 rue d'alesia
txo = Gadjo(
    name="Txo", location=Location(lat=48.872307, lng=2.363342)
)  # 56 rue de lancry
mout = Gadjo(name="Mout", location=Location(lat=48.843575, lng=2.233364))  # boulbi
lance = Gadjo(name="Lance", location=Location(lat=48.846260, lng=2.234209))  # boulbi

team = GadjosTeam(gadjos=[ad, octax, txo, cz, mout, chay, lance, mout])
