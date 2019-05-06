from scipy.stats import norm
import numpy as np
#find the normal distribution
ans = norm.pdf(0)
print(ans)

#loc = mean, scale = standard deviation
ans2 = norm.pdf(0, loc=5, scale = 10)
print(ans2)

#having a random array and calculating the elements at the same time
r = np.random.randn(10)
ans3 = norm.pdf(r)
print(ans3)

(print(norm.logpdf(r)))

print(norm.cdf(r))
