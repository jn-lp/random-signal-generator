from array import array


def average(signals):
    return sum(signals) / len(signals)


def dispersion(signals):
    avg = average(signals)
    return sum(map(lambda sig: pow(avg - sig, 2), signals)) / len(signals)


def correlation(sigs1, sigs2):
    l = len(sigs1)
    assert l == len(sigs2)

    m1 = average(sigs1)
    m2 = average(sigs2)

    res = []
    for i in range(l):
        res.append((sigs1[i] - m1) * (sigs2[i] - m2))

    return sum(res) / (l - 1)


def correlation_array(sigs1, sigs2):
    l = len(sigs1)
    assert l == len(sigs2)

    m1 = average(sigs1)
    m2 = average(sigs2)

    res = array("f")
    for i in range(l):
        res.append((sigs1[i] - m1) * (sigs2[i] - m2))

    return sum(res) / (l - 1)


def autocorrelation(sigs):
    l = int(len(sigs) / 2)
    f_sigs1 = sigs[0:l]

    corr = []
    for i in range(l):
        corr.append(correlation(f_sigs1, sigs[i:(i+l)]))

    return corr


def crosscorrelation(sigs1, sigs2):
    l = int(len(sigs1) / 2)
    f_sigs1 = sigs1[0:l]

    corr = []
    for i in range(l):
        corr.append(correlation(f_sigs1, sigs2[i:(i+l)]))

    return corr
