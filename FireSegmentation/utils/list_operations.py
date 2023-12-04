import logging
def addFireToList(fires:list,  fuego:str,new_fuego:str) -> list:
    add_fire=False
    for a_fire in fires:
        if fuego in a_fire and new_fuego not in a_fire:
            logging.info('add fire to list {}'.format(new_fuego))
            a_fire.append(new_fuego)
            add_fire=True
            break
        elif new_fuego  in a_fire:
            add_fire=True
            break         
    if not add_fire:
        logging.info('add fire {}'.format(new_fuego))
        fires.append([new_fuego])
    return fires