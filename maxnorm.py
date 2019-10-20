import numpy as np
ntrials=10000
sum=0
for N in range(1,201):
    sum=0
    for trial in range(ntrials):
        vars=np.random.normal(size=N)
        vars.sort()
        sum+=vars[N-1]
        ##sum+=np.amax(vars) #alternatively, we can use this function to find the max value of vars
    sum/=ntrials #average largest value from random number generator
    print(N,sum)