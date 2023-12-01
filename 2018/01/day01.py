# part 1
# ==================================================
# load the input file
with open("input.txt", "r") as f:
    problem = f.read()


changes = [int(n.strip()) for n in problem.split() if n.strip()]
print(sum(changes))


# part 2
# ==================================================
from itertools import accumulate, cycle

seen = set()
print(next(f for f in accumulate(cycle(changes)) if f in seen or seen.add(f)))

