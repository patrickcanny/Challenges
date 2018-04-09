from collections import Counter
 
def add(contact):
    return [contact[:i] for i in range (1, len(contact)+1)] 

count = Counter()
n = int(raw_input().strip())

for a0 in range(n):
    op, contact = raw_input().strip().split(' ')
    if op == 'add':
        count.update(add(contact))
    elif op == 'find':
        print(count.get(contact, 0))
