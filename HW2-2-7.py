import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as plt

g = 9.8
t = np.linspace(0, 100, 1000)
x_0 = -209
y_0 = 80
v_x_0 = 44.4
v_y_0 = 0 

#parametric equations when rejecting air resistance
def x_freefall(t, x_0, v_x_0):
    return v_x_0*t+x_0
    
def y_freefall(t, y_0, v_y_0):
    return -g/2*(t**2)+v_y_0*t+y_0

#parametric equations when air resistance is introduced
dt = .0005
c_w = 0.8
A = 0.2
m = 30
rho = 1
alpha = (c_w*rho*A)/(2*m)

x_position = [x_0+55.24195160930993-30]
y_position = [y_0]

x_velocity = [v_x_0]
y_velocity = [v_y_0]

#takes the current index as an argument, this will be incremented while looping, should begin at 0 and loop until i = 999, 1000 pts
def append_next_velocity_y(i):
    next_velocity_y = ((-alpha*np.sqrt(x_velocity[i]**2+y_velocity[i]**2))*y_velocity[i]-(g))*dt
    y_velocity.append(next_velocity_y+y_velocity[i])

def append_next_velocity_x(i):
    next_velocity_x = (-alpha*np.sqrt(x_velocity[i]**2+y_velocity[i]**2))*x_velocity[i]*dt
    x_velocity.append(next_velocity_x+x_velocity[i])
    
def append_next_x(i):
    next_x_postion = (x_velocity[i]*dt)
    x_position.append(next_x_postion+x_position[i])
    
def append_next_y(i):
    next_y_positon = (y_velocity[i]*dt)
    y_position.append(y_position[i]+next_y_positon)

#fill x-velocity list, y-velocity list, x-postion list, and y-position list, respectively
i=0
while(i<10000):
    append_next_velocity_x(i)
    append_next_velocity_y(i)
    i+=1

j=0
while(j<10000):
    if(y_position[j]<0):
        break
    append_next_x(j)
    append_next_y(j)
    j+=1

def total_time():
    total_time = (len(x_position)-1)*dt
    return total_time

#plot commands
plt.ylim(0, 80)
plt.xlim(-250,0)
plt.xlabel("x-displacement (m)")
plt.ylabel("y-displacement (m)")
plt.plot(x_position, y_position, label = "Drag Proportional to v^2")
plt.plot(x_freefall(t, -209, 44.4), y_freefall(t, 80, 0), label = "Drag Neglected")
plt.scatter(-30, 0, label = "Target")
plt.scatter(0,0, label = "Cattle (0,0)")
plt.title("Plot of Trajectories (HW3 - 2.7)")
plt.legend()
plt.show()

t = PrettyTable()
t.field_names = ['Drop Position: ','Final Y-Position (drag): ','Final x-position (drag): ', 'Total time: ']
t.add_row(['%.3f'%x_position[0], '%.3f'%y_position[j-1], '%.3f'%x_position[j-1], '%.3f'%total_time()])
print(t)
