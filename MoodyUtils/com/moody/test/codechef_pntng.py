'''
Created on 23-Jun-2014

@author: brij
'''

inp = raw_input().split()
N, M, H = int(inp[0]), int(inp[1]), int(inp[2])

T = []
C = []

t_sum = 0
for i in xrange(H):
    temp = raw_input().split()
    T.append(int(temp[0]))
    C.append(int(temp[1]))
    t_sum += int(temp[0])

if t_sum < (N*M):
    print "Impossible"
else:
    sort_index = sorted(range(len(C)), key=lambda k: C[k])
    cost = 0
    total = M * N
    k = 0
    while total > 0:
        if T[sort_index[k]] <= total:
            cost += (T[sort_index[k]] * C[sort_index[k]])
            total -= T[sort_index[k]]
            k += 1
        else:
            cost += (total * C[sort_index[k]])
            break
        
    print cost

    