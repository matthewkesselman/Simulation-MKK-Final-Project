#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Feb 19 21:31:28 2023

@author: matthewkesselman
"""

## Uniform generators
import random
# from mpl_toolkits import mplot3d

# import numpy as np
import matplotlib.pyplot as plt


class randu():
    
    def __init__(self, seed=77): # other seed test used = 33
        self.seed = seed
        self.current_state = 65539 * seed % 2**31
        self.next_state = 65539 * self.current_state % 2**31
        
    def getNextState(self):
        self.current_state = self.next_state
        self.next_state = 65539 * self.current_state % 2**31
        
        return self.current_state
    
    def getDenom(self):
        return 2**31
        
    
class parkMillerOne():
    
    def __init__(self, seed=77):
        self.seed = seed
        self.current_state = 16807 * seed % (2**31-1)
        self.next_state = 16807 * self.current_state % (2**31-1)
        
    def getNextState(self):
        self.current_state = self.next_state
        self.next_state = 16807 * self.current_state % (2**31-1)
        
        return self.current_state
        
    def getDenom(self):
        return (2**31-1)
    
class parkMillerTwo():
    
    def __init__(self, seed=77):
        self.seed = seed
        self.current_state = 48271 * seed % (2**31-1)
        self.next_state = 48271 * self.current_state % (2**31-1)
        
    def getNextState(self):
        self.current_state = self.next_state
        self.next_state = 48271 * self.current_state % (2**31-1)
        
        return self.current_state
        
    def getDenom(self):
        return (2**31-1)
    

class advancedLehmerLCG():
    
    def __init__(self, seed=77):
        self.seed = seed
        self.current_state = 50653 * seed % (2**61-1)
        self.next_state = 50653 * self.current_state % (2**61-1)
        
    def getNextState(self):
        self.current_state = self.next_state
        self.next_state = 50653 * self.current_state % (2**61-1)
        
        return self.current_state
        
    def getDenom(self):
        return (2**61-1)
    
class simpleLCG():
    def __init__(self, seed=77):
        self.seed = seed
        self.current_state = 17 * (seed+2) % (94)
        self.next_state = 17 * (self.current_state+2) % (94)
        
    def getNextState(self):
        self.current_state = self.next_state
        self.next_state = 17 * (self.current_state+2) % (94)
        
        return self.current_state
        
    def getDenom(self):
        return (94)
    
    
class midSquareMethod():
    def __init__(self, seed=7543): # seed must be 4 digit number, other seed test used = 5473
        self.seed = seed
        self.current_state = int(str(seed**2).zfill(8)[2:6])
        self.next_state = int(str(self.current_state**2).zfill(8)[2:6])
        
    def getNextState(self):
        self.current_state = self.next_state
        self.next_state = int(str(self.current_state**2).zfill(8)[2:6])
        
        return self.current_state
        
    def getDenom(self):
        return 10000
   
    
def getResults(generator, size=100000):    
    nums = []
    uniforms = []
    
    for i in range(0, size):
        nums.append(generator.getNextState())
        uniforms.append(nums[i]/generator.getDenom())
    
    return nums, uniforms
    
randuNums, randuUniforms = getResults(randu())
parkMillerOneNums, parkMillerOneUniforms = getResults(parkMillerOne())
parkMillerTwoNums, parkMillerTwoUniforms = getResults(parkMillerTwo())
advancedLehmerLCGNums, advancedLehmerLCGUniforms = getResults(advancedLehmerLCG())
simpleNums, simpleUniforms = getResults(simpleLCG())

def getMersenne(size=100000):
    mersenneUniforms = []

    for i in range(0, size):
        mersenneUniforms.append(random.random())
    
    return mersenneUniforms
    
mersenneUniforms = getMersenne()
midSquareNums, midSquareUniforms = getResults(midSquareMethod())


def graphingHistogram (uniforms, name=''):
    plt.clf()
    plt.hist(uniforms,50)
    plt.title(name)
    return plt

# graphingHistogram(randuUniforms, 'RANDU HISTOGRAM').show()
# graphingHistogram(simpleUniforms, 'SIMPLE HISTOGRAM').show()
# graphingHistogram(parkMillerOneUniforms, 'PARK MILLER ONE HISTOGRAM').show()
# graphingHistogram(parkMillerTwoUniforms, 'PARK MILLER TWO HISTOGRAM').show()
# graphingHistogram(advancedLehmerLCGUniforms, 'ADVANCED LEHMER LCG HISTOGRAM').show()
# graphingHistogram(mersenneUniforms, 'MERSENNE TWISTER HISTOGRAM').show()
# graphingHistogram(midSquareUniforms, 'MIDSQUARE HISTOGRAM (n=100000)').show()

midSquareNums2, midSquareUniforms2 = getResults(midSquareMethod(),size=100)
# graphingHistogram(midSquareUniforms2, 'MIDSQUARE HISTOGRAM (n=100)').show()

midSquareNums3, midSquareUniforms3 = getResults(midSquareMethod(),size=30)
# graphingHistogram(midSquareUniforms3, 'MIDSQUARE HISTOGRAM (n=30)').show()

midSquareNums4, midSquareUniforms4 = getResults(midSquareMethod(),size=10)
# graphingHistogram(midSquareUniforms4, 'MIDSQUARE HISTOGRAM (n=10)').show()


graphingHistogram(randuUniforms, 'RANDU HISTOGRAM').savefig('randu2D.png', bbox_inches='tight', dpi=300)
graphingHistogram(simpleUniforms, 'SIMPLE HISTOGRAM').savefig('simple2D.png', bbox_inches='tight', dpi=300)
graphingHistogram(parkMillerOneUniforms, 'PARK MILLER ONE HISTOGRAM').savefig('parkMillerOne2D.png', bbox_inches='tight', dpi=300)
graphingHistogram(parkMillerTwoUniforms, 'PARK MILLER TWO HISTOGRAM').savefig('parkMillerTwo2D.png', bbox_inches='tight', dpi=300)
graphingHistogram(advancedLehmerLCGUniforms, 'ADVANCED LEHMER LCG HISTOGRAM').savefig('advancedLehmerLCG2D.png', bbox_inches='tight', dpi=300)
graphingHistogram(mersenneUniforms, 'MERSENNE TWISTER HISTOGRAM').savefig('mersenneTwister2D.png', bbox_inches='tight', dpi=300)
graphingHistogram(midSquareUniforms, 'MIDSQUARE HISTOGRAM (n=100000)').savefig('midsquareMethod (n=100K) 2D.png', bbox_inches='tight', dpi=300)
graphingHistogram(midSquareUniforms2, 'MIDSQUARE HISTOGRAM (n=100)').savefig('midsqaureMethod (n=100) 2D.png', bbox_inches='tight', dpi=300)
graphingHistogram(midSquareUniforms3, 'MIDSQUARE HISTOGRAM (n=30)').savefig('midsqaureMethod (n=30) 2D.png', bbox_inches='tight', dpi=300)
graphingHistogram(midSquareUniforms4, 'MIDSQUARE HISTOGRAM (n=10)').savefig('midsqaureMethod (n=10) 2D.png', bbox_inches='tight', dpi=300)





def graphing3D (uniforms, name=""):
    plt.clf()
    tuplesForGraphing = []
    for i in range(2, len(uniforms)):
        tuplesForGraphing.append((uniforms[i-2],uniforms[i-1],uniforms[i]))
        
    ax = plt.axes(projection='3d')
    x, y, z = zip(*tuplesForGraphing)
    ax.scatter3D(x, y, z, c=z, cmap='winter');
    
    ax.view_init(-140, 60)
    plt.title(name)


    return plt

# graphing3D(randuUniforms, 'RANDU TUPLES').show()
# graphing3D(simpleUniforms, 'SIMPLE TUPLES').show()
# graphing3D(parkMillerOneUniforms, 'PARK MILLER ONE TUPLES').show()
# graphing3D(parkMillerTwoUniforms, 'PARK MILLER TWO TUPLES').show()
# graphing3D(advancedLehmerLCGUniforms, 'ADVANCED LEHMER LCG TUPLES').show()
# graphing3D(mersenneUniforms, 'MERSENNE TWISTER TUPLES').show()
# graphing3D(midSquareUniforms, 'MIDSQUARE TUPLES').show()

graphing3D(randuUniforms, 'RANDU TUPLES').savefig('randu3D.png', bbox_inches='tight', dpi=300)
graphing3D(simpleUniforms, 'SIMPLE TUPLES').savefig('simple3D.png', bbox_inches='tight', dpi=300)
graphing3D(parkMillerOneUniforms, 'PARK MILLER ONE TUPLES').savefig('parkMillerOne3D.png', bbox_inches='tight', dpi=300)
graphing3D(parkMillerTwoUniforms, 'PARK MILLER TWO TUPLES').savefig('parkMillerTwo3D.png', bbox_inches='tight', dpi=300)
graphing3D(advancedLehmerLCGUniforms, 'ADVANCED LEHMER LCG TUPLES').savefig('advancedLehmerLCG3D.png', bbox_inches='tight', dpi=300)
graphing3D(mersenneUniforms, 'MERSENNE TWISTER TUPLES').savefig('mersenneTwister3D.png', bbox_inches='tight', dpi=300)
graphing3D(midSquareUniforms, 'MIDSQUARE TUPLES').savefig('midsquare3D.png', bbox_inches='tight', dpi=300)


 
def goodnessOfFit(uniforms, k=8): # Chi-squared test (5 groups)
    
    grps = []

    for z in range(0, k):
        sums = sum(1 for i in uniforms if i>(1/k)*z and i<=(1/k)*(z+1))
        grps.append(sums)

    expectedDistribution = len(uniforms)/k
    chiSquaredScore = 0
    
    for group in grps:
        chiSquaredScore += ((group - expectedDistribution)**2/expectedDistribution)
    

    return chiSquaredScore, grps

chi1,g = goodnessOfFit(randuUniforms, 5)
chi2,g = goodnessOfFit(simpleUniforms, 5)
chi3,g = goodnessOfFit(mersenneUniforms, 5)
chi4,g = goodnessOfFit(parkMillerOneUniforms, 5)
chi5,g = goodnessOfFit(parkMillerTwoUniforms, 5)
chi6,g = goodnessOfFit(advancedLehmerLCGUniforms, 5)
chi7,g = goodnessOfFit(midSquareUniforms, 5)



def updownTest(uniforms):
    upFlag = 0
    runs = 0
    
    for i in range(1, len(uniforms)):
        if(uniforms[i]>uniforms[i-1] and upFlag==0):
            runs+=1
            upFlag = 1
        if(uniforms[i]<uniforms[i-1] and upFlag==1):
            runs+=1
            upFlag=0
    
    expectedRuns = (2*len(uniforms)-1) / 3
    expectedDeviation = (16*len(uniforms)-29)/90
    
    z_score = (runs-expectedRuns)/(expectedDeviation**.5)
    
    return z_score, runs, expectedRuns

        
z_score1, runs, expectedRuns = updownTest(randuUniforms)
z_score2, runs, expectedRuns = updownTest(simpleUniforms)
z_score3, runs, expectedRuns = updownTest(mersenneUniforms)
z_score4, runs, expectedRuns = updownTest(parkMillerOneUniforms)
z_score5, runs, expectedRuns = updownTest(parkMillerTwoUniforms)
z_score6, runs, expectedRuns = updownTest(advancedLehmerLCGUniforms)
z_score7, runs, expectedRuns = updownTest(midSquareUniforms)


#  lag 1 correlation
def correlationTests(uniforms):
    p_hat = 0
    n = len(uniforms)
    
    for i in range(0, n-1):
        p_hat += uniforms[i]*uniforms[i+1]
        
    p_hat = (p_hat*(12/(n-1))) - 3
    var_p_hat = (13*n - 19)/((n-1)**2)
    
    z_score = p_hat/(var_p_hat**.5)
    
    return z_score, p_hat

z_score1_corr_test, p_hat1 = correlationTests(randuUniforms)
z_score2_corr_test, p_hat2 = correlationTests(simpleUniforms)
z_score3_corr_test, p_hat3 = correlationTests(mersenneUniforms)
z_score4_corr_test, p_hat4 = correlationTests(parkMillerOneUniforms)
z_score5_corr_test, p_hat5 = correlationTests(parkMillerTwoUniforms)
z_score6_corr_test, p_hat6 = correlationTests(advancedLehmerLCGUniforms)
z_score7_corr_test, p_hat7 = correlationTests(midSquareUniforms)


import time
def timedRun(uniform, size=100000, mersenne=False):
    if mersenne:
        start = time.time()
        getMersenne(size)
        end = time.time()
    else:
        start = time.time()
        getResults(uniform,size=size)
        end = time.time()

    return end-start


timedParkMillerOne = timedRun(uniform = parkMillerOne(),size=1000000)
timedParkMillerTwo = timedRun(uniform = parkMillerTwo(),size=1000000)
timedAdvancedLehmerLCG = timedRun(uniform = advancedLehmerLCG(),size=1000000)
timedRandU = timedRun(uniform = randu(),size=1000000)
timedsimpleNums = timedRun(uniform = simpleLCG(),size=1000000)
timedMidSquare = timedRun(uniform = midSquareMethod(),size=1000000)
timedMersenne = timedRun(uniform = "",size=1000000,mersenne=True)




# X^2 goodness of fit tests, runs test, means test, von Neumann test for indepdence
# run-time efficiency of generators
