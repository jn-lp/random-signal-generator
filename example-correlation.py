import matplotlib
import matplotlib.pyplot as plt
import rsg
import stats

HARMONICS = 8
FREQUENCY = 1200
N = 1024

COMPLEXITY_LIMIT = 16384

sigs1 = rsg.generate(HARMONICS, FREQUENCY, N)
sigs2 = rsg.generate(HARMONICS, FREQUENCY, N)

fig, (ax1, ax2) = plt.subplots(2, 1)
plt.tight_layout(pad=4)


ax1.plot(list(range(N)), sigs1, c="g", label="signal")
ax1.plot(list(range(int(N/2))), stats.autocorrelation(sigs1),
         linewidth=5, label="corelation", alpha=0.5)

ax1.set_xlim(0, int(N/8))
ax1.set(ylabel='correlation', xlabel='τ',
        title='Autocorrelation')

ax2.plot(list(range(N)), sigs1, c="g", label="signal 1")
ax2.plot(list(range(N)), sigs2, c="r", label="signal 2")
ax2.plot(list(range(int(N/2))), stats.crosscorrelation(sigs1, sigs2),
         linewidth=5, label="corelation", alpha=0.5)
ax2.plot()

ax2.set_xlim(0, int(N/8))
ax2.set(ylabel='correlation', xlabel='τ',
        title='Сross-correlation')

fig.savefig("example-coorelation.png")
plt.show()
