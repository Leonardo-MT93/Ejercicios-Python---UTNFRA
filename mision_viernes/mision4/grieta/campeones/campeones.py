from .kamille import kamille_stats
from .lux import lux_stats
from .tresh import tresh_stats

def mostrar_atributos(campeon):
    match campeon:
        case "Trish":
            return tresh_stats
        case "Kamille":
            return kamille_stats
        case "Lux":
            return lux_stats

              
