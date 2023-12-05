from utils.geodesic_distance import geodesic_distance
from datetime import datetime
import logging

def segmentacionDeIncendios(fuegos: list[dict], d: float, t: float) -> tuple[int,list[list[str]]]:
    """
    This function segments fires based on geodesic distance and time.
    It returns a tuple containing the number of fire segments and a list of fire segments.
    Each fire segment is a list of fire IDs.
    """
    # Initialize the list of fire segments with the first fire
    fire_segments = [[fuegos[0]['id']]]
    for i in range(1, len(fuegos)):
        # Calculate the geodesic distance and time difference to the last fire in the current segment
        distance = geodesic_distance((fuegos[i-1]['x'], fuegos[i-1]['y']), (fuegos[i]['x'], fuegos[i]['y']))
        time_difference = (datetime.fromisoformat(fuegos[i]['time']) - datetime.fromisoformat(fuegos[i-1]['time'])).total_seconds() / 60

        # If the distance or time difference is too large, start a new fire segment
        if distance > d or time_difference > t:
            fire_segments.append([fuegos[i]['id']])
        else:
            # Otherwise, add the fire to the current segment
            fire_segments[-1].append(fuegos[i]['id'])

    return len(fire_segments), fire_segments


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
 
ejemplo()