'''
Created on 04-Jun-2014

@author: brij
'''
import sys

N = 3
Nsq = N*N
plen = Nsq*Nsq

def same_row(i, j): return (i / Nsq == j / Nsq)
def same_col(i, j): return (i - j) % Nsq == 0
def same_block(i, j): return (i / (N*Nsq) == j / (N*Nsq) and i % Nsq / N == j % Nsq / N)

def r(a):

    i = a.find('0')
    if i == -1:
        return a
    
    excluded_numbers = set()
    for j in range(plen):
        if same_row(i, j) or same_col(i, j) or same_block(i, j):
            excluded_numbers.add(a[j])

    for m in range(1, Nsq+1):
        if str(m) not in excluded_numbers:
            temp = r(a[:i] + str(m) + a[i + 1:])
            if not temp:
                excluded_numbers.add(str(m))
            else:
                return temp

def printSudoku(res):
	temp = ''
	for i in range(plen):
		#print i, Nsq, (i+1) % Nsq
		if (i+1) % Nsq == 0:
			temp += res[i]
			print temp
			temp = ""
		else:
			temp += res[i] + ' '
	
if __name__ == '__main__':
    if len(sys.argv) == 2 and len(sys.argv[1]) == plen:
        printSudoku(r(sys.argv[1]))
        
    else:
        print 'Usage: python sudoku.py puzzle'
        print '  where puzzle is an 81 character string representing the puzzle read left-to-right, top-to-bottom, and 0 is a blank'
