import matplotlib
import matplotlib.pyplot as plt
import rsg
import stats
import time

HARMONICS = 8
FREQUENCY = 1200
Ns = list(map(lambda num: 2 ** num, list(range(1, 20))))

listtimes = list()
arraytimes = list()
for N in Ns:
    start = time.time()
    stats.correlation(rsg.generate(HARMONICS, FREQUENCY, N),
                      rsg.generate(HARMONICS, FREQUENCY, N))
    listtimes.append(time.time() - start)

    start = time.time()
    stats.correlation_array(rsg.generate(HARMONICS, FREQUENCY, N),
                            rsg.generate(HARMONICS, FREQUENCY, N))
    arraytimes.append(time.time() - start)

fig, ax = plt.subplots()

ax.plot(Ns, listtimes, c="g", label="list")
ax.plot(Ns, arraytimes, c="r", label="array")

fig.savefig("example-listvsarray.png")
plt.show()
