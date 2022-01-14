def direction(facing, turn):
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    index = directions.index(facing)
    steps = turn / 45
    
    if steps < 0:
        return directions[int((index + steps) % 8)]
    else:
        return directions[int((index + steps) % 8)]