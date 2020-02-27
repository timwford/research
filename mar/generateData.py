def generateData(samples=40, size=3):
    np.random.seed(20)

    sCount = int(samples / 2)

    multipliers = list(range(sCount))
    multipliers = [2*(x+1) for x in multipliers]


multipliers = multipliers + multipliers[::-1]

  series = []
   for i in range(samples):
        series.append(list(multipliers[i] * np.random.rand(3)))

    return series
