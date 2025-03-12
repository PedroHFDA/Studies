# count é um iterator sem fim (itertools)

import itertools

c1 = itertools.count()

for i in c1:
    if i > 100:
        break
    
    print(i)