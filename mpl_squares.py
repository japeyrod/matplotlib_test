import matplotlib.pyplot as plt

a = 1
squares = []
for i in range(10):
    a += a
squares = [1, 4, 9, 16, 25]
plt.plot(squares)
plt.show()