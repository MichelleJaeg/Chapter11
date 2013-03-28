import stats

def main ():
    data = stats.getNumbers()
    xbar = stats.mean(data)
    std = stats.stdDev(data)
    xbar2, std2 = stats.meanStdDev(data)
    print (xbar, std, xbar2, std2)
main ()