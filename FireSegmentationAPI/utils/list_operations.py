import logging

def add_fire_to_list(fires: list[list[str]], fuego: str, new_fuego: str) -> list[list[str]]:
    """
    This function adds a new fire to the list of fires if it's not already present.
    Each fire is a list of strings.
    The function returns the updated list of fires.
    """
    # Check if the new fire is already in the list of fires
    for fire in fires:
        if new_fuego in fire:
            return fires

    # If the new fire is not in the list, add it
    logging.info(f'Adding fire {new_fuego} to list')
    fires.append([new_fuego])
    return fires