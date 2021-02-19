# additional task for lab 1.1
import matplotlib
import matplotlib.pyplot as plt
import rsg
import stats

HARMONICS = 8
FREQUENCY = 1200
Ns = list(map(lambda num: 2 ** num, list(range(1, 12))))

Mxs = list()
for N in Ns:
    Mxs.append(stats.average(rsg.generate(HARMONICS, FREQUENCY, N)))

fig, ax = plt.subplots()
ax.plot(Ns, Mxs, c="r")
ax.set_xlim(0, Ns.pop())

fig.savefig("example-mx.png")
plt.show()
