import random
import numpy as np
from math import *
from matplotlib import pyplot as plt
from matplotlib import patches, figure
import collections
import time


def frange(start, stop, inc):
    while start <= stop:
        yield start
        start += inc

        
def bootstrap(x, confidence = 0.68, nsamples = 100):
    def mean(S): 
        return float(sum(x for x in S))/len(S)
    means = [mean(resample(x)) for k in xrange(nsamples)]
    means.sort()
    left_tail = int(((1.0-confidence)/2)*nsamples)
    right_tail = nsamples-1-left_tail    
    return means[left_tail], mean(x), means[right_tail]


def resample(S,size=None):
    return [random.choice(S) for i in xrange(size or len(S))]


def E(f,S): 
    return float(sum(f(x) for x in S))/(len(S) or 1)


def mean(X): 
    return E(lambda x:x, X)