import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity



# Generate 1D data from normal distribution
nbpts = 50 # Number of points to generate
mu = 1 # the mean
sigma = 2 # the standard deviation

data = np.random.normal(mu,sigma,(nbpts,1)) # makes a column vector

# Create histogram. By default, this will show how many points fall in each bin.
bins = 10 # This specifies the number of bins, Python decides the interval. This can be OK but means you do not specify exactly where the bins are.
plt.hist(data, bins)
plt.show()


'''
# A different specification
edges = np.linspace(-5,8,14) # This specifies the number of bins and also where the first bin starts from
plt.hist(data, edges)
plt.show()
'''

'''
# Another specification
binsize = 1
edges = np.arange(-5,8,binsize) # This specifies a sequence defining the left edge of each bin (and, indirectly, the number of bins)
plt.hist(data,edges)
plt.show()
'''

