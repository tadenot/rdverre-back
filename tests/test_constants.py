import sys
sys.path.append("..")

from app.dependencies.function import *

chay = Gadjo(name="Chay", location=Location(address="70 rue de la Tour, Paris"))
ad = Gadjo(name="Ad", location=Location(address="56 rue de Turenne, Paris"))
team = GadjosTeam(gadjos=[chay, ad])
