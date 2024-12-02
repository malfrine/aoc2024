left = []
right = []

with open("input.txt") as f:
    while s:= f.readline():
        l, r, *_ = s.split("   ")
        left.append(int(l))
        right.append(int(r))


left = sorted(left)
right = sorted(right)

diff = 0
for l, r in zip(left, right):
    diff += abs(l - r)

right_count = {}
for r in right:
    if r in right_count:
        right_count[r] += 1
    else:
        right_count[r] = 1

similarity = 0
for l in left:
    similarity += l * right_count.get(l, 0)

print(diff)
print(similarity)