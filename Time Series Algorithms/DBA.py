import numpy as np
from DTW import dtw

def dba(D,iter):
    T = np.mean(D,axis=0)
    for i in xrange(iter):
        T = dba_update(T,D)

    return T

def dba_update(Tinit , D):
    alignment = [None]*len(Tinit)
    for S in D:
        alignment_for_S = DTW_multiple_alignment(Tinit,S)
        for i in xrange(len(Tinit)):
            if alignment_for_S[i] != None:
                if alignment[i] != None:
                    alignment[i].extend(alignment_for_S[i])
                else:
                    alignment[i] = alignment_for_S[i]
    
    T = [None]*len(Tinit)

    for i in xrange(len(Tinit)):
         T[i] = float(sum(alignment[i]))/len(alignment[i])

    return T

def DTW_multiple_alignment(Sref , S):
    cost = dtw(Sref,S)
    L = len(Sref)
    alignment = [None]*len(Sref)
    i,j = len(Sref)-1 , len(S)-1
    while i>=0 and j>=0:
        if alignment[i] != None:
                alignment[i].extend([S[j]])
        else:
            alignment[i] = [S[j]]
        if i==0:
            j = j-1
        elif j==0:
            i = i-1
        else:
            score = min(cost[i-1][j-1],cost[i][j-1],cost[i-1][j])
            if score == cost[i-1][j-1]:
                i = i-1
                j = j-1
            elif score == cost[i-1][j]:
                i = i-1
            else:
                j = j-1

    return alignment


