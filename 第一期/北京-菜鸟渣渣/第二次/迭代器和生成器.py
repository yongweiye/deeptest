#coding=utf-8
import  sys
'''
seq_tuple = (1, 2, 3, 4, 5)

while_it = iter(seq_tuple)
while True:
    try:
        print(next(while_it))
    except Exception:
        sys.exit()
'''
def fab(max):
   n, a, b = 0, 0, 1
   L = []
   while n < max:
       L.append(b)
       a, b = b, a + b
       n = n + 1
   return L
f = iter(fab(1000))
while True:
    try:
        print (next(f))
    except StopIteration:
        sys.exit()