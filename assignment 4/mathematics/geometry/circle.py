import math

def circumference(radius):
    if radius.isdigit() == False:
        return("input valid number")
    return(2* math.pi *radius)

def area(radius):
    if radius.isdigit() == False:
        return("input valid number")
    return(radius * math.pi *radius)