import serial
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
            n.append(float(i))

    l = [n[i:i + 3] for i in range(0, len(n), 3)]
    for i in range(len(l)):
        l[i][1] = l[i][1]*step*m.pi/180
        l[i][2] = l[i][2]*step*m.pi*3/180

    l.pop()
    print(l[1:10])
    return l

#get_data()