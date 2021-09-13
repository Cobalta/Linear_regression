import tools as tl

# READING
r_info = open("r_info.txt","r")
Lines = r_info.readlines()
print(Lines)
t0 = float(Lines[0][3:])
t1 = float(Lines[1][3:])
y_minmax = [int(Lines[2][5:]),int(Lines[3][5:])]
x_minmax = [int(Lines[4][5:]),int(Lines[5][5:])]

#INPUT
print("Kilométrage ?")
kilo = input()

#COMPUTING
kilonorm = tl.normalize(float(kilo), x_minmax)
yhatnorm = (float(kilonorm) * t1) + t0
yhat = tl.denormalize(yhatnorm, y_minmax)

print("Le prix estimé est de " + str(yhat))