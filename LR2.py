# Функции принадлежности
# низкая, средняя и высокая температуры
t = [5, 15, 25]

def temperature_low(x):
    if x <= t[0]:
        return 1
    elif x > t[1]:
        return 0
    else:
        return (t[1] - x) / (t[1] - t[0])

def temperature_mid(x):
    if x < t[0] or x > t[2]:
        return 0
    elif x >= t[0] and x < t[1]:
        return (x - t[0]) / (t[1] - t[0])
    else:
        return (t[2] - x) / (t[2] - t[1])

def temperature_high(x):
    if x >= t[2]:
        return 1
    elif x < t[1]:
        return 0
    else:
        return (x - t[1]) / (t[2] - t[1])

# низкое, среднее и высокое время прогулки (в минутах)
t2 = [30, 80, 150]

def time_low(x):
    if x <= t2[0]:
        return 1
    elif x > t2[1]:
        return 0
    else:
        return (t2[1] - x) / (t2[1] - t2[0])

def time_mid(x):
    if x < t2[0] or x > t2[2]:
        return 0
    elif x >= t2[0] and x < t2[1]:
        return (x - t2[0]) / (t2[1] - t2[0])
    else:
        return (t2[2] - x) / (t2[2] - t2[1])

def time_high(x):
    if x >= t2[2]:
        return 1
    elif x < t2[1]:
        return 0
    else:
        return (x - t2[1]) / (t2[2] - t2[1])

# низкая, средняя1, средняя2 и высокая теплота одежды 
t3 = [25, 45, 65, 85]

def wear_low(x):
    if x <= t3[0]:
        return 1
    elif x > t3[1]:
        return 0
    else:
        return (t3[1] - x) / (t3[1] - t3[0])

def wear_mid(x):
    if x < t3[0] or x > t3[3]:
        return 0
    elif x >= t3[0] and x < t3[1]:
        return (x - t3[0]) / (t3[1] - t3[0])
    elif x >= t3[2] and x < t3[3]:
        return (t3[3] - x) / (t3[3] - t3[2])
    elif x >= t3[1] and x < t3[2]:
        return 1
    else:
        return (t3[3] - x) / (t3[3] - t3[2])

def wear_high(x):
    if x >= t3[3]:
        return 1
    elif x < t3[2]:
        return 0
    else:
        return (x - t3[2]) / (t3[3] - t3[2])

import numpy as np
import matplotlib.pyplot as plt

# temperature
fig = plt.subplots()
x = list(x for x in range(40) )
y = list(temperature_low(x) for x in range(40))
y1 = list(temperature_mid(x) for x in range(40))
y2 = list(temperature_high(x) for x in range(40))
plt.plot(x, y)
plt.plot(x, y2)
plt.plot(x, y1)

fig1 = plt.subplots()
x = list(x for x in range(180) )
y = list(time_low(x) for x in range(180))
y1 = list(time_mid(x) for x in range(180))
y2 = list(time_high(x) for x in range(180))
plt.plot(x, y)
plt.plot(x, y2)
plt.plot(x, y1)

fig2 = plt.subplots()
x = list(x for x in range(100) )
y = list(wear_low(x) for x in range(100))
y1 = list(wear_mid(x) for x in range(100))
y2 = list(wear_high(x) for x in range(100))
plt.plot(x, y)
plt.plot(x, y2)
plt.plot(x, y1)

#plt.show()

# температура на улице
print('Введите температуру на улице: ')
temp = int(input())
print('t = ' + str(temp) + '. MFt1 = ' + str(temperature_low(temp)))
MFt1 = temperature_low(temp)
print('t = ' + str(temp) + '. MFt2 = ' + str(temperature_mid(temp)))
MFt2 = temperature_mid(temp)
print('t = ' + str(temp) + '. MFt3 = ' + str(temperature_high(temp)))
MFt3 = temperature_high(temp)

# время прогулки в минутах
print('Введите время прогулки в минутах: ')
temp = int(input())
print('time = ' + str(temp) + 'min. MFt1 = ' + str(time_low(temp)))
MFs1 = time_low(temp)
print('time = ' + str(temp) + 'min. MFt2 = ' + str(time_mid(temp)))
MFs2 = time_mid(temp)
print('time = ' + str(temp) + 'min. MFt3 = ' + str(time_high(temp)))
MFs3 = time_high(temp)

def MFy1(w):
    return wear_low(w) * max(MFt1, MFs1)

def MFy2(w):
    return wear_mid(w) * min(MFt2, MFs2)

def MFy3(w):
    return wear_high(w) * min(MFt3, MFs3)

fig3 = plt.subplots()
x = list(x for x in range(100) )
y = list(max(MFy1(x), max(MFy2(x), MFy3(x))) for x in range(100))

plt.plot(x, y)

center = sum(x[i] * y[i] for i in range(100)) / sum(y[i] for i in range(100))
print("Центр тяжести: ", center)
plt.show()