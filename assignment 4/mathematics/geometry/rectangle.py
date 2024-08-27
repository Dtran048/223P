def perimeter(length, width):
    if length.isdigit() == False or width.isdigit() == False:
        return("input valid number")
    return(2*(length)+ 2*(width))

def area(length, width):
    if length.isdigit() == False or width.isdigit() == False:
        return("input valid number")
    return(length * width)