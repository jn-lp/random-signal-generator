import random
import math
import time


def generate(harmonics, frequency, N):
    signals = [0] * N
    W = frequency / harmonics

    for _ in range(harmonics):
        amplitude = random.random()
        phase = random.random()

        for t in range(N):
            signals[t] += (amplitude * math.sin(W*t + phase))

        W += W

    return signals


def complexity(intervals):
    t = []
    for i in range(intervals):
        start = time.time()
        generate(8, 1200, i)
        t.append(time.time() - start)
    return t
