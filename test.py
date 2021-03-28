import bstats

x = [84, 86, 89, 92, 82, 86, 89, 92, 80, 86, 80, 90, 87, 83]

print('Total number of data   : {} data'.format(len(x)))
print('Mean                   :', bstats.mean(x))
print('Median                 :', bstats.median(x))
print('Mode                   :', bstats.mode(x))
print('Variance               :', bstats.var(x))
print('Standar Deviation      :', bstats.stdev(x))

bstats.describe(x)