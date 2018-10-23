import matplotlib.pyplot as plt

a = 1
squares = []
for i in range(10):
    a += a
squares = [1, 4, 9, 16, 25]
input_value = [1, 2, 3, 4, 5]
plt.xlim(0, 10)
# plt.axis([0, 31, 0, 30]);
plt.plot(input_value, squares, "o-")
plt.show()