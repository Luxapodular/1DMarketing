import random
import pointlists

def choosePixel(minute):
    if minute in [0,1]:
        return random.choice(pointlists.list023)
    elif minute in [2]:
        return random.choice(pointlists.list223)
    elif minute in [3]:
        return random.choice(pointlists.list323)
    elif minute in [4,5,6]:
        return random.choice(pointlists.list423)
    elif minute in [7]:
        return random.choice(pointlists.list723)
    elif minute in [8,9]:
        return random.choice(pointlists.list823)
        
    