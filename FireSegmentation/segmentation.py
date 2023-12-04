from utils.geodesic_distance import geodesic_distance
from utils.list_operations import addFireToList
from datetime import datetime
import logging

def segmentacionDeIncendios(fuegos: list[dict], d: float, t: float) -> tuple[int,list[list[str]]]:
  # Completar el código en esta funcion
  # Se recomienda modularizar la solucion para hacer más claro el código
  # Se recomienda usar la función "geodesic_distance" del archivo "utils/geodesic_distance.py"

  return (2, [["0", "1", "2"], ["3", "4"]])


def ejemplo():
  # Una vez implementado el testing, se puede eliminar esta funcion.
  # Dejo el codigo acá para poder hacer una prueba rápida
  fuegos: list[dict] = [
    {"id": "0", "x": 0.0, "y": 0.0, "time":"2023-01-01T00:00"},
    {"id": "1", "x": 1.0, "y": 0.0, "time":"2023-01-01T00:00"},
    {"id": "2", "x": 0.0, "y": 1.0, "time":"2023-01-01T00:00"},
    {"id": "3", "x": 10.0, "y": 10.0, "time":"2023-01-01T00:00"},
    {"id": "4", "x": 10.0, "y": 11.0, "time":"2023-01-01T00:00"}
  ]

  d: float = 10.0
  t: float = 60.0

  print(segmentacionDeIncendios(fuegos, d, t))
  print(group_by_distance_and_time(fuegos, d, t))



#function that recieve an ar list of id, x, y and datetime and return all the items grouped by geodesic distance and time between the items
def group_by_distance_and_time(fuegos: list[dict], d: float, t: float) -> list[list[str]]:
    fire=[[fuegos[0]['id']]]
    number_fire=0
    for fuego in fuegos[:-1]:
        logging.debug('a fire {}'.format(fuego))
        for new_fuego in fuegos[number_fire:]:
            logging.debug('a fire between {} and {}'.format(fuego['id'],new_fuego['id']))
            logging.debug('distance {}'.format(geodesic_distance(fuego['x'], fuego['y'], new_fuego['x'], new_fuego['y'])))
            if geodesic_distance(fuego['x'], fuego['y'], new_fuego['x'], new_fuego['y']) <= d and (datetime.strptime(fuego['time'],'%Y-%m-%dT%H:%M') - datetime.strptime(new_fuego['time'],'%Y-%m-%dT%H:%M')).total_seconds() <= t:
                fire=addFireToList(fire,fuego['id'],new_fuego['id'])
        fire=addFireToList(fire,fuego['id'],fuego['id'])
    return (len(fire), fire)

ejemplo()