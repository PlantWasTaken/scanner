import math as m
import plotly.express as px
import time as t
from serii import get_data

def sin(n):
    return m.sin(n)
    

def cos(n):
    return m.cos(n)

def xyzPlot(len, z_angle, xy_angle, armLength):
    len = len #len from sensor ot obj
    z_angle = z_angle
    xy_angle = xy_angle
    armLength = armLength #lenght of arm, sensor is attached to

    dist_sensor_oregon = [0,0,0] #z,x,y | distance form sensor to 0,0,0
    len_sensor_pinne = [0,0,0] #x,y,z| length of stick attached ot sensor
    sensor_obj = [0,len,0] #z,x,y | sensor to obj zxy point| opp,hyp,adj

    relative_len = [0,0,0] #zxy  
    #relative_len = sensor_obj+dist_sensor_oregon+len_sensor_pinne

    #xyz of fiirst seonsor read
    hyp_sensor_obj = len #R
    z_sensor_obj = hyp_sensor_obj*cos(z_angle) #H
    adj_sensor_obj = hyp_sensor_obj*sin(z_angle) #L

    #z_sensor_obj = opp_sensor_obj #H
    x_sensor_obj = adj_sensor_obj*sin(xy_angle)
    y_sensor_obj = adj_sensor_obj*cos(xy_angle)
    sensor_obj[0]= x_sensor_obj #x
    sensor_obj[1]= y_sensor_obj #y
    sensor_obj[2]= z_sensor_obj #z

    #xyz offset correcton for sensor_obj
    #hyp_len_sensor_pinne = armLength #x axis
    #opp_len_sensor_pinne = hyp_len_sensor_pinne*sin(z_angle)
    #adj_len_sensor_pinne = m.sqrt((hyp_len_sensor_pinne**2) -(opp_len_sensor_pinne**2))
    #z_len_sensor_pinne = hyp_len_sensor_pinne*sin(z_angle)
    #x_len_sensor_pinne = adj_len_sensor_pinne*sin(xy_angle)
    #y_len_sensor_pinne = adj_len_sensor_pinne*cos(xy_angle)
    #len_sensor_pinne[0] = x_len_sensor_pinne
    #len_sensor_pinne[1] = y_len_sensor_pinne
    #len_sensor_pinne[2] = z_len_sensor_pinne
#
    #relative_len[0] = len_sensor_pinne[0] + sensor_obj[0] + dist_sensor_oregon[0]
    #relative_len[1] = len_sensor_pinne[1] + sensor_obj[1] + dist_sensor_oregon[1]
    #relative_len[2] = len_sensor_pinne[2] + sensor_obj[2] + dist_sensor_oregon[2]
#
    #x = relative_len[0]
    #y = relative_len[1]
    #z = relative_len[2]
    x =x_sensor_obj
    y =y_sensor_obj
    z = z_sensor_obj

    
    if(z > 200 or y > 10000 or x < 0 or x > 10000 or z<0):
        return [0,0,0,0]
    else:
        return [x,y,z]
    #return [x,y,z]
X = []
Y = []
Z = []


#for i in range(1000):
    #print(float(ser.readline().decode('utf-8').rstrip()))


print("Workijng...")
#data = scan()
data = get_data()

for i in data:
    xyz_plot = xyzPlot(float(i[0]), float(i[1]), float(i[2]),4) #len z x
    X.append(xyz_plot[0])
    Y.append(xyz_plot[1])
    Z.append(xyz_plot[2])
    #print(xyz_plot)
print(len(X))

fig = px.scatter_3d(x=X, y=Y, z=Z)
fig.show()
