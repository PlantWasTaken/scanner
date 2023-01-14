import time as t
import math as m

def get_data():
    step = 360/2048
    data = open("tcp.txt", "r")
    n = []

    for i in data:
        if(i == '\n'):
            pass
        else:
            n.append(i.split())

    #l = [n[i:i + 3] for i in range(0, len(n), 3)]
    for i in range(len(n)):
        n[i][1] = float(n[i][1])*step*m.pi/180
        n[i][2] = float(n[i][2])*step*m.pi*3/180

    n.pop()
    print(n[1:10])
    return n

#get_data()
