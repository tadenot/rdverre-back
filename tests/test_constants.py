import sys

sys.path.append("..")

from app.dependencies.function import *

chay = Gadjo(name="Chay", location=Location(address="18 rue de navarin, Paris"))
poops = Gadjo(name="Ad", location=Location(address="12 avenue Jean Jaures, Versailles"))
debs = Gadjo(name="Ad", location=Location(address="porte dauphine"))
forget = Gadjo(
    name="Ad", location=Location(address="1 rue Juliot Curie, Gif-sur-Yvette")
)
lesbre = Gadjo(name="Ad", location=Location(address="2e arrondissement"))
ad = Gadjo(name="Ad", location=Location(address="56 rue de Turenne, Paris"))
ad = Gadjo(name="Ad", location=Location(address="56 rue de Turenne, Paris"))
ad = Gadjo(name="Ad", location=Location(address="56 rue de Turenne, Paris"))
team = GadjosTeam(gadjos=[chay, debs, lesbre, ad])
