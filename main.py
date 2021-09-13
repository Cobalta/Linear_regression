import matplotlib.pyplot as plt
import pandas as pd
import tools as tl

#INIT
r_info = open("r_info.txt","w")
t0sum, t1sum, t0, t1, i = 0, 0, 0, 0, 0
ratio = 0.01
size = 50
x, y, xnorm, ynorm, yhat = [], [], [], [], []
tl.read_data(x, y)
minmax_x = [min(x), max(x)]
minmax_y = [min(y), max(y)]
for elem in x:
    xnorm.append(tl.normalize(elem, minmax_x))
for elem in y:
    ynorm.append(tl.normalize(elem, minmax_y))
ylen = len(y)
yhatnorm = [0] * ylen

#REGRESSION
o = 0
while o < 10000:
    while i < ylen:
        t0sum += yhatnorm[i] - ynorm[i]
        i += 1
    i = 0
    while i < ylen:
        t1sum += (yhatnorm[i] - ynorm[i]) * xnorm[i]
        i += 1
    i = 0
    t0 -= ratio * (1/ylen) * t0sum
    t1 -= ratio * (1/ylen) * t1sum
    while i < ylen:
        yhatnorm[i] = t0 + (t1 * xnorm[i])
        i += 1
    i = 0
    o += 1

#DENORM
minmax_yhatnorm = [min(yhatnorm), max(yhatnorm)]
for elem in yhatnorm:
    yhat.append(tl.denormalize(elem, minmax_y))

#WRITE
r_info.write("t0 " + str(t0) + "\n")
r_info.write("t1 " + str(t1) + "\n")
r_info.write("ymin " + str(minmax_y[0]) + "\n")
r_info.write("ymax " + str(minmax_y[1]) + "\n")
r_info.write("xmin " + str(minmax_x[0]) + "\n")
r_info.write("xmax " + str(minmax_x[1]) + "\n")

#DISPLAY
df = pd.DataFrame({'kilo': x, 'prix': y})
df2 = pd.DataFrame({'x': x, 'estimation': yhat})
plt.plot('kilo', 'prix', data=df, linestyle='none', marker='o')
plt.plot('x', 'estimation', data=df2, linestyle='solid', marker='x')
plt.legend()
plt.show()
