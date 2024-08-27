def sum(paralist):
    x=0
    for i in paralist:
        if i.isdigit() == False:
            return("not all valid numbers")
        x += i
    return(x)


def average(paralist):
    x=0
    for i in paralist:
        if i.isdigit() == False:
            return("not all valid numbers")
        x += i
    x = x/len(paralist)
    return(x)