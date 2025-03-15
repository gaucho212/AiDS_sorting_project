import matplotlib.pyplot as plt

f = open("benchmark_results.txt", "r")
lines = f.readlines()
x = [2**z for z in range(5, 16)]
y = [float(lines[i].split()[3]) for i in range(2, 13)]
y1 = [float(lines[i].split()[3]) for i in range(68, 79)]
y2 = [float(lines[i].split()[3]) for i in range(134, 145)]
y3 = [float(lines[i].split()[3]) for i in range(200, 211)]


f.close()

plt.plot(
    x,
    y,
    label="Shell Sort",
    color="blue",
    linestyle="-",
)
plt.plot(
    x,
    y1,
    label="Heap Sort",
    color="red",
    linestyle="-",
)
plt.plot(
    x,
    y2,
    label="Insertion Sort",
    color="green",
    linestyle="-",
)
plt.plot(
    x,
    y3,
    label="Selection Sort",
    color="yellow",
    linestyle="-",
)
plt.xlabel("List size")
plt.ylabel("Time [s]")
plt.legend()
plt.title("Wykres algorytmow sortujacych")
plt.grid()
plt.yscale("log")
plt.show()
