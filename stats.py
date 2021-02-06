def average(signals):
    return sum(signals) / len(signals)


def dispersion(signals):
    avg = average(signals)
    return sum(map(lambda sig: pow(avg - sig, 2), signals)) / len(signals)

