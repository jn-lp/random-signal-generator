import matplotlib
import matplotlib.pyplot as plt
import rsg
import stats

HARMONICS = 8
FREQUENCY = 1200
N = 1024

COMPLEXITY_LIMIT = 16384

sigs = rsg.generate(HARMONICS, FREQUENCY, N)

print("Math Expectation", stats.average(sigs))
print("Math Dispersion", stats.dispersion(sigs))

fig, (ax1, ax2) = plt.subplots(2, 1)
plt.tight_layout(pad=4)

ax1.plot(sigs)
ax1.set(xlabel='time', ylabel='signal',
        title='Random generated signals')

ax2.plot(rsg.complexity(1024))
ax2.set(xlabel='number of intervals', ylabel='time',
        title='Complexity of algorithm')

fig.savefig("test.png")
plt.show()
