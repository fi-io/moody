'''
Created on 29-Jun-2014

@author: brij
'''

import sys
t = int(raw_input())
for i in xrange(t):
    k = list(raw_input())
    length = len(k)
    mid = (length + 1) / 2
    odd = length & 1
    
    p = (mid - 2) if odd else (mid - 1)
    q = mid
    ok = False
    while p >= 0 and q < length:
        if k[p] > k[q]:
            k[q] = k[p]
            ok = True
        elif k[p] == k[q]:
            pass
        else:
            break
        p -= 1
        q += 1
    #print k, ok
    
    if not ok:
        p = mid - 1
        q = (mid - 1) if odd else mid
        carry = 1
        while p >= 0 or carry:
            a = int(k[p]) if p >= 0 else 0
            k[q] = str((a + carry) % 10)
            carry = (a + carry) / 10
            p -= 1
            q += 1
        #k = k[:q] + '0' + k[q+1:]
        
        p = 0
        q = q - 1
        while p < q:
            k[p] = k[q]
            p += 1
            q -= 1

    print ''.join(k)
sys.exit(0)
     
        
