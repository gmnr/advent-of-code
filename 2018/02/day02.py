with open('input.txt', 'r') as f:
	problem = f.read().split()

# part 1
# ==================================================
from collections import Counter


two = 0
three = 0

for box in problem:
    count = Counter(box)
    if len([k for k,v in count.items() if v == 2]) > 0:
        two += 1
    
    if len([k for k,v in count.items() if v == 3]) > 0:
        three += 1
    
print(f"checksum is {two*three}")

# part 2
# ==================================================
from itertools import combinations, compress


for one, two in combinations(problem, 2):    
    diff = [e1 == e2 for e1,e2 in zip(one,two)]    
    if sum(diff) == (len(one) - 1):
        res2 = ''.join(list(compress(one,diff)))
        break

print(res2)