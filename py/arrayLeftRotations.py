#A left rotation denotes a movement of each element of an array to the left
#i.e. [1, 2, 3, 4] rotated once will become [4, 1, 2, 3]

#Given a starting array and a number of left rotations, return the final array

from collections import deque
def array_left_rotation(a, n, k):
        d = deque(a, maxlen = n)
            for _ in range (k):
                        d.append(d.popleft())
                            return d




 n, k = map(int, raw_input().strip().split(' '))
 a = map(int, raw_input().strip().split(' '))
 answer = array_left_rotation(a, n, k);
 print ' '.join(map(str,answer))
