import  matplotlib.pyplot as plt
from numpy import cos, sin, pi, linspace


plt.figure(figsize=(5,5)) # 5x5 inç boyutunda bir şekil oluştur
plt.grid() #
plt.xlim(-10,10) #x düzlemi için sınır
plt.ylim(-10,10) #y düzlemi için sınır

plt.plot(-7.5, 2.5, marker='4', markerfacecolor='black', markeredgecolor='blue', markersize=12 ) # köşe koordinatları ve markörleri
plt.plot(-7.5,-7.5, markerfacecolor='black', markeredgecolor='blue', markersize=5 )
plt.plot(5, -7.5, markerfacecolor='black', markeredgecolor='blue', markersize=5)

#Triangle
plt.plot((5.0, -7.5, -7.5, 5.0),(-7.5, -7.5, 2.5, -7.5))
plt.fill((5.0, -7.5, -7.5, 5.0),(-7.5, -7.5, 2.5, -7.5), color='red')

plt.savefig('test.png')
plt.show()
#code end