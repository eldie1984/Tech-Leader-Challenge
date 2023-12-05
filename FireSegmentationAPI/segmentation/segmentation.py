from utils.geodesic_distance import geodesic_distance
from datetime import datetime
import logging

def segmentacionDeIncendios(fuegos: list[dict], d: float=10, t: float=60) -> tuple[int,list[list[str]]]:
    """
    This function segments fires based on geodesic distance and time.
    It returns a tuple containing the number of fire segments and a list of fire segments.
    Each fire segment is a list of fire IDs.
    """
    # Initialize the list of fire segments with the first fire
    fire_segments = [[fuegos[0]['id']]]
    for i in range(1, len(fuegos)):
        # Calculate the geodesic distance and time difference to the last fire in the current segment
        distance = euclidean_distance((fuegos[i-1]['x'], fuegos[i-1]['y']), (fuegos[i]['x'], fuegos[i]['y']))
        time_difference = (datetime.fromisoformat(fuegos[i]['id'].strip()[:16]) - datetime.fromisoformat(fuegos[i-1]['id'].strip()[:16])).total_seconds() / 60

        # If the distance or time difference is too large, start a new fire segment
        if distance > d or time_difference > t:
            fire_segments.append([fuegos[i]['id']])
        else:
            # Otherwise, add the fire to the current segment
            fire_segments[-1].append(fuegos[i]['id'])

    return len(fire_segments), fire_segments